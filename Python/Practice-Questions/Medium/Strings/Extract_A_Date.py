"""
6. Extract a Date

Ask the user to enter a date in this format:

2026-08-23

Produce:

Year: 2026
Month: 08
Day: 23

Constraint: Use string slicing.

Don't use a date library.

Then test:

2025-12-31
2026-01-05
2030-11-17
"""
date = input("Enter Date in this format [2026-08-23 / Year-month-date] : ").strip()

find_common_sign = date.find("-")
print(find_common_sign)
year = date[0:find_common_sign]
print(f"Year : {year}")

month = date[find_common_sign + 1 : find_common_sign + 3]
print(f"Month : {month}")

day = date[-2:]
print(f"Day : {day}")