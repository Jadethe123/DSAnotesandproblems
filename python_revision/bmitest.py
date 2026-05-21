height = float(input("enter height in m :"))
weight = float(input("enter weight is kg : "))

bmi = weight / height**2

print(bmi)
if bmi <= 18.5:
    print("underweight")
elif 18.5 <=bmi<= 24.9:
    print("normal")
elif 25<=bmi<=29.9:
    print("overweight")
elif 30<= bmi <=34.9:
    print("obese")
