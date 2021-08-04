#Pizza Ordering System

#Pizzas Available
pizzas ={
1:["01. Cheese", 8.50],
2:["02. Cheese XL", 8.50],
3:["03. Cheese & Garlic", 8.50],
4:["04. Sweet Corn", 8.50],
5:["05. Anchovies", 8.50],
6:["06. Chicken", 8.50],
7:["07. ", 8.50],
8:["08. ", 13.50],
9:["09. ", 13.50],
10:["07. Italian", 13.50],
11:["08. MeatLovers", 13.50],
12:["09. Margherita", 13.50],
}

drinks ={
1:["1. Coke", 10.00],
2:["2. Sprite", 10.00],
3:["3. Pepsi", 10.00],
4:["4. Fanta", 10.00],
5:["5. Iron Brew", 10.00],
6:["6. Lemonade", 10.00],
7:["7. Dr Pepper", 10.00],
8:["8. 7 up", 10.00],
9:["9. Water", 10.00],
}

#Menu
def main_menu():
    while True:
        print("="*28 + " Stephanie's Pizzeria " + "="*24) 
        print("=" * 32 + " Main Menu " + "=" * 32 + "\n"     
              "\t(O) Order\n"                              
              "\t(E) Exit\n" +
              "_" * 72)

        main = str(input("Please Select Your Operation: ")).upper()    
        if (len(main) == 1):                                           
            if (main == 'O'):                                          
                print("\n" * 2)                                        
                order()                                       
                break                                                                                                                                                 
            elif (main == 'E'):                                        
                print("=" * 32 + " Bye " + "=" * 31 + "\n")           
                break                                                    
            else:                                                                                 
                print("\n" * 4 + "ERROR: Invalid Input (" + str(main) + "). Try again!")     
        else:                                                                                     
            print("\n" * 4 + "ERROR: Invalid Input (" + str(main) + "). Try again!")        


def order():
    while True:
        print("="*28 +" Menu " + "="*28)
        print("\t(P) Pizza\n" +
              "\t(D) Drinks\n" +
              "\t(E) Exit\n" +
              "_" * 72)

        order= str(input("What Would You Like To Order?: ")).upper()
        if (len(order) == 1):                                           
            if (order == 'P'):                                          
                print("")
                for entry in list(pizzas):
                    print(str(pizzas[entry][0]) + " $" + str(pizzas[entry][1]))
                    pizza()                                   
                break                                                                                                                                                 
            elif (order == 'D'):                                        
                print("")
                for entry in drinks:
                    print(entry)
                break
            elif (order == 'E'):                                        
                print("=" * 32 + " Bye " + "=" * 31 + "\n")           
                break            
            else:                                                                                 
                print("\n" * 4 + "ERROR: Invalid Input (" + str(order) + "). Try again!")     
        else:                                                                                     
            print("\n" * 4 + "ERROR: Invalid Input (" + str(order) + "). Try again!")        

def pizza():
    print("stop")

main_menu() 