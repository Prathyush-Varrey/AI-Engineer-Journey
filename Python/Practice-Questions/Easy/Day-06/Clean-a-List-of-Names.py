"""
3. Clean a List of Names

Start with:

names = ["  prathyush", "RAHUL ", "  anil  ", "SNEHA"]

Produce:

Cleaned names:
Prathyush
Rahul
Anil
Sneha

Your program should:

Remove unnecessary spaces
Normalize capitalization
Process every name

Challenge: Don't manually clean each name.
"""
names = ["  prathyush", "RAHUL ", "  anil  ", "SNEHA"]

cleaned_names = [name.strip().capitalize() for name in names]

print("Cleaned names:")
for name in cleaned_names:
    print(name)
