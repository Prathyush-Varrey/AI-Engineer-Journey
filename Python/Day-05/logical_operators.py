#logical operators (and, or, not): used to check if 2 or more conditional statments are true 

temp = int(input("Enter temperature outside! : "))

if temp >= 0 and temp <= 30:
    print("Go outside!....")
elif temp < 0 or temp > 30 :
    print("Saty inside!...")

# not flips nature of the conditon if it's true <-> false  