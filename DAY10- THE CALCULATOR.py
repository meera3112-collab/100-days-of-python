import calculator_logo as logo
print(logo.logo)

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2
    else:
        return "division by zero error"

calculator={}
calculator['+']=add
calculator['-']=subtract
calculator['*']=multiply
calculator['/']=divide

continue_calculation=False
new_calculation=True
while continue_calculation or new_calculation:
    if new_calculation==True:
        n1=int(input("What's the first number ? "))
    else:
        n1=output
    operation=input("+\n-\n*\n/\nPick an operation :")
    n2=int(input("What's the second number ?"))
    output=calculator[operation](n1,n2)
    print(f"{n1} {operation} {n2} = {output}")
    input1=input(f" Type 'y' to continue calculating with {output} or type 'n' to start new calculation or type 'exit' to exit :").lower()
    if input1=='y':
        n1=output
        new_calculation=False
        continue_calculation=True
    elif input1=='n':
        new_calculation=True
        continue_calculation=False
    else:
        continue_calculation=False
        new_calculation=False
        
    



