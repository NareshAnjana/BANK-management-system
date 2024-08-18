from register import *
print("welcome to naresh banking project")
while True:
    try:
        register = int(input("1. Signup\n"
                             "2. SignIN"))
        if register == 1 or register == 2:
            if register == 1:
             SignUp()
        else:
            print("Please Enter Valid Input From Options")
    except ValueError:
        print("Invalid Input Try Again with Numbers")