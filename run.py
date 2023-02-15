#!/usr/bin/env python3.10
from Password import User, Credentials

creds = Credentials('my_username', 'my_password')

def __init__(self, username=None, password=None):
    if username is None:
        self.credentials_list = []

    else:
        self.credentials_list = [username, password]
        
def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def create_credential(username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(username, password)
    return new_credential

def get_password():
    """ Helper function to get a password from user"""
    print("Password (leave blank to generate a random pasword)...")

    password = input().strip()
    if not password:
        return None #User wants to generate a random password
    else:
        return password

def save_credential(credential):
    '''
    Function to save contact
    '''
    credential.save_credential()

def del_credential(index):
    '''
    Function to delete a credential
    '''
    print("Before deletion:", Credentials.credentials_list)

    print("After deletion:", Credentials.credentials_list[index])
    


def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()



def main():
    print("Hello Welcome to your Password Locker. What is your name?")
    
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")

    while True:  #Since True always evaluates to True, the loop will run indefinitely, until something within the loop returns or breaks.
        print("Use the short codes : cu - create a new user account, cc - create new credential, sc - save credential,  dc - display credential, del - delete credential, ex - exit")

        short_code = input().lower()
        if short_code == "cu":
            print("New User")
            print("-"*10)

            print("Username...")

            user_name = input()

            print("Password...")
            pass_word = input()

            save_user(create_user(user_name, pass_word)) #create and save new user
            print ('\n')


        elif short_code == "cc":
            print("New Credential")
            print("-" * 10)
            print("Platform")
            platform = input().strip()
            print("Username...")
            username = input().strip()
            password = get_password()
            creds.create_credential(platform, username, password)

      

        elif short_code =="dc":
            
            if display_credential():
                print("Here is a list of your credentials")
                print('\n')
                
                    # print(f"Platform: {credential.platform}")
                for credential in display_credential():
                    print(credential)
                    print('\n')
            else:
                print('\n')
                print("You don't seem to have any credential saved yet")
                    
                print('\n')
            
        elif short_code == "del":
            print("Delete credential")
            print("-" * 10)
            print("Index")
            index = int(input())
            creds.delete_credential(index)
            print('\n')

        elif short_code == 'ex':
            print("Bye.....")
            break
        else:
            print("I didn't really get that. Please use the short codes")


if __name__ == '__main__':

    main()