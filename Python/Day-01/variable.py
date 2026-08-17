# Variable = A variable is a reusable container that has a value like (integers, strings, float, boolean)
#            A variable behaves as if it was the value it contains 

# Strings = is a sequence of char
first_name = "Varrey"

#print(first_name)

# usinmg f string 
print(f"Hello {first_name}")

#integers
user_age = 25
num_of_followers = 3000

print(f"Your are {user_age} years old")
print(f"You have {num_of_followers} followers of your entire social media life")


#float
user_tokens_balance = 1.5

print(f"Your current Token balance is {user_tokens_balance}")

#boolean
user_isActive = True
print(f"Your current active status in social media {user_isActive}") 

if not user_isActive:
    print("Your account is not active, please activate your account to continue using our services")
else:
    print("Your account is active, you can continue using our services")