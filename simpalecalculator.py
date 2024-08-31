# user Inpute 
num1 = float(input ("Enter the First Number"))
num2 = float(input ("Enter the secound Number"))
opration = input("Choise The opration (+,-,*,/):")

# simple calculator using python

def calculate(num1, num2, opretion):
    if operation=='+':
        return num1 + num2
    elif opretion=='-':
        return num1 + num2
    elif operation=='*':
        return num1 * num2
    elif opretion=='/':

        if num=='0':
            return "Error! Division by Zero"
        else:
            return num1 / num2
    else:
        return "Inalide Equation"
    
    # Opration_Perform

    result= Calculate(num1, num2, Opration)
print(f"The result is: {result}")

exceptValueError:
print("Invalid input! Please enter numeric values.")