# for loop : a statement that will execute it's block of code a limited amount of time
# while loop -> Unlimited & for  loop -> limited

#for i in range(10):
    #print(i+1)

#for i in range(50, 100+1, 2):
 #   print(i)

import time

for sec in range(10, 0, -1):
    print(sec)
    time.sleep(1)
print("Happy New Year")