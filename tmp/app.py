import flask
from passlib.hash import sha256_crypt

from db_handler import firebase_handler as fb_handle
import actors

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/boards')
def boards():
    return flask.render_template('boards.html')

@app.route('/arithmetic_board')
def arithmetic_board():
    return flask.render_template('arith.html')

def __login_helper(usertype, username, password_candidate):
    fb_handler = fb_handle.FirebaseEntryPoint.create()

    if usertype == 'student':
        fb_url = actors.Student.DB_URL
    elif usertype == 'teacher':
        fb_url = actors.Teacher.DB_URL
    elif usertype == 'parent':
        fb_url = actors.Parent.DB_URL
    else:
        fb_url = actors.Admin.DB_URL

    data = fb_handler.retrieve_data(fb_url, username)
    if data == None:
        flask.flash('User Not found!', 'danger')
        return None
    password = fb_handler.retrieve_password_from_fb_data(data)
    return password


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        usertype = flask.request.form['optionRadios']
        username = flask.request.form['email']
        password_candidate = flask.request.form['pwd']

        password = __login_helper(usertype, username, password_candidate)
        if password != None:
            if sha256_crypt.verify(password_candidate, password):
                flask.session['logged_in'] = True
                flask.session['username'] = username
                flask.session['usertype'] = usertype
                return flask.redirect(flask.url_for('boards')) # TODO: Discuss
            else:
                flask.flash('Incorrect login!', 'danger')

    return flask.render_template('login.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if flask.request.method == 'POST':
        username = flask.request.form['email']
        password_candidate = flask.request.form['pwd']

        password = __login_helper('admin', username, password_candidate)
        if password != None:
            if sha256_crypt.verify(password_candidate, password):
                flask.session['logged_in'] = True
                flask.session['username'] = username
                flask.session['usertype'] = 'admin'
                return flask.redirect(flask.url_for('boards')) # TODO: Discuss
            else:
                flask.flash('Incorrect login!', 'danger')

    return flask.render_template('login.html', login_type='admin')

@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if flask.session['logged_in'] and flask.session['usertype'] == 'admin':
        return flask.render_template('create_user.html')
    else:
        return flask.redirect(flask.url_for('login'))

if __name__ == '__main__':
    app.secret_key = "mathub-ser515"
    app.run(host='0.0.0.0', port=3000, debug=True)