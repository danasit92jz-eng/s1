instagram_account =  {}
while True:
    username = input("enter your username")
    password= input("enter your passord")
    if username in instagram_account:
        print("this account already exists try another username")
    else:
        instagram_account[username] = password
        print("your account has been created successfully")
        
