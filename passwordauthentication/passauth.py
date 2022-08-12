import os
import sys
from getpass import getpass
from decouple import config

pass1= config('PASSWORD', default='')
user1= config('USERNAME', default='')
phone1= config('PHONENUMBER', default='')


print("1. LogIn or 2. Sign Up?")
choice=int(input())
if choice==1:

    username=input("Username: ")
    phoneNumber=input("Phone number:")
    password=getpass()


    c=0
    try:
        if pass1!=password:
            print("Invalid password")
            c+=1
        if user1!=username:
            print("invalid username")
            c+=1
        if phoneNumber!=phone1:
            print("Invalid number")
            c+=1
        if c==3:
            print("Welcome to the server")
    except KeyError:
        print("No such value exists in the database")

elif choice==2:
    username=input("Username: ")
    phoneNumber=input("Phone number:")
    password=getpass()

    print("Welcome to the server")

else:
    print("Invalid choice")

