#program 1
instagram_account =  {}
while True:
    username = input("enter your username")
    password= input("enter your passord")
    if username in instagram_account:
        print("this account already exists try another username")
    else:
        instagram_account[username] = password
        print("your account has been created successfully")
        #program 2
        number =[10,15,22,33,40,51]
        result  = ["even" if number %2==0 else"odd" for number in number]
        print(result)

