row = int (input("Enter number of rows: "))

col = int (input("Enter number of columns: "))

search = int (input("Search a number: "))


for row in range (1, row + 1):
    for col in range (1, col + 1):
        val = row * col
        if val == search:
            print(f"[{val:^3}]", end = " ")
        else:
            print (f"{val:5}", end = " ")
    print()
        