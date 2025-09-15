row1 = []

row= int (input("Enter number of rows: "))
    
col = int (input("Enter number of columns: "))
    
for x in range (row):
    print(f"Enter row1 score {x}: ")
    num1 = int (input())
    row1.append(num1)
    col1 = []
    for y in range (col):
      print(f"Enter row2 score: ")
      num2 = int (input())
      col1.append(num2)
    
print(row1)
print(col1)




   











    


