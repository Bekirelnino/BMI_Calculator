print("hello")

first_name=input("whats your first name?:")
last_name=input("whats your last name?:")
age=int(input("how old are you?:"))
weight=float(input("whats your weight(kg)?:"))
height=float(input("whats your height(m)?:"))
BMI=weight/(height**2)
if BMI < 18.5:
   category="Under weight"
elif BMI>= 18.5 and BMI<25:
   category="Normal weight"
elif BMI>=25 and BMI<30:
    category="Over weight"
elif BMI>=30:
    category="Obese weight"
print("Dear",first_name,last_name,"you are",age,"your BMI is",BMI,"and you are",category)