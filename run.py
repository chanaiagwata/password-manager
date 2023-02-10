#!/usr/bin/env python3.10
from Password import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user


def create_credential(username, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(username, password)
    return new_credential

def save_credential(credential):
    '''
    Function to save contact
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

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
        print("Use the short codes : cu - create a new user account, cc - create new credential, sc - save credential,  dc - display credential, del - delete credential")
