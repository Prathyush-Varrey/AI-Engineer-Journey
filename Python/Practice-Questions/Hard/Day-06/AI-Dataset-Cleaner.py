"""
7. 🔥 AI Dataset Cleaner

Imagine you receive this messy dataset:

data = [
    [" Prathyush ", "24", "India"],
    ["RAHUL", "27", "india"],
    [" sneha", "22", "INDIA"],
    ["Anil ", "25", "India"]
]

Your goal is to produce:

[
    ["Prathyush", 24, "India"],
    ["Rahul", 27, "India"],
    ["Sneha", 22, "India"],
    ["Anil", 25, "India"]
]

Notice:

Names have inconsistent spaces/capitalization.
Ages are strings and need to become numbers.
Countries have inconsistent capitalization.
Challenge

You must process the entire 2D list programmatically.

Don't manually modify individual rows.

Think:
2D list
   ↓
row
   ↓
individual value
   ↓
clean/convert
   ↓
store result

This is very close to the type of thinking you'll eventually use with Pandas.
"""

data = [
    [" Prathyush ", "24", "India"],
    ["RAHUL", "27", "india"],
    [" sneha", "22", "INDIA"],
    ["Anil ", "25", "India"]
]

cleaned_data = []

for row in data:
    cleaned_row = []
    for item in row:
        item = item.strip()
        if  item.isalpha():
            cleaned_row.append(item.capitalize())
        if item.isdigit():
            item = int(item)
            cleaned_row.append(item) 
    cleaned_data.append(cleaned_row)
print(cleaned_data)