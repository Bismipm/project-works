def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1 * n2)
def div(n1,n2):
    print(n1 / n2)
while True:
    option=int(input("select the choice\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.stop"))
    if option==5:
        break
    elif option==1 or option==2 or option==3 or option==4:
        num1=float(input("enter number 1 :"))
        num2=float(input("enter number 2 :"))
        if option==1:
            add(num1,num2)
        elif option==2:
            sub(num1,num2)
        elif option==3:
            mul(num1,num2)
        elif option==4:
            div(num1,num2)
    else:
        print("invalid")

def sum(a,b):
    print(a*2+b*2)
def squ (a,b):
    print((a+b)**2)
def diff(a,b):
    print((a*2+b2))-((a+b)*2)
while true:
    option=int(input("select the choice\n1.sum of square\n2.square of sum\n3.difference of sum of square and square of sum\n4.stop"))
    if option==4:
        break
    elif option==1 or option==2 or option==3:
        a=float(input("enter num.1:"))
        b=float(input("enter num.2:"))
        if option==1:
            sum(a,b)
        elif option==2:
            squ(a,b)
        elif option==3:
            diff(a,b)
        else:
            print("invalid")
def add():
    return  (20+10)
add()
print(add())