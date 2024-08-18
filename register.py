from database import*
from random import *
def SignUp():
    username = input("Create Username")
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print("User Already Exists")
        SignUp()
     
    else:
        print("Username Available Please Proceed")
        password = input("Enter Your Password")
        name = input("Enter Your Name")
        age = input("Enter Your Age")
        city = input("Enter Your City")
        while True:
            account_number=int(random.randint(10000000, 99999999))
            temp = db_query(f"SELECT account_number FROM customers WHERE account_number = '{account_number}';")
            if temp:
                continue
            else:
                print("Your Account Number",account_number)
                break
            