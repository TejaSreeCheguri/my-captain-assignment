

#CALCULATOR

print("ENTER 1 for Addition \n      2 for Subtraction \n      3 for  Multiplication \n      4 for division")
b = eval(input("enter first number: "))                     #eval() function converts the input which is in string format to integer
c = eval(input("enter second number: "))
a = eval(input(" Enter your choice: "))

if a==1:
    sum = b+c
    print("sum is: ",sum)
elif a==2:
    dif = b-c
    print("difference is: ",dif)
elif a==3:
    product = b*c
    print("product is: ",product)
elif a==4:
    div = b//c
    print("quotient is: ",div)
else:
    print("invalid")



