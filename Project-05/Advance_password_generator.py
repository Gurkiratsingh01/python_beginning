import random
import string

print(" Choose the password type ")
print(" 1 . letters only '")
print(" 2 . letters + digits ")
print(" 3 . strong ( letters + digits + punctuation) ")

choice = int(input(" Enter type (1,2,3) "))

if choice == 1 :
    chars = string.ascii_letters

elif choice == 2 :
    chars = string.ascii_letters+ string.digits

elif choice == 3 :  
    chars = string.ascii_letters + string.digits + string.punctuation

else: 
    print( " invalid choice ")
    exit()

length = int(input(" Enter password length "))

password = "".join(random.choice(chars) for i in range (length))

print(" Your password is : " , password)