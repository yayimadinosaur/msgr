# from run import cursor
# import credentials    see if class is actually needed

from models import Users, UserMessages, LoginData

#   get all data from users in db
def get_all_user_data():
    user_data = Users.query.all()
    return user_data

#   get all data from login_data in db
def get_all_login_data():
    login_data = LoginData.query.all()
    return login_data

#   get all user_messages in db
def get_all_user_message_data():
    user_message_data = UserMessages.query.all()
    return user_message_data

#   signup query on database

#   lookup user in the database to see if the account exists
def lookup_username(username):
    username_check = Users.query.filter(
        Users.username == username
    ).first()
    if username_check:
        print(f'username {username} found in db')
        return True
    else:
        print(f'username {username} not found')
        return False
    #   if user exists
    #       return success
    #   if does not exist
    #       return error - msg : invalid user / user does not exist

#   get username user_id
def get_user_id(username):
    selected_row = Users.query.filter_by(username = username).first()
    return selected_row.user_id

#   get username from user_id
def get_username(user_id):
    selected_row = Users.query.filter_by(user_id=user_id).first()
    return selected_row.username

#   lookup email in the database to see if the acc exists
#   returns user_id if it does
def lookup_email(email):
    user_check = LoginData.query.filter(
        LoginData.email == email
    ).first()
    if user_check:
        print(f'user_check {user_check}')
        print(f'user email found in db [{email}]')
        database_query = LoginData.query.filter_by(email=email).first()
        print(f'>>>\nuser_id {database_query.user_id}<<<\n')
        return database_query.user_id
    else:
        print(f'user email [{email}] not found [{user_check}]')
        return False
    #   if email exists
    #       return success
    #   if does not exist
    #       return error - msg : invalid user / user does not exist

#   checks password in db
def check_password(password, user_id):
    verify_password = LoginData.query.filter(
        LoginData.password == password
    ).first()
    if verify_password:
        print(f'password [{password}] verified')
        return True
    else:
        print(f'password [{password}] is incorrect')
        return False

#   create user on signup
def create_user(user_details):
    check_email = lookup_email(user_details['email'])
    if check_email:
        print("email is already registered")
        return False
    check_username = lookup_username(user_details['username'])
    if check_username:
        print("username is already taken")
        return False
    print(f'email {user_details["email"]} + username {user_details["username"]} available')
    #   insert user_details into psql db
    new_user_details = Users(
        #   somehow db.session.flush() made the user_id autoincrement
        user_id = None,
        username = user_details["username"],
        first_name = user_details["first_name"],
        last_name = user_details["last_name"],
        online_status = user_details["online_status"],
    )
    return new_user_details
    # new_user_credentials = LoginData(

    # )
    # new_user = (new_user_details, new_user_credentials)
    # return new_user

#   create login data for user
def create_login_data(user_details):
    user_login_data = LoginData(
        user_id = get_user_id(user_details["username"]),
        email = user_details["email"],
        password = user_details["password"],
        access_token = 123456,
        refresh_token = 123455,
    )
    return user_login_data

    #   check if user exists
    # lookup_user(username, password)
    #       if not create
    #           save user details in database
    #           check against database if user was successfully created
    #               if fails, return error msg - reason
    #           return user created msg
    #       if exists, return error msg
    #           i.e. "already created / taken"

#   login query on database
def login_user(email, password):
    user_id = lookup_email(email)
    print(f'login_user user_id [{user_id}]')
    if user_id:
        print(f'email [{email}] found in db')
        if check_password(password, user_id):
            print(f'password {password} found in db')
            print(f'time to login!!!')
            return True
        else:
            print(f'password {password} does not match in db')
            return False
    else:
        print(f'email {email} not found do something else')
        return False
    #   check if user exists
    #   lookup_user(email)
    #       if not, return error msg - invalid user credentials
    #   if user does exist
    #       check credentials from form
    #           if success, redirect to user home page
    #           if fail, return error msg - invalid user credentials