# from models import Users, UserMessages, LoginData
from run import app, db
from flask import jsonify, render_template, url_for, redirect, request, session

#   import register + login forms
from forms import SignupForm, LoginForm
#   import user (custom)
#   do we need?
from user import User

import database

@app.route('/success', methods=["GET", "POST"])
def success():
    #TODO fix user by using flask sessions instead?
    user = request.args['user']
    print(user)
    return jsonify(
        {
            "success" : "login worked",
            "user_logged_in" : session["username"],
        }
    )
#   welcome page
#   should reroute user to login and signup
@app.route('/home', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def welcome():
    form = LoginForm()
    print(f'session {session.get("username")}')
    # if form.login.data:
    #     print("login clicked")
    # if form.login.data:
    #     print("login lol")
    #     return redirect(url_for('success'))
    if form.signup.data:
        print("signup clicked")
        print(f"printing form data\n{form.data}\n")
        return redirect(url_for('signup'))
    if form.validate_on_submit():
        #       OLD way of looking up user email, use data.login instead
        # lookup = database.lookup_email(form.data['email'])
        # if lookup:
        #     print(f'lookup email passed')
        # else:
        #     print(f'lookup email failed')
        #     return redirect(url_for('welcome'))
        login_user_check = database.login_user(form.data['email'], form.data['password'])
        if login_user_check == False:
            print("LOGIN FAILED BRUH GG")
            return redirect((url_for('welcome')))
        #   check login credentials w/ psql database
        #   if error, display error msg
        #   if pass, session['username'] set to form username
        #   access token + refresh token?
        print(f"login clicked + success")
        user = User()
        user.email = form.data['email']
        user.password = form.data['password']
        print(f'user class details\n{user.email} {user.password}')
        session['username'] = database.get_username(database.lookup_email(form.data['email']))
        print('login successful')
        print(f"printing form data\n{form.data}")
        print(f'>>>printing user class values<<<\n')
        print(f'user.email {user.email}\nuser.password {user.password}\n')
        return redirect(url_for('hello_user'))
    #   invalid credentials
    #   do something with ui and error msg
    print(f"errors\n{form.errors}")
    return render_template(
        "home.jinja2",
        form=form
    )

@app.route('/test', methods=['POST'])
def test_page():
    return f'test_page'

#// TODO   fix signup page please
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    print(form.data)
    # print(f'errors {form.errors}')
    if form.goback.data:
        print(f"go back clicked")
        return redirect(url_for('welcome')) 
    if form.validate_on_submit():
        user_details = {
            'username' : form.data['username'],
            'email' : form.data['email'],
            'password' : form.data['password'],
            'first_name' : form.data['first_name'],
            'last_name' : form.data['last_name'],
            #   make online status to timestamp in the future
            'online_status' : True,
        }
        lookup = database.create_user(user_details)
        print(f'create user so far\n{lookup}')
        if lookup:
            print("yay u can signup")
            db.session.add(lookup)
            db.session.commit()
            print(f'added lookup')
            login_data = database.create_login_data(user_details)
            db.session.add(login_data)
            print(f'printing login data\n{login_data}')
            db.session.commit()
            print("added login data")
            #   db.session.flush() somehow made the autoincrement work
            print("session committed for signup created user")
            session['username'] = form.data['username']
            #add a account created page? you can login now
            #   redirect to login page
            return redirect(url_for('hello_user'))
        else:
            print("fail cannot signup")
            return redirect(url_for('signup'))
    print(f'error found! {form.errors}')
    return render_template(
        "signup.jinja2",
        form=form,
        # template="form-template"
    )

#   login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login page'

#   logout page
@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.pop('username', None)
    return render_template(
        "logout.jinja2",
    )

#   see all users?
@app.route('/users')
def users():
    return jsonify(
        {
            "users" : "blank"
        }
    )

#   profile page for other users?
# @app.route('/user/<name>')
# def hello_user(name):
@app.route('/userhome', methods=["GET", "POST"])
def hello_user():
    if 'username' not in session:
        return render_template('access_denied.jinja2')
    # return f"Hello {name}, this is your user page"
    return render_template('user_home.jinja2')

#   account + messages for user?
@app.route('/messages', methods=["GET", "POST"])
def messages():
    return render_template('user_messages.jinja2')


#   TEST AREA TO READ DB locally
#TODO   >>>>REMOVE AFTER TESTING<<<<<
@app.route('/psql', methods=['GET', 'POST'])
def psql_db():
    psql_data = {
        'users' : [],
        'login_data' : [],
        'user_msgs' : [],
    }
    user_data = database.get_all_user_data()
    login_data = database.get_all_login_data()
    user_msg_data = database.get_all_user_message_data()
    for item in user_data:
        tmp = {}
        tmp['user_id'] = item.user_id
        tmp['username'] = item.username
        tmp['first_name'] = item.first_name
        tmp['last_name'] = item.last_name
        tmp['online_status'] = item.online_status
        psql_data['users'].append(tmp)
    for stuff in login_data:
        pew = {}
        pew['user_id'] = stuff.user_id
        pew['email'] = stuff.email
        pew['password'] = stuff.password
        pew['access_token'] = stuff.access_token
        pew['refresh_token'] = stuff.refresh_token
        psql_data['login_data'].append(pew)
    for omg in user_msg_data:
        blah = {}
        blah['user_id'] = omg.user_id
        blah['message'] = omg.message
        blah['message_between'] = omg.message_between
        blah['message_date'] = omg.message_date
        psql_data['user_msgs'].append(blah)
    session["psql_data"] = psql_data
    return render_template("psql.jinja2")