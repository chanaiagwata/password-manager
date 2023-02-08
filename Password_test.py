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

    def tearDown(self):
        '''
        teardown method that does clean up after each test case has run
        '''
        User.user_list = []

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

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users method to check if we can save multiple user object
        '''
        self.new_user.save_user()
        test_user = User("ioctane", "12334") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)    

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
    
    def tearDown(self):
        '''
        teardown method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []

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
        self.new_credential.save_credential() #save the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_users method to check if we can save multiple user object
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("ioctane", "12334") #new user
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credential(self):
        '''
        test_delete_credential method to test if we can remove a credential from credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("Test", "12345") # save new credential object
        test_credential.save_credential()

        self.new_credential.delete_credential() # Deleting a credential object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_view_credential(self):
        '''
        view_credential method returns list of all saved credentials
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)
        


if __name__ == '__main__':
    unittest.main()