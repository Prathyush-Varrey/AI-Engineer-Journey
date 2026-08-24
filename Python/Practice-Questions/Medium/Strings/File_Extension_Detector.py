"""
4. File Extension Detector

Ask the user for a filename:

Enter filename: model_training.csv

Your program should display:

Filename: model_training.csv
Extension: csv

Test with:

data.csv
model.py
report.pdf
image.png
Challenge

Don't assume that every filename has the same number of characters.

Your solution needs to work regardless of the filename length.

I need to find "." then extract the characters after the "."
"""
user_input = input("Enter Your File Name Here :").strip()

find_common_sign = user_input.find(".")
#print(find_common_sign)
file_extension = user_input[find_common_sign + 1:]
print(f"Extension : {file_extension}")