num1 = int (input("Enter matix size: "))

for x in range (1, num1 + 1): 
    for y in range (1,num1 + 1) :
      if x%2 == 0:
        print(f"*", end = " ")
      else:
         print ("o", end = " ")
    print ()


while (True):


    str = input (print("Enter tring: "))
    if (str == "/"):
        break;
    for z in str:
     print(z)



    for a in range (len(str)):
        match(str[a]):
            case "a":
                print (f"{str[a]} vowel" )
            case "e":
                print (f"{str[a]} vowel" )
            case "i":
                print (f"{str[a]} vowel" )
            case "o":
                print (f"{str[a]} vowel" )
            case "u":
                print (f"{str[a]} vowel" )
            case _ :
                print(f"{str[a]} consonant")

