#Pizza Ordering System
#Imports

# I imported time so I can delay print statrements to clearly separate some print statments easier.
import time
#Empty List that will be filled with their Pizza
order_list = []
#Empty ;ist that will be filled with their drinks
drink_list = []
#Empty List that will be filled with their Price
price_list = []
#Empty List that will be filled with their Toppings
topping_list = []
#To check if they have picked delivery or pickup
delivery_list = []
#Stores Customers Address for later use (meant to spelt wrong)
adderess = []
#Pizzas Available (Pizza Menu)
pizzas ={
1:["No. 01. Cheese", 8.50],
2:["No. 02. Cheese XL", 8.50],
3:["No. 03. Cheese & Garlic", 8.50],
4:["No. 04. Sweet Corn", 8.50],
5:["No. 05. Anchovies", 8.50],
6:["No. 06. Chicken", 8.50],
7:["No. 07. Bacon", 8.50],
8:["No. 08. Beef & Onion", 13.50],
9:["No. 09. Chicken & Cranberry", 13.50],
10:["No. 10. Italian", 13.50],
11:["No. 11. MeatLovers", 13.50],
12:["No. 12. Margherita", 13.50],
}
#Drinks Available (Drink Menu)
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
#Toppings Available (Toppings Menu)
toppings ={
1:["1. Pepperoni", 0,50],
2:["2. Sausage", 0.50],
3:["3. Mushroom", 0.50],
4:["4. Extra Cheese", 0.50],
5:["5. Onions", 0.50],
}

#Menu
def main_menu():
    while True:
#Boundary Values for number of Pizzas (So it is not less than 0 or more than 5)
        if len(order_list) >= 5 or len(order_list) < 0:
            limit()
            break

#Name and Main Menu of the Program shows Functions of ordering or exiting.
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
                print("\n" * 2 + "ERROR: Invalid Input (" + str(main) + "). Try again!")     
        else:                                                                                     
            print("\n" * 2 + "ERROR: Invalid Input (" + str(main) + "). Try again!")        

#Order
def order():
    while True:
#Boundary Values for number of Pizzas (So it is not less than 0 or more than 5)
        if len(order_list) >= 5 or len(order_list) < 0:
            limit()
            break

#Options for ordering a Pizza a Drink or exiting>
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
                for entry in list (drinks):
                    print(str(drinks[entry][0]) + " $" + str(drinks[entry][1]))
                drink()
                break
            elif (order == 'E'):                                        
                print("=" * 32 + " Bye " + "=" * 31 + "\n")           
                break            
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(order) + "). Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(order) + "). Try again!")        

#Select Pizza from menu
def pizza():
    while True: 
#Boundary Values for number of Pizzas (So it is not less than 0 or more than 5)
        if len(order_list) >= 5 or len(order_list) < 0:
            limit()
            break

#(Pizza Menu already Printed) Stores your pizza choice.
        print("_" * 72)
        pizza_type = int(input("Select Your Pizza No. "))
        if (pizza_type <=12):
            print("\n" + "_" * 72  )
            no_ = input("How many {} Pizzas would you like? ".format(pizzas[pizza_type][0]))
            no_ = int(no_)
            if no_ > 5 or no_ < 1:
                print("You can unfortunately only order between 1 and 5 pizzas at a time.")
                print("")
                for entry in list(pizzas):
                    print(str(pizzas[entry][0]) + " $" + str(pizzas[entry][1]))
                pizza()
                break
            for no_ in range(no_): 
                order_list.append(pizzas[pizza_type][0])
                price_list.append(pizzas[pizza_type][1]) 
            print(order_list)
            print("\n" * 2)
            topping()
            break  
        else:                                                                  
            print("\n" * 2 + "ERROR: Invalid Input (" + str(pizza_type) + "). Try again!")

#Select drinks from menu
def drink():
    while True:
#Boundary Values for number of Pizzas (So it is not less than 0 or more than 5)
        if len(drink_list) >= 5 or len(order_list) < 0:
            limit()
            break

#(Srink Menu already Printed) Stores your drink choice.
        print("_" * 72)
        drink_type = int(input("Select Your Drink No. "))
        if (drink_type <=9):
            print("\n" + "_" * 72  )
            no_ = input("How many {} drinks would you like? ".format(drinks[drink_type][0]))
            no_ = int(no_)
            if no_ > 5 or no_ < 1:
                print("You can unfortunately only order between 1 and 5 drinks at a time.")
                print("")
                for entry in list (drinks):
                    print(str(drinks[entry][0]) + " $" + str(drinks[entry][1]))
                drink()
                break
            for no_ in range(no_): 
                drink_list.append(drinks[drink_type][0])
                drink_list.append(drinks[drink_type][1]) 
            print(drink_list)
            print("\n" * 2)
            finishing()
            break  
        else:                                                                  
            print("\n" * 2 + "ERROR: Invalid Input (" + str(drink_type) + "). Try again!")

