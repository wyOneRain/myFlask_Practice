from flask import Flask, session, redirect, url_for, request,render_template,escape,flash
from exts import validate
from Models import Users
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# db.init_app(app)

@app.route('/')
def index():
    # return render_template('base.html')
    if 'username' in session:
        return render_template('base.html')
    return render_template('base.html',title='OneRain Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(request.form)
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username=request.form.get('username')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        msg=validate(username,password1,password2)
        flash(msg)
        if '成功' in msg:
            Users().insert_user(username,password1)
        return redirect(url_for('login'))
    else:
        return render_template('register.html',page_name='Register')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True,threaded=True)

