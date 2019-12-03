# Author: Piyush Malhotra
# Date modified: 11/28/2019

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

@app.route('/profile')
def profile():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.STUDENT:
            return flask.render_template(
            'studprofile.html', usertype=flask.session['usertype'],
            username=flask.session['client']['username'],
            grade=flask.session['client']['grade'])
        if 'usertype' in flask.session and flask.session['usertype'] == actors.TEACHER:
            return flask.render_template(
            'teacherprofile.html', usertype=flask.session['usertype'],
            username=flask.session['client']['username'])

        if 'usertype' in flask.session and flask.session['usertype'] == actors.PARENT:
                return flask.render_template(
                'parentprofile.html', usertype=flask.session['usertype'],
                username=flask.session['client']['username'])
    return flask.redirect(flask.url_for('login'))

@app.route('/create_assignment', methods = ['POST', 'GET'])
def create_assignment():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.TEACHER:
            if flask.request.method == 'POST':
                data = flask.request.get_json()
                print('HERE', data)
                fb_handler = fb_handle.FirebaseEntryPoint.create()
                fb_handler.add_assignment('/Assignment', data)
                return flask.jsonify({'result': 'success'})
            return flask.render_template('create_assignment.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/view_assignment')
def view_assignment():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.TEACHER:
            return flask.render_template('teacher_assignment.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/student_view_assgn')
def student_view_assgn():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.STUDENT:
            return flask.render_template('studassignment.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/charts')
def charts():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        return flask.render_template('charts.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/cms')
def cms():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if 'usertype' in flask.session and flask.session['usertype'] == actors.ADMIN:
            return flask.render_template('cms.html')
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
            flask.session['client']['login_count'] += 1
            if data['login_count'] == 1:
                return flask.redirect(flask.url_for('reset_password'))
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
            data['grade'] = 12

            __login_count_incrementer(actors.ADMIN, username)

            flask.session['client'] = data
            flask.session['client']['login_count'] += 1
            if data['login_count'] == 1:
                return flask.redirect(flask.url_for('reset_password'))
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
                data['grades'] = flask.request.form.getlist('grades')
                print('HERE!!')
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
    exp = exp.replace(' ', '')
    exp = exp.replace('import', 'import ')
    try:
        exec(exp)
        return flask.jsonify({'results': results, 'success': True})
    except Exception as e:
        return flask.jsonify({'results': results, 'success': False})

@app.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        if flask.request.method == 'POST':
            fb_url = __get_url_from_usetype(flask.session['usertype'])
            fb_handler = fb_handle.FirebaseEntryPoint.create()

            client_data = flask.session['client']
            password = flask.request.form['password']
            confirm_password = flask.request.form['confirm-password']
            if password != confirm_password:
                flask.flash("Passwords doesn't match", 'danger')
                return flask.render_template('reset_password.html')
            password = sha256_crypt.encrypt(flask.request.form['password'])
            client_data['password'] = password
            flask.session['client'] = client_data

            fb_handler.update_data(fb_url, client_data)
            return flask.redirect(flask.url_for('boards'))
        else:
            return flask.render_template('reset_password.html')
    return flask.redirect(flask.url_for('login'))

@app.route('/assignments')
def assignments():
    if 'logged_in' in flask.session and flask.session['logged_in']:
        fb_handler = fb_handle.FirebaseEntryPoint.create()
        assigns = fb_handler.retrieve_assignments_for_grade(
            '/Assignment', flask.session['client']['grade'])
        flask.session['client']['assignments'] = assigns
        return flask.render_template('assignments.html')
    return flask.redirect(flask.url_for('login'))
    
if __name__ == '__main__':
    app.secret_key = "mathub-ser515"
    app.run(host='0.0.0.0', port=3000, debug=True)
