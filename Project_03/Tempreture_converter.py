print(" TEMPRETURE CONVERTER ")

print(" Choose the conversion ")
print(" 1 . Celcius to ferenhite ")
print(" 2 . Ferenhite to Celcius ")

a = input(" Enter the conversion, (1.2) ")

if a == "1" :
    c = float(input(" enter the tempreture in celcius "))  
    f = (c*9/5) + 32
    print("Tempreture in ferenhite is : " , f )

elif a == "2" :
    f = float(input(" Enter the tempreture in Ferenhite "))
    c = (f - 32) * 5/9
    print(" Tempreture in Celcius is : " , c )

else :
    print("conversion is invalid")