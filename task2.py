correct_username = "Sherlock"
correct_password = "6666"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("Login Successful")

else:
    print("Invalid Credentials")