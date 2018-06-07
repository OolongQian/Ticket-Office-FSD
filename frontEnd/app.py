from flask import Flask
from utility.pipeline import PipeLine
from flask import request, render_template, abort, redirect, url_for, session

# set backend executable path
database_exec_path = './backend/train'

app = Flask(__name__)
app.pl = PipeLine(database_exec_path)


@app.route('/', methods=['GET'])
def home(): 
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    # request for signin page and fill the form
    if request.method == 'GET': 
        return render_template('signup.html')
    else: 
        # request for POST form information 
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        cmd = 'register' + ' ' + name + ' ' + password + ' ' + email + ' ' + phone
        print(cmd) 
        app.pl.write(cmd) 
        return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run() 
