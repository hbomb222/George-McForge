#name = input ("please enter name ")
#if (name == "frank"):
#    print ("hello frank")
#    name = input ("please enter name ")
#if (name == "george"):
#    print ("hello george")

#year = int (input ("please enter your birth year "))
#age = (2021 - year)
#print ("you are ",age," years old")
#if (age < 18):
#    print ("Go away. Child")
#if (age >= 18):
#    print ("come in for a drink")

#username = (input("enter username "))
#if (username == "bob"):
#    password = (input("enter password "))
#if (password == "pass1234"):
#    print ("access granted")

#username = (input("enter username "))
#if (username == "frank"):
#    password = (input("enter password "))
#if (password != "pass1234"):
#    print ("access denied")

username = input("enter username ") # ask user for username
user_dict = {"bob":"password1234", "fred":"happypass122", "lock":"passwithlock144"} # create dictionary of username password pairs

if (username == "bob" or username == "fred" or username == "lock"): # check if the entered username matches any of the known values
    password = (input("enter password ")) # ask user for password
    check_password = user_dict[username] # retrive the saved password from the dictionary for the entered username
    if (password == check_password): # check if the entered password is the same as the saved password
        print ("access granted") # print if username and password match
    else: # if the passwords do not match, jump to this code
        print ("access denied") # print if username matches but password does not match