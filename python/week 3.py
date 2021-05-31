#if (y==20):
#    x=9

#if (y>100):
#    x=40
#else
#    x=20

num1 = int (input("please enter score 1 out of 100: "))
num2 = int (input("please enter score 2 out of 100: "))
num3 = int (input("please enter score 3 out of 100: "))
ave = float((num1+num2+num3)/3)
print(ave)
if (ave > 90):
    print ("congratulations")