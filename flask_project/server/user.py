class User():
    def __init__(self):
        self.email = None
        self.password = None

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