from flask import Flask
from utility.pipeline import PipeLine
from flask import request, render_template, abort, redirect, url_for, session

# set backend executable path
database_exec_path = './backend/prog'

app = Flask(__name__)
app.pl = PipeLine(database_exec_path)

@app.route('/', methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST': 
        username = request.form['firstname']
        username = username + 'Haha'
        return render_template('_test.html', username=username)
    return render_template('_test.html', username=None)

if __name__ == "__main__": 
    app.run(debug=True) 
