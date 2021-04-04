class User():
    def __init__(self):
        self.email = None
        self.password = None

    @property
    def email(self):
        """ Get the email"""
        return self._email

    @email.setter
    def email(self, value):
        """ Set the email """
        self._email = value

    @email.deleter
    def email(self):
        """ Delete the email"""
        del self._email
    
    @property
    def password(self):
        """ Get the password """
        return self._password

    @password.setter
    def password(self, value):
        """ Set the password """
        self._password = value

    @password.deleter
    def password(self):
        """ Delete the password"""
        del self._password