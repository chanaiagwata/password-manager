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
    
    def save_user(self):
        '''
        save_user method saves user object to user list
        '''
        User.user_list.append(self)

class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list  = [] #empty credential list

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def save_credential(self):
        '''
        save_credential saves credential to credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credential(self):
        '''
        delete_credential method deletes from credential list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the contact list
        '''
        return cls.credentials_list
        

