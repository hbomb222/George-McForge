#question 1

# values = [66, 43, 1, 6, 2, 99, 4]

# i = 0
# while (i < len(values)): #while loop goes through each number in the list
#         if(values[i] < 10): #finds the numbers that are less than 10
#         print(values[i]) #prints the values of those less than 10
#     i+=1

#question 2

# date = input("please enter the date in he for dd/mm/yyyy: ")
# seperated = date.split("/")
# print("date",seperated[0])
# print("month",seperated[1])
# print("year",seperated[2])

#question 3

# values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]

# sum = sum(values)
# print("the sum of all the values is",sum)
# average = sum/len(values)
# print("the average is",average)
# maximum = max(values)
# print("the max number is",maximum)

#question 4

# name=input("please enter your name: ")
# fullname=name.split()
# initials=""
# for i in range(len(fullname)):
#         initials+=fullname[i] [0]
# print("fullname:",name)
# print("initials:",initials)

#question 5

# x = 0
# result = []
# while(True):
#     x = input("enter number: ")
#     if x == "x":
#         break
#     result.append(x)
# print("the value of result is",result)

#question 6

# result = 0
# mylist=input("enter a large number: ")
# i = 0
# while i < len(mylist):
#     result=result+int(mylist[i])
#     i = i + 1
# print("the large number is",mylist)
# print("the sum of the large number digits is",result)

#question 7

# mylist = []
# while(True):
#     x = input("enter numbers: ")
#     if x == "x":
#         break
#     mylist.append(x)
# count = 0
# dup = []
# for i in mylist:
#     for j in mylist:
#         if i == j:
#             count += 1
#     if count > 1:
#         dup.append(i)
#     count = 0
# print(set(dup))