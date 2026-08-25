#nested loop : having a loop inside a loop ( outer loop executes till inner loop stops execution)

rows = int(input("Enter How Many rows? : "))
col = int(input("Enter How many col? : "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(col):
        print(symbol, end=" ")
    print()