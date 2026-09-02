def user_auth():
    password = input("Enter the password: ") 

    login_password = input("Enter the login password: ")

    if password == login_password:
        print("Access granted.")
    else:
        print("Access denied. Incorrect password.")

user_auth()

