from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail, Message

app = Flask(__name__,template_folder='template')

app.config['SECRET_KEY'] = 'ang_sikreto_ay_mananatiling_lihim' #specify the parameters of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #specify the parameters of the database, running the program will automatically create
# a new folder directory instance with a data.db file
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'carleyeshield21@gmail.com'
app.config['MAIL_PASSWORD'] ='ejqkwgqsbylewfub
'
db = SQLAlchemy(app)

class Form(db.Model): #this will create a table in which can be viewed in the sqlite app
    id = db.Column(db.Integer, primary_key=True) #as an indentifier of each row of the table
    firstname = db.Column(db.String(80)) #column name of the table in the database
    lastname = db.Column(db.String(80)) #column name of the table in the database
    email = db.Column(db.String(80)) #column name of the table in the database
    date = db.Column(db.Date) #column name of the table in the database
    occupation = db.Column(db.String(80)) #column name of the table in the database

@app.route("/", methods=['GET','POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['lust_name']
        email = request.form['email']
        date = request.form['date'] #this will produce a sqlalchemy.exc.StatementError: (builtins.TypeError) SQLite Date type only accepts Python
        # date objects as input, because of the type of variable should be a date type according to the class Form that we have created,
        # we must convert this variable using the datetime class
        converted_date = datetime.strptime(date, '%Y-%m-%d')
        occupation = request.form['occupation']
        print(first_name)
        print(last_name)
        print(email)
        print(occupation)

        #creating an instance of the class Form
        form = Form(firstname=first_name, lastname=last_name, email=email, date=converted_date, occupation=occupation) #arguments should come from the column
        # names you created in the table from the Form class
        db.session.add(form)
        db.session.commit()

        flash('Your form was submitted', 'warning')

    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all() #this will execute the creation of the table
        app.run(debug=True,port=5001)
