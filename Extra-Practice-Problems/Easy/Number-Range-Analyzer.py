"""
3. Number Range Analyzer

Ask the user for a starting number and ending number.

Example:

Start: 1
End: 20

Display:

Numbers divisible by 3: 3 6 9 12 15 18
Numbers divisible by 5: 5 10 15 20

Then display:

Numbers divisible by both: 15

Focus: for + conditions + logical operators.
"""
start_num = int(input("Enter A starting number: "))
end_num = int(input("Enter A ending number: "))
nums_divisible_by_3 = ""
nums_divisible_by_5 = ""
nums_divisible_by_both = ""

for i in range(start_num, end_num + 1  ):
    if i % 3 == 0:
        nums_divisible_by_3 += str(i) + " "
    if i % 5 == 0:
        nums_divisible_by_5 += str(i) + " "
    if i%3 == 0 and i % 5 == 0:
        nums_divisible_by_both += str(i) + " "

print(f"Numbers divisible by 3: {nums_divisible_by_3}")
print(f"Numbers divisible by 5: {nums_divisible_by_5}")
print(f"Numbers divisible by both: {nums_divisible_by_both}")