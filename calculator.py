print("Calculator")
number=int(input("Enter the number: "))
#Get the operation
operation=input("Enter the operation (+, -, *, /): ")
#Get the second number
number2=int(input("Enter the second number: "))
#Perform the operation
if operation=="+":
    print("result is:",number+number2)
elif operation=="-":
    print("result is:",number-number2)
elif operation=="*":
    print("result is:",number*number2)
elif operation=="/":
 print("result is:",number/number2)
elif operation=="%":
    print("result is:",number%number2)
else:
    print("Invalid operation")