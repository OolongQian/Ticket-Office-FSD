from flask import Flask
from flask import request, render_template, abort, redirect, url_for, session
from subprocess import Popen, PIPE, STDOUT

app = Flask(__name__)

# set it to a random string
app.secret_key = 'any random string that are long enough'

# set this to path/to/your/database/backend/program
database_exec_path = "/Users/qiansucheng/Desktop/frontEnd/demo/DS2018-frontend-demo-master/train"

def app_init():
    app.proc = Popen([database_exec_path], stdin=PIPE, stdout=PIPE)

app_init()

def db_write(cmd):
    app.proc.stdin.write((cmd + '\n').encode())
    app.proc.stdin.flush()

def db_readline():
    return app.proc.stdout.readline().decode().strip('\n')

@app.route('/', methods=['GET'])
def home():
    if 'home_success_info' in session and session['home_success_info'] != '':
        success_info = session['home_success_info']
        session.pop('home_success_info', None)
    else:
        success_info = None
    if 'home_err_info' in session and session['home_err_info'] != '':
        err_info = session['home_err_info']
        session.pop('home_err_info', None)
    else:
        err_info = None
    if 'user_id' in session and 'user_name' in session and session['user_name'] != '':
        user_name = session['user_name']
    else:
        user_name = None
    return render_template('index.html', success_info=success_info, err_info=err_info, user_name=user_name)

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']
        db_write(' '.join(['login', userid, password]))
        reply = db_readline()
        print(reply)
        if reply == '0' or reply == 'Wrong Command':
            return render_template('signin.html', err_info='Login failed for some reason.')
        else:
            session['home_success_info'] = 'Logged in successfully! Now you can play around.'
            session['user_id'] = userid
            db_write(' '.join(['query_profile', userid]))
            reply = db_readline()
            if reply == '0':
                session['home_err_info'] = 'Login failed! User does not exist.'
            else:
                session['user_name'] = reply.split(' ')[0]
            return redirect(url_for('home'))
    else:
        return render_template('signin.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            return render_template('signup.html', err_info='The two passwords you typed do not match.')
        db_write(' '.join(['register', name, password, email, phone]))
        reply = db_readline()
        if reply == '-1':
            return render_template('signup.html', err_info='Registration failed for some reason.')
        else:
            userid = int(reply)
            session['home_success_info'] = 'Registration successful! Your account ID is %s.' % (userid)
            return redirect(url_for('home'))
    else:
        return render_template('signup.html')

@app.route('/signout', methods=['GET'])
def signout():
    if 'user_id' in session:
        session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET'])
def profile():
    if 'user_id' not in session:
        session['home_err_info'] = 'Error! You have not signed in.'
        return redirect(url_for('home'))
    user_id = session['user_id']
    db_write(' '.join(['query_profile', user_id]))
    reply = db_readline()
    if reply == '0':
        session['home_err_info'] = 'Error! User does not exist.'
        return redirect(url_for('home'))
    else:
        vec = reply.split(' ')
        user_name = vec[0]
        user_email = vec[1]
        user_phone = vec[2]
        user_priv = vec[3]
    return render_template('profile.html', user_id=user_id, user_name=user_name, user_email=user_email, user_phone=user_phone, user_priv=user_priv)

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    if 'user_id' not in session:
        session['home_err_info'] = 'Error! You have not signed in.'
        return redirect(url_for('home'))
    if request.method == 'POST':
        user_id = session['user_id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        repassword = request.form['repassword']
        if password != repassword:
            return render_template('settings.html', err_info='The two passwords you typed do not match.')
        db_write(' '.join(['modify_profile', user_id, name, password, email, phone]))
        reply = db_readline()
        if reply == '0':
            return render_template('settings.html', err_info='Modification failed for some reason.')
        else:
            session['home_success_info'] = 'Profile modified successfully!'
            return redirect(url_for('home'))
    else:
        user_name = session['user_name']
        return render_template('settings.html', user_name=user_name)

if __name__ == '__main__':
    app.run()
