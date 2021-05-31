# #week 1 was print "hello world"
# #week 2 flowcharts and algorithms
# #week 3 selection (if conditions elif)
# # i=0
# # while(i<26):
# #     print(i)
# #     i=i+1

# # for x in range(26):
# #     print(x)

# sum=0
# for x in range(10,51):
#     sum=sum+x
#     print(sum)

# # import random
# # n = random.randint(1, 99)
# # guess = int(input("Enter an integer from 1 - 10: ""))
guesses = 7
counter = 0
import random
n = random.randint(1, 25)
while guesses > counter:
    guess = int(input("enter a number between 1 and 25: "))
    print ("number of guesses left " + str(guesses-counter))
    if guess > n:
        print ("nope, its less than that")   
    elif guess < n:
        print ("nope, its higher than that")
    elif guess == n:
        print ("well done")
        break
    counter = counter + 1
