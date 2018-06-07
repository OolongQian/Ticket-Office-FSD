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



@app.route('/signin', methods=['GET', 'POST'])
def signin(): 
    return render_template('index.html')

if __name__ == "__main__": 
    app.run() 
