import math
x = 5
def factorial(x):
    a = 1
    for r in range(1,x+1):
        a = a * r
    return a

def sine_x(x,n):
    fnl = 0
    for var1 in range(n):
        eq = lambda var3,var4 : math.pow(-1,var4) * math.pow(var3,2*var4 +1) / factorial(2*var4 + 1)
        fnl += eq(x,var1)
    return fnl/180

def Hn():
        #x decreases by 1 until x is 1 
        #then returns 1 then sums every 1/x until reaches actual x 
        global x
        if(x == 1): return 1
        x = Hn(x-1) + 1/x



var1 = int(input("Please enter an integer"))
var2 = int(input("please enter an integer"))
print(sine_x(var1,var2))
