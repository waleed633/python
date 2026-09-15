# Python program to print star pattern based on the rows specified by the user
# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))
# outer loop for each row
for i in range(1, rows+1):
    # Inner loop for each column in the row
    for j in range(1, i+1):
        # Print star without newline
        print("*", end="")
        # After each row, print a new line
    print()
