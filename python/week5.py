
# states = ["vic","nsw","sa","wa","tas","qld"]
# # print(states)
# # states.append("act")
# # print(states)
# # states.remove("nsw")
# # print(states)
# states.pop(3)
# print(states)

"""
words = "hello,world,i,am,here"
print (words)
print(words.split(",")) #default split is spaces
"""
"""
string1 = "hello "
string2 = "world"
string3 = string1 + " " + string2
print (string3)
"""
"""
numbers = list(range(3))
print (numbers)

numbers=[1,2,3,4,5]

print(numbers[0]+numbers[3])
"""
"""
numbers = [10 ] * 5
print(numbers)
"""
"""
numbers= [1,2,3,4,5]
print(numbers [-3])
"""
"""
numbers= [1,2,3,4,5]
numbers[4]

print(len(numbers))
"""
"""
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
"""
""" #will need this line for the assessment
number_list = [1,2,3,6,8,9,2,5.2]
i = 0
while i < len(number_list):
    print (number_list[i])
    i = i + 1
"""
number_list = [1,2,3,5,6,2,5.2,10.5,12,15.9]
total = 0
i = 0
while i <len(number_list):
    total = total + number_list[i]
    i = i + 1
avg = total / len(number_list)
print(total)
# print ('the average is {:.2f}|%(avg)):
