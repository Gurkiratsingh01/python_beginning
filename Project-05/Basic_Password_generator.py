import random
import string
 
length = int(input(" Enter password length "))

all_chars = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(all_chars) for i in range(length))

print(" Your password is : " , password)