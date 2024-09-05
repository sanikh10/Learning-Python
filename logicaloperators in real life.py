username = "sanikh"
password = "123456"

enter_username = input('Enter your username: ')
enter_password = input('Enter your password: ')


# if enter_username == username and enter_password == password:
#     print("Login Successfull")
# else:
#     print("Username or password incorrect")


if enter_username != username or enter_password != password:

    print("Username or password incorrect")
else:
    print("Login Successfull")