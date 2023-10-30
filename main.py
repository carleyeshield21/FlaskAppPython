from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template')

app.config['SECRET KEY'] = 'ang_sikreto_ay_mananatiling_lihim' #specify the parameters of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #specify the parameters of the database, running the program will automatically create
# a new folder directory instance with a data.db file
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
        date = request.form['date']
        occupation = request.form['occupation']
        print(first_name)
        print(last_name)
        print(email)
        print(occupation)

        #creating an instance of the class Form
        form = Form(first_name=first_name, last_name=last_name, email=email, date=date)

    return render_template("index.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all() #this will execute the creation of the table
        app.run(debug=True,port=5001)
