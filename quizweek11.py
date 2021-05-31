# while True:
#     try:
#         x=int(input("please enter a number: "))
#         break
#     except ValueError:
#         print("not a valid number. please enter a valid number.")
# print(x)

# #question 2

# import re
# email = ''
# while not re.match('^[A-Za-z0-9_\.]{2,32}@[A-Za-z0-9\.]{2,29}[A-Za-z]{2,3}$', email):
#     email = input('Enter email address: ')
# print('email address is valid')

# def getipaddress():
#     while True:
#         try:
#             ip = input("enter an ip address: ")
#             if "." in ip:
#                 test = ip.split(".")
#             else:
#                 raise ValueError("you need . to seperate your ip")
#             if len(test)!=4:
#                 raise ValueError("not a valid ip, incorrect amount of numbers")
#             if test[0] == "0":
#                 raise ValueError("0 isnt useable as first number")
#             for x in test:
#                 x = int(x)
#                 if x > 255 or x < 0:
#                     raise ValueError("not a valid ip, number too large")
#             print (ip)
#             return ip
#         except ValueError as err:
#             print (err)
# getipaddress()

# def get_words_from_user(min, max):
#     if min > max:
#         temp = min
#         min = max
#         max = temp
#     sentence_word_length = min - 1
#     while sentence_word_length < min or sentence_word_length > max:
#         sentence = input('Enter sentence: ')
#         sentence_list = sentence.split(' ')
#         sentence_word_length = len(sentence_list)
#     for word in range(0, len(sentence_list) - 1):
#         sentence_list[word] = sentence_list[word].lower()
#     print(sentence_list)

# get_words_from_user(5, 9)

import re
def get_password():
    password = ''
    while not re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%?&])(?!.*[Pp][Aa][Ss]{2}[Ww][Oo][Rr][Dd])[A-Za-z\d@$!%*?&]{7,}$',password):
        password = input('Enter password: ')
    check = input('Enter password again: ')
    if check == password:
        print('valid password')
    else:
        print('Passwords don\'t match')
get_password()