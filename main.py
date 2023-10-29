from flask import Flask, render_template

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True,port=5001)






# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')
