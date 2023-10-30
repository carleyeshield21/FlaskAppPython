from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template')
app.config['SECRET KEY'] = 'ang_sikreto_ay_mananatiling_lihim' #specify the parameters of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #specify the parameters of the database
db = SQLAlchemy(app)

@app.route("/", methods=['GET','POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['lust_name']
        email = request.form['email']
        occupation = request.form['occupation']
        print(first_name)
        print(last_name)
        print(email)
        print(occupation)

    return render_template("index.html")

app.run(debug=True,port=5001)






# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')
