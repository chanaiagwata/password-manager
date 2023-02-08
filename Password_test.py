import unittest
from Password import User, Credentials

class TestUser(unittest.TestCase):
    '''
    Testclass that defines test cases for the User class behaviors
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("chanai", "268231")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"chanai")
        self.assertEqual(self.new_user.password,"268231")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into user list
        '''
        self.new_user.save_user() #save the new user
        self.assertEqual(len(User.user_list), 1)

class TestCredentials(unittest.TestCase):
    '''
    Testcase that defines test cases for the Credentials behaviors
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credential = Credentials("chanai", "268231")

    def test_init(self):
        '''
        test_init test case to test if the object is initiatized properly
        '''

        self.assertEqual(self.new_credential.username, "chanai")
        self.assertEqual(self.new_credential.password, "268231")
    
    def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into user list
        '''
        self.new_credential.save_credentia() #save the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    
if __name__ == '__main__':
    unittest.main()