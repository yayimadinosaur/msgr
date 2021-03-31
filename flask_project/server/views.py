from models import Users, UserMessages, LoginData
from run import app
from flask import jsonify, render_template, url_for, redirect, request, session

#   import register + login forms
from forms import SignupForm, LoginForm
#   import user (custom)
from user import User

@app.route('/success/', methods=["GET", "POST"])
def success():
    #TODO fix user by using flask sessions instead?
    user = request.args['user']
    print(user)
    return jsonify(
        {
            "success" : "login worked",
            "email" : session['email'],
            "password" : session['password'],
        }
    )
#   welcome page
#   should reroute user to login and signup
@app.route('/home/')
@app.route('/', methods=["GET", "POST"])
def welcome():
    form = LoginForm()
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
        print(f"login clicked + success")
        user = User()
        user.email = form.data['email']
        user.password = form.data['password']
        session['email'] = form.data['email']
        session['password'] = form.data['password']
        print(f"sesssion email is {session['email']}")
        print('login successful')
        print(f"printing form data\n{form.data}")
        print(f'printing user class values\n')
        print(f'user.email {user.email}\nuser.password {user.password}\n')
        return redirect(url_for('success', user=user))
    print(f"errors\n{form.errors}")
    return render_template(
        "home.jinja2",
        form=form
    )

@app.route('/test/', methods=['POST'])
def test_page():
    return f'test_page'

#// TODO   fix signup page please
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    print(form.data)
    # print(f'errors {form.errors}')
    if form.goback.data:
        print(f"go back clicked")
        return redirect(url_for('welcome'))
    if form.validate_on_submit():
        session['first_name'] = form.data['first_name']
        session['last_name'] = form.data['last_name']
        session['username'] = form.data['username']
        session['email'] = form.data['email']
        session['password'] = form.data['password']
        print("signup successful!\n")
        #TODO check form data w/ psql db
        #TODO if data valid, direct to hello_user, if not redirect to fail?
        return redirect(url_for("hello_user", name=form.data["username"]))
    print(f'error found! {form.errors}')
    return render_template(
        "signup.jinja2",
        form=form,
        # template="form-template"
    )

#   login page
@app.route('/login/', methods=['GET', 'POST'])
def login():
    return 'login page'

#   logout page
@app.route('/logout/')
def logout():
    return 'logout page'

#   see all users?
@app.route('/users/')
def users():
    return jsonify(
        {
            "users" : "blank"
        }
    )

#   profile page for other users?
@app.route('/user/<name>')
def hello_user(name):
    # return f"Hello {name}, this is your user page"
    return render_template('user_home.jinja2')

#   account + messages for user?
@app.route('/messages/')
def messages():
    return f'welcome to the messages page'


#   TEST AREA TO READ DB locally
#TODO   >>>>REMOVE AFTER TESTING<<<<<
@app.route('/psql/', methods=['GET', 'POST'])
def psql_db():
    return url_for('psql_db')