#!/usr/bin/env python3.10
from Password import User, Credentials

def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

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