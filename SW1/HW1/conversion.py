def convert(dollar, Rupee = 83.89, pound = 0.76, yuan =7.13):
 
    Rup = dollar * Rupee
    gbp = dollar * pound
    cny = dollar * yuan
    return Rup, gbp, cny

def main():
    while True:
        inp = input("Enter dollar ($) (* to exit): ")
        if inp.strip() == '*':
            print("Bye")
            break
        
        parts = inp.split('@')
        dollars_list = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            try:
                val = float(p)
                dollars_list.append(val)
            except ValueError:
                print(f"Ignoring invalid input: {p}")

            if not dollars_list:
        
             continue
        
     
        print(f"{'Dollar ($)':<15}{'Indian Rupee (₹)':<20}{'British Pound (£)':<20}{'Chinese Yuan (¥)'}")
        
        for amount in dollars_list:
            Rup, gbp, cny = convert(amount)
            print(f"{amount:<15.2f}{Rup:<20.2f}{gbp:<20.2f}{cny:.2f}")
        
if __name__ == "__main__":
    main()
