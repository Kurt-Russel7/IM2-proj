mydict = {

    }

matrix = int (input("Matrix Size: "))
for x in range (matrix):
    val = input(f"Shopping items {x + 1}: ")
    mydict [x] = val
        


    print (mydict)
while(True):
    opt = input("What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").upper()
    
    match opt:
        case 'C':
            changeKey = int (input("Enter key to change value:"))
            if changeKey in mydict:
                print (f"Found '{mydict.get(changeKey)}'  item")
                changeVal = input("Enter Value:")
                mydict[changeKey] = changeVal
            else:
                 print("I'm sorry, not in the cart")



        case 'R':
            DelKey = int (input("Enter a key you want to delete:"))
            if DelKey in mydict:
                mydict.pop(DelKey)
            else:
                Delval = input("Enter item you want to delete:")
                if Delval in mydict.values():
                    mydict.popitem()
                else:
                    print("Item not found")

        case 'D':
            print (mydict)
        case 'S':
            findval = input("Enter item to search:")
            if findval in mydict.values():
                print (f"Found '{findval}'  item")

            else:


                findKey = int (input("Enter a key you want to search:"))
                if findKey in mydict:
                    print(mydict.get(findKey))
                else:
                 print("I'm sorry, not in the cart")

        case '*':
            print ("bye")
            break

        
