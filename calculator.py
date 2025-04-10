import math_utils
math_utils.MyFunc()

calc = {1:"add",2:"substract",3:"multiply",
        4:"divide",5:"power",6:"mod"}
x = input("Please enter an integer: ")
y = input("Please enter another integer: ")

print(calc)

z = input("please enter the function name: ")

if(z == calc[1]):
    print(math_utils.add(x,y))
elif(z == calc[2]):
    print(math_utils.substract(x,y))
elif(z == calc[3]):
    print(math_utils.multiply(x,y))
elif(z == calc[4]):
    print(math_utils.divide(x,y))
elif(z == calc[5]):
    print(math_utils.power(x,y))
elif(z == calc[6]):
    print(math_utils.mod(x,y))
else:
    print("function name you entered is not included")

