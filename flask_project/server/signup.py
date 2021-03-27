class Signup():
    def __init__(self):
        self._first_name = None
        self._last_name = None
        self._username = None
        self._email = None
        self._password = None
    
    @property
    def first_name(self):
        """ Get the first name """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """ Set the first name """
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        """ Delete the first name"""
        del self._first_name

    @property
    def last_name(self):
        """ Get the first name """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ Set the first name """
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        """ Delete the first name"""
        del self._last_name

    @property
    def username(self):
        """ Get the first name """
        return self._username

    @username.setter
    def username(self, value):
        """ Set the first name """
        self._username = value

    @username.deleter
    def username(self):
        """ Delete the first name"""
        del self._username
        
    @property
    def email(self):
        """ Get the first name """
        return self._email

    @email.setter
    def email(self, value):
        """ Set the first name """
        self._email = value

    @email.deleter
    def email(self):
        """ Delete the first name"""
        del self._email

    @property
    def password(self):
        """ Get the first name """
        return self._password

    @password.setter
    def password(self, value):
        """ Set the first name """
        self._password = value

    @password.deleter
    def password(self):
        """ Delete the first name"""
        del self._password
    
