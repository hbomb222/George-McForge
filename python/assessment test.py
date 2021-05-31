name = (0)

surname = (0)

year = (0)
student = ("103549069")
studentdidgit=int(student[-3])#my 3rd last didget of my student id
while True:
    name = input("please enter your first name: ").lower()#enter your name will be converted into lowercase
    if name == "":
        break
    surname = input("please enter your surname: ").lower()#enter a surname will be converted into lowercase

    year = int (input ("please enter your age: "))#enter an age

    print((2021 - year + studentdidgit))#prints your birth year
    birthyear = 2021 - year + studentdidgit#stores the birth year as a string
    print(name[0]+ surname)

    username = name[0] + surname + (str(birthyear))#adds all the username details together
    print(username + "@Huawow.io")
    email = username + "@Huawow.io"

    password = name + surname[0] +"_"+ (str(birthyear))#adds all the password details together
    print(password)
    print(email +"|"+ password)