#Extra Toppings
def topping():
    while True:
        print("_" * 72)
        extra_toppings = str(input("Would you like extra toppings? (Y/N): ")).upper()
        if (len(extra_toppings) == 1):      
            if (extra_toppings == 'Y'):
                print("")
                for entry in list(toppings): 
                    print(str(toppings[entry][0]) + " $" + str(toppings[entry][1]))
                print("_" * 72)
                topping_type = int(input("Select Your Topping No. "))
                if (topping_type <=5):
                    topping_list.append(toppings[topping_type][0])
                    price_list.append(toppings[topping_type][1])
                    print(topping_list)  
                    print("\n" * 2)
                else:                                                                  
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(topping_type) + "). Try again!")
            elif (extra_toppings == 'N'):
                print("\n" * 2)
                finishing()
                break
            else:                                                                                     
                print("\n" * 2 + "ERROR: Invalid Input (" + str(extra_toppings) + "). Try again!")
        else:                                                                                     
                print("\n" * 2 + "ERROR: Invalid Input (" + str(extra_toppings) + "). Try again!")      

#Checking
def finishing():
    while True:
        print("_" * 72)
        continue_ordering = str(input("Is that all today? (Y/N): ")).upper()
        if (len(continue_ordering) == 1):      
            if (continue_ordering == 'N'):
                print("\n" * 2)
                order()
                break
            elif (continue_ordering == 'Y'):
                print(order_list)
                print("\n" * 2)
                print("_" * 72)
                check_order = str(input("Is this what you would like to order? (Y/N):")).upper()
                if (len(check_order) == 1):      
                    if (check_order == 'Y'):
                        print("\n" * 2)
                        delivery()
                        break
                    elif (check_order == 'N'):
                        restart = str(input("You Have Made A Mistake Then. Would you like to restart? (Y/N:)")).upper()
                        if (len(restart) == 1):      
                            if (restart == 'Y'):
                                main_menu()
                                break
                            if (restart == 'N'):
                                break
                            else:
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                        else:                                                                                     
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                    else:                                                                                     
                        print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                else:                                                                                     
                        print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")      
            else:                                                                                     
                print("\n" * 2 + "ERROR: Invalid Input (" + str(continue_ordering) + "). Try again!")
        else:                                                                                     
                print("\n" * 2 + "ERROR: Invalid Input (" + str(continue_ordering) + "). Try again!")      

#Delivery
def delivery():
    while True:
        print("=" * 20 + " Pickup or Delivery (Cost of $3) " + "=" * 20 + "\n"     
              "\t(P) Pickup\n"                              
              "\t(D) Delivery\n" +
              "_" * 72)

        delivery_option = str(input("Please Select Your Operation: ")).upper()    
        if (len(delivery_option) == 1):                                           
            if (delivery_option == 'P'):                                          
                print("\n" * 2)                                        
                payment()                                       
                break                                                                                                                                                 
            elif (delivery_option == 'D'):                                        
                print("I will have to take down some details for delivery.")
                name = str(input("Name: ")).title()       
                address = str(input("Address: ")).title()
                phone_no = str(input("Phone Number: "))
                print("_" * 72)
                time.sleep(1.5)
                print("Are these details correct?")
                print(
                "Name: {} \n".format(name) + 
                "Address: {} \n".format(address) + 
                "Phone Number: {}".format(phone_no) 
                )
                adderess.append(address)
                print("_" * 72)
                print(
                    "\n" +
                    "\t(Y) Yes\n" +
                    "\t(N) No\n" +
                    "_" * 72)
                delivery_details = str(input("Please Select an Operation: ")).upper()    
                if (len(delivery_details) == 1):                                           
                    if (delivery_details == 'Y'):       
                        price_list.append(3)
                        delivery_list.append("x")                                   
                        print("\n" * 2)                                        
                        payment()                                       
                        break                                                                                                                                                 
                    elif (delivery_details == 'N'): 
                        print("_" * 72)                                       
                        delivery()    
                        break                                               
                    else:                                                                                 
                        print("\n" * 4 + "ERROR: Invalid Input (" + str(delivery_details) + "). Try again!")     
                else:                                                                                     
                    print("\n" * 4 + "ERROR: Invalid Input (" + str(delivery_details) + "). Try again!")                                                   
            else:                                                                                 
                print("\n" * 4 + "ERROR: Invalid Input (" + str(delivery_option) + "). Try again!")     
        else:                                                                                     
            print("\n" * 4 + "ERROR: Invalid Input (" + str(delivery_option) + "). Try again!")     
#Payment
def payment():
    price = sum(price_list)
    price = str(price)
    print("You order comes to a total of ${}.".format(price))
    time.sleep(0.4)
    if (len(delivery_list) == 1):
        print("That will be delivered to {} in 45mins".format(adderess))
    time.sleep(0.4)
    if (len(delivery_list) == 0):
        print("You order will be ready to pick up in 30mins")
    print("Have a lovely day.")


#Pizza Limit
def limit():
    while True:
        print("Help!")
        break


main_menu()