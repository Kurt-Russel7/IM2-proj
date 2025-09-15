
mydict = {

    }


    
    
matrix = int (input("Matrix Size: "))
for x in range (matrix):
    val = input(f"Shopping items {x + 1}")
    mydict [x] = val
        

    print (mydict)
while(True):
    opt = input("What would you like to do [C]hange items [R]emove [D]isplay  S[earch] ? ").upper()
    
    match opt:
        case 'C':
            print ("change")
        case 'R':
            print ("Remove")
        case 'D':
            print (mydict)
        case 'S':
            findKey = int (input("Enter a key you want to search:"))
            if findKey in mydict:
                print(mydict.get(findKey))
            else:
             print("I'm sorry, not in the cart")
        
