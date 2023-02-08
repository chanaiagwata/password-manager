class User:
    """
    Class that generates new instances of users
    """
    user_list = [] #Empty user list

    def __init__(self, username, password):
        """
        __init__method that helps define properties of our objects
        Args:
            username: new user username
            password: new user password
        """
        self.username = username
        self.password = password


class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list  = [] #empty credential list

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

