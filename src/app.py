import flask
from passlib.hash import sha256_crypt

from db_handler import firebase_handler as fb_handle
from auth import login_helper
import actors

app = flask.Flask(__name__)

def __get_url_from_usetype(usertype):
    usertype_2_dburl = {
        actors.STUDENT: actors.Student.DB_URL,
        actors.ADMIN: actors.Admin.DB_URL,
        actors.TEACHER: actors.Teacher.DB_URL,
        actors.PARENT: actors.Parent.DB_URL
    }
    return usertype_2_dburl[usertype]

def __get_user_data(username, usertype):
    fb_handler = fb_handle.FirebaseEntryPoint.create()
    data = fb_handler.retrieve_data(
        __get_url_from_usetype(usertype), username)

    return data

def __login_helper(usertype, username, password_candidate):
    fb_handler = fb_handle.FirebaseEntryPoint.create()
    fb_url = __get_url_from_usetype(usertype)

    return login_helper.verify(fb_url, username, password_candidate)

def __login_count_incrementer(usertype, username):
    fb_handler = fb_handle.FirebaseEntryPoint.create()
    fb_url = __get_url_from_usetype(usertype)

    fb_handler.increment_login_count(fb_url, username)

@app.route('/')
def index():
    fb_handle.FirebaseEntryPoint.create()
    return flask.render_template('index.html')

@app.route('/boards')
def boards():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template('boards.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/arithmetic_board')
def arithmetic_board():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template('arith.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/game-board')
def game_board():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template(
            'arith.html', usertype=flask.session['usertype'],
            username=flask.session['client']['username'],
            grade=flask.session['client']['grade'])
    return flask.redirect(flask.url_for('login'))

@app.route('/practice-board')
def practice_board():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template('arith.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/assignment-board')
def assignment_board():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template('arith.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.ADMIN:
            return flask.redirect(flask.url_for('create_user'))
        return flask.redirect(flask.url_for('boards'))

    if flask.request.method == 'POST':
        usertype = flask.request.form['optionRadios']
        username = flask.request.form['email'].lower()
        password_candidate = flask.request.form['pwd']

        is_verified, error_if_any = __login_helper(
            usertype, username, password_candidate)
        if is_verified:
            flask.session['logged_in'] = True
            flask.session['username'] = username
            flask.session['usertype'] = usertype

            data = __get_user_data(username, usertype)
            data['usertype'] = usertype

            __login_count_incrementer(usertype, username)

            flask.session['client'] = data
            return flask.redirect(flask.url_for('boards')) # TODO: Discuss
        else:
            flask.flash(error_if_any, 'danger')

    return flask.render_template('login.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.ADMIN:
            return flask.redirect(flask.url_for('create_user'))
        return flask.redirect(flask.url_for('boards'))

    if flask.request.method == 'POST':
        username = flask.request.form['email'].lower()
        password_candidate = flask.request.form['pwd']

        is_verified, error_if_any = __login_helper(
            actors.ADMIN, username, password_candidate)
        if is_verified:
            flask.session['logged_in'] = True
            flask.session['username'] = username
            flask.session['usertype'] = actors.ADMIN

            data = __get_user_data(username, actors.ADMIN)
            data['usertype'] = actors.ADMIN

            __login_count_incrementer(actors.ADMIN, username)

            flask.session['client'] = data
            return flask.redirect(flask.url_for('create_user')) # TODO: Discuss
        else:
            flask.flash(error_if_any, 'danger')

    return flask.render_template('login.html', login_type='admin')

@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if flask.session['logged_in'] and flask.session['usertype'] == actors.ADMIN:
        if flask.request.method == 'POST':
            username = flask.request.form['username'].lower()
            usertype = flask.request.form['usertype']
            name = flask.request.form['name']

            data = {
                'username': username,
                'name': name,
                'login_count': 0
            }

            if usertype == actors.STUDENT:
                data['grade'] = flask.request.form['grade']
                data['id'] = '{}'.format(actors.STUDENT_ID_PREFIX)
            elif usertype == actors.TEACHER:
                data['grades'] = flask.request.form['grades']
                data['id'] = '{}'.format(actors.TEACHER_ID_PREFIX)
            elif usertype == actors.PARENT:
                data['stud_id'] = flask.request.form['stud-id']
                data['id'] = '{}'.format(actors.PARENT_ID_PREFIX)
            else:
                data['id'] = '{}'.format(actors.ADMIN_ID_PREFIX)

            fb_url = __get_url_from_usetype(usertype)
            fb_handler = fb_handle.FirebaseEntryPoint.create()
            
            if data['id'] == None:
                data['id'] += str(actors.START_ID)
                fb_handler.set_id(fb_url, actors.START_ID)
            else:
                data['id'] += str(fb_handler.update_id(fb_url))

            password = login_helper.default_password_generator(username, data['id'])
            data['password'] = sha256_crypt.encrypt(password)

            actors.Admin.create_user(fb_url, data)
            
            flask.flash('User Created with ID: {}'.format(data['id']), 'success')
        return flask.render_template('create_user.html')
    else:
        return flask.redirect(flask.url_for('login'))

@app.route('/logout')
def logout():
    if 'logged_in' in flask.session:
        flask.session['logged_in'] = False

    if 'usertype' in flask.session:
        flask.session['usertype'] = None

    if 'username' in flask.session:
        flask.session['username'] = None

    if 'client' in flask.session:
        flask.session['client'] = None

    return flask.redirect(flask.url_for('login'))


@app.route('/eval', methods=['GET', 'POST'])
def eval():
    exp = flask.request.json['exp']
    results = []
    exp = exp.replace('print', 'results.append')
    try:
        exec(exp)
        return flask.jsonify({'results': results, 'success': True})
    except Exception as e:
        return flask.jsonify({'results': results, 'success': False})

if __name__ == '__main__':
    app.secret_key = "mathub-ser515"
    app.run(host='0.0.0.0', port=3000, debug=True)
