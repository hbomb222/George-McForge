# outfile=open("maths.txt", "w")
# outfile=open("maths.txt", "a")
# x=input("please enter a number: ")

# y=input("please enter another number: ")
# outfile=open("maths.txt", "w")
# sum= int(x) + int (y)

# print("the sum is: ", sum)
# outfile.write(str(sum))
# outfile.close()
# outfile=open("maths.txt", "r")
# print(outfile.read())


# num1 = int(input("enter the first number: "))
# num2 = int(input("enter the second number: "))
# total = num1+num2
# outfile = open("maths.txt","w")
# outfile.write(str(total))
# outfile.close()

# name=(0)

# outfile=open("people.txt", "a")
# while True:
#     name = input("please enter your first name: ")
#     outfile.write(str(name) + '\n')
#     if name == "":
#         break
# outfile.close()


# outfile=open("names.txt","r")
# lines=outfile.readlines()
# outfile.close()
# outfile=open("names-formatted","w")
# for line in lines:
#     outfile.write(line.title())
# outfile.close()

# for num in range(1, 10 + 1):
#     temp = 1
#     for i in range(1, num + 1):
#         temp = i * temp
#     print(str(num) + "! = " + str(temp))


infile=open("logins.txt","r")
userpassword=infile.read()
user=userpassword.split(":")[0]
password=userpassword.split(":")[1]
userinput=input("please enter username: ")

if user == userinput:
    passwordinput=input("please enter password: ")
    if password == passwordinput:
        print("access granted")
    else:
        print("incorrect password")
else:
    print("user unknown")
