print(" My first and own calculator")

a = float(input(" Enter a number : "))

b = float(input(" Entera number : "))

print(" Choose the operations ")
print(" 1 . ADD ")
print(" 2 . SUBTRACT")
print(" 3 . MULTIPLY ")
print(" 4 . DIVIDE ")

choice = input(" Enter a operation :")

if choice == "1" :
    print("Result" , a + b)

elif choice == "2" :
    print("Result" , a - b )

elif choice == "3" :
    print(" Result" , a * b) 

elif choice == "4" :
    print("Result" , a / b)

else :
    print(" operation is invalid ")
