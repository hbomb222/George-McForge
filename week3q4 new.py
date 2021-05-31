username = input("enter username ") # ask user for username
user_dict = {"bob":"password1234", "fred":"happypass122", "lock":"passwithlock144"} # create dictionary of username password pairs

if (username == "bob" or username == "fred" or username == "lock"): # check if the entered username matches any of the known values
    password = (input("enter password ")) # ask user for password
    check_password = user_dict[username] # retrive the saved password from the dictionary for the entered username
    if (password == check_password): # check if the entered password is the same as the saved password
        print ("access granted") # print if username and password match
    else: # if the passwords do not match, jump to this code
        print ("access denied") # print if username matches but password does not match