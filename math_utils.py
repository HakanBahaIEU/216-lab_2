def add(x,y):
    x = int(x)
    y = int(y)
    return x+y

def substract(x,y):
    x = int(x)
    y = int(y)
    return x - y

def multiply(x,y):
    x = int(x)
    y = int(y)
    return x*y

def divide(x,y):
    x = int(x)
    y = int(y)
    if(y == 0):
        print("Y cannot be zero")
        return 0
    return x/y
    
def power (x,y):
    x = int(x)
    y = int(y)
    i = 1
    if(y == 0):
        return 1
    while(i < y):
        x = x*x
        i = i + 1
    return x

def mod(x,y):
    x = int(x)
    y = int(y)
    return x%y

def MyFunc():
    print('The value of __name__ is: '+__name__)

def main():
    MyFunc()
    
if __name__=='__main__':
    main()
