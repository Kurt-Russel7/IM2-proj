while (True):

    row = int (input("Enter number of rows: "))
    if row == 0:
        break;
    col = int (input("Enter number of columns: "))
    if col == 0:
        break;
    search = int (input("Search a number: "))


    for rows in range (1, row + 1):
        for cols in range (1, col + 1):
            val = row * col
            if val == search:
                print(f"[{val:^3}]", end = " ")
            else:
                print (f"{val:5}", end = " ")
        print()
        