#If Statement : a block of code that will execute if it's condition is true

user_age = int(input("Enter Your Age : "))


if user_age == 100:
    print("centuray!...")
elif user_age >= 18:
    print("Your Adult!..")
else:
    print("Your child!.")