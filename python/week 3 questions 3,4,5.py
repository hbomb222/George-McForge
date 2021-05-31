#question 1
#if (y==20):
#    x=9

#if (y>100):
#    x=40
#else
#    x=20
#Question 2
#num1 = int (input("please enter score 1 out of 100: "))
#num2 = int (input("please enter score 2 out of 100: "))
#num3 = int (input("please enter score 3 out of 100: "))
#ave = float((num1+num2+num3)/3)
#print(ave)
#if (ave > 90):
#    print ("congratulations")
#Question 3
#password = (input("please provide password: "))
#if (password == "Rela238#"):
#    print ("success")
#if (password != "Rela238#"):
#    print ("invalid password: ")
#Question 4
#username = input("enter username ") # ask user for username
#user_dict = {"bob":"password1234", "fred":"happypass122", "lock":"passwithlock144"} # create dictionary of username password pairs

#if (username == "bob" or username == "fred" or username == "lock"): # check if the entered username matches any of the known values
#    password = (input("enter password ")) # ask user for password
#    check_password = user_dict[username] # retrive the saved password from the dictionary for the entered username
#    if (password == check_password): # check if the entered password is the same as the saved password
#        print ("access granted") # print if username and password match
#    else: # if the passwords do not match, jump to this code
#        print ("access denied") # print if username matches but password does not match


#question 5
grade=int(input("What was your grade?: "))
if grade >= 90 and grade <= 100:
    print("you will recieve a high distinction")
elif (grade >= 80 and grade <= 89):
    print("you will recieve a distinction")
elif (grade >= 70 and grade <= 79):
    print("you will recieve a credit")
elif (grade <= 69 and grade >= 60):
    print("you will recieve a pass")