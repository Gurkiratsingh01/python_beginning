a = float(input(" Enter your weight "))

b = float(input(" Enter your height (metres) "))

BMI = a/(b*b)

if BMI < 18.5 :
    print(" UNDERWEIGHT ")

elif 18.5 <= BMI <= 24.9 :
    print(" NORMAL WEIGHT ")

elif 25 <= BMI <= 29.9 :
    print(" OVERWEIGHT ")

elif BMI >= 30 :
    print(" OBEESE ")

else :
    print(" Invalid data ")

