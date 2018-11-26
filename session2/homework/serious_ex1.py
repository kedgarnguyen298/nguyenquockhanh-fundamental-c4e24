hei = float(input("Enter your height (cm): "))
wei = float(input("Enter your weight (kg): "))

print("Your height: ", hei, "(cm)")
print("Your weight: ", wei, "(kg)")
print("--------------------------")

heim = hei / 100
BMI = wei / (heim * heim)

print("Your BMI: ", BMI)

if BMI < 16:
    print("You are Severely underweight !")
elif BMI < 18.5:
    print("You are underweight !")
elif BMI < 25:
    print("Congratulation! You're normal !")
elif BMI < 30:
    print("You are overweight !")
else:
    print("You are Obese !")