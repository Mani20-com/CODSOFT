def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "zero division error"
    return x/y
while True:
    print("\n-- calculator menu ---")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    choice=input("choose an option(1-5): ")
    if choice=='5':
        print("Exiting calculator")
        break
    n1=float(input("enter first num: "))
    n2=float(input("enter second num: "))
    if choice=='1':
        print("result:", add(n1,n2))
    elif choice=='2':
        print("result:", subtract(n1,n2))
    elif choice=='3':
        print("result:", multiply(n1,n2))
    elif choice=='4':
        print("result:", divide(n1,n2))
    else:
        print("invalid input")    

