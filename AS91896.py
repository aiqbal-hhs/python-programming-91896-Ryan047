#Pizza Ordering System
#Imports
# I Imported time so I can delay print statrements to clearly separate some print statments easier.
import time
#Empty List that will be filled with their Pizza
order_list = []
#Empty List that will be filled with their drinks
drink_list = []
#Empty List that will be filled with their Price
price_list = []
#Empty List that will be filled with their Toppings
topping_list = []
#To check if they have picked delivery or pickup
delivery_list = []
#List of Yes Answers
yes = ["YES", "Y", "YEP", "YEAH", "YO", "YUP"]
#List of No Answers
no = ["NO", "N", "NAH", "NOPE",]
#Stores Customers Address for later use (meant to spelt wrong)
adderess = []
#Pizzas Available (Pizza Menu)
pizzas ={
#Dictionary: Pizza Name, Price
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
#Dictionary: Drink Name, Price
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
#Dictionary: Topping Name, Price
1:["1. Pepperoni", 0,50],
2:["2. Sausage", 0.50],
3:["3. Mushroom", 0.50],
4:["4. Extra Cheese", 0.50],
5:["5. Onions", 0.50],
}
#Function
def get_int(prompt):
    while True:
        try:
            answer = int(input(prompt))
            break
        #When a value error is triggered it will return the question again
        except ValueError:
            print("Please make sure you enter an integer value in your answer.\n============================================================")
    return answer




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
#Prints the Menu in a Way that I can Constantly change it.
                for entry in list(pizzas):
                    print(str(pizzas[entry][0]) + " $" + str(pizzas[entry][1]))
                pizza()                                       
                break                                                                                                                                                 
            elif (order == 'D'):                                        
                print("")
#Prints the Menu in a Way that I can Constantly change it.
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
        pizza_type = int(get_int("Select Your Pizza No. "))
        if (pizza_type <=12) and (pizza_type >= 1 ):
            print("\n" + "_" * 72  )
#Value Error 
#Only Accepts Integers So My Code Does Not Break
            while True:
                try:
                    no_ = int(input("How many {} Pizzas would you like? ".format(pizzas[pizza_type][0])))
                    break
                except ValueError:
                    print("Error: Incorrect Input, please enter a number.\n")

            if no_ > 5 or no_ < 1:
#Makes Sure they can not order more than 5 Pizzas
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
#(drink Menu already Printed) Stores your drink choice.
        print("_" * 72)
        drink_type = int(input("Select Your Drink No. "))
        if (drink_type <=9):
            print("\n" + "_" * 72  )
#Value Error 
#Only Accepts Integers So My Code Does Not Break
            while True:
                try:
                    no_ = int(input("How many {} drinks would you like? ".format(drinks[drink_type][0])))
                    break
                except ValueError:
                    print("Error: Incorrect Input, please enter a number.\n")
#Make Sure Not To Order More Than 5 Pizza
            if no_ > 5 or no_ < 1:
                print("You can unfortunately only order between 1 and 5 drinks at a time.")
                print("")
                for entry in list (drinks):
                    print(str(drinks[entry][0]) + " $" + str(drinks[entry][1]))
                drink()
                break
#Adding the Ordered Drink and Price to a List that I will later Call on.
            for no_ in range(no_): 
                drink_list.append(drinks[drink_type][0])
                price_list.append(drinks[drink_type][1]) 
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
        if (len(extra_toppings) <=4 or len(extra_toppings > 1)):      
            if (extra_toppings in yes):
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

                else: #<----- Making my Code Robust                                                              
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(topping_type) + "). Try again!")
            elif (extra_toppings in no):
                print("\n" * 2)
                finishing()
                break
            else: #<----- Making my Code Robust                                                                                    
                print("\n" * 2 + "ERROR: Invalid Input (" + str(extra_toppings) + "). Try again!")
        else:  #<----- Making my Code Robust                                                                               
                print("\n" * 2 + "ERROR: Invalid Input (" + str(extra_toppings) + "). Try again!")      

#Checking
def finishing():
    while True:
        print("_" * 72)
        continue_ordering = str(input("Is that all today? (Y/N): ")).upper()
        if (len(continue_ordering) <= 4 or len(continue_ordering) > 1):      
            if (continue_ordering in no):
                print("\n" * 2)
                order()
                break
            elif (continue_ordering in yes):
                print(order_list)
                print(drink_list)
                print("\n" * 2)
                print("_" * 72)
                check_order = str(input("Is this what you would like to order? (Y/N):")).upper()
                if (len(check_order) <= 4 or len(check_order) > 1):      
                    if (check_order in yes):
                        print("\n" * 2)
                        delivery()
                        break
                    elif (check_order in no):
                        print("\n" * 2)
                        print("_" * 72)
                        restart = str(input("You Have Made A Mistake Then. Would you like to restart? (Y/N:)")).upper()
                        if (len(restart) <= 4 or len(restart) > 1):      
                            if (restart in yes):
                                order_list.clear()
                                drink_list.clear()
                                price_list.clear()
                                topping_list.clear()
                                delivery_list.clear()
                                main_menu()
                                break
                            if (restart in no):
                                break
                            else:#<----- Making my Code Robust
                                print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                        else: #<----- Making my Code Robust                                                                                    
                            print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                    else:#<----- Making my Code Robust                                                                                     
                        print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")
                else:#<----- Making my Code Robust                                                                                     
                        print("\n" * 2 + "ERROR: Invalid Input (" + str(check_order) + "). Try again!")      
            else:#<----- Making my Code Robust                                                                                     
                print("\n" * 2 + "ERROR: Invalid Input (" + str(continue_ordering) + "). Try again!")
        else:#<----- Making my Code Robust                                                                                     
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
                if (len(delivery_details) <= 4 or len(delivery_details) > 1):                                           
                    if (delivery_details in yes):       
                        price_list.append(3)
                        delivery_list.append("x")                                   
                        print("\n")                                        
                        payment()                                       
                        break                                                                                                                                                 
                    elif (delivery_details in no): 
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

#Pizza Limit
def limit():
#To Keep People In Check When They Want To Order More Than 5 Pizza.
    while True:
        if len(order_list) >= 5:
            print("Unfortunately You Have Too Many Pizzas, FATTY!!. \n" + "Maximum No is 5 Pizzas and You Cannot Order Anymore Pizzas. \n")
            print("=" * 32 + " What would you like to do to you Order? " + "=" * 32 + "\n"     
                  "\t(R) Remove\n"                              
                  "\t(E) Exit\n" +
                  "_" * 72)                                  
            piiza_removal = str(input("Please Select Your Operation: ")).upper()
            if (len(piiza_removal) == 1):                                           
                if (piiza_removal == 'R'): 
                    remove()                                         
                    pass                                 
                elif (piiza_removal == 'E'):                                                   
                    break                                                    
                else: #<----- Making my Code Robust                                                                                 
                    print("\n" * 2 + "ERROR: Invalid Input (" + str(piiza_removal) + "). Try again!")     
            else:   #<----- Making my Code Robust                                                                                  
                print("\n" * 2 + "ERROR: Invalid Input (" + str(piiza_removal) + "). Try again!")

        elif len(order_list) < 1:
            print("=" * 32 + " You Must Order a Pizza " + "=" * 32 + "\n"     
                  "\t(O) Ok\n"                              
                  "\t(N) No\n" +
                  "_" * 72)
#Remove Or Proceed With An Order
        order_change = str(input("Please Select Your Operation: ")).upper()    
        if (len(order_change) == 4):                                           
            if (order_change == 'O'):                                          
               main_menu()
            elif (order_change in no):                                        
                print("You Are Wasting My Time.")           
                break                                                    
            else: #<----- Making my Code Robust                                                                                 
                print("\n" * 2 + "ERROR: Invalid Input (" + str(order_change) + "). Try again!")     
        else:  #<----- Making my Code Robust                                                                                 
            print("\n" * 2 + "ERROR: Invalid Input (" + str(order_change) + "). Try again!") 
        break

#Remove
def remove():
    print("_" *72)
    print("You Have Too Many Items. \n" +
          "You Will Remove An Item. \n" +
          "\t")
    
#Prints The Current Order
    print(order_list)
    print("_" *72)
    while True:
            try:
                pizza_removal = int(input("Select Which Pizza You Want To Order...Your Number Will Correspond to a Pizza in that List Placement. \nNo."))
                pizza_removal = pizza_removal - 1
                break
            except ValueError:
                print("Error: Incorrect Input, please enter a number.\n")
    order_list.remove(order_list[pizza_removal])
#Prints New Order
    print(order_list)
#Adding/Removing Another Pizza, Paying or Exiting
    print("_" * 72)
    print("Request Complete. What do you want to do next?")
    print("_" * 72)
    print("\t(A) Add Pizza\n" + 
          "\t(R) Remove Another Pizza\n" +
          "\t(P) Pay\n" +                
          "\t(E) Exit\n" +
          "_" * 72)
    while True:
        remove_choice = str(input("Please Select Your Operation: ")).upper()    
        if (len(remove_choice) == 1): 
#Adding New Pizza                                          
            if (remove_choice == 'A'):                                          
                print("\n" * 2)                                        
                order()
                break
#Removing Another Pizza                                                                                                                                                                                      
            elif (remove_choice == 'R'):    
                print("\n" * 2)                                      
                remove()
                break
#Paying For Order
            elif (remove_choice == 'P'): 
                print("\n" * 2)  
                payment()
                break          
#Allows To Exit Program                             
            elif (remove_choice == 'E'):                                        
                break                                          
            else:                                                                                 
                print("\n" * 2 + "ERROR: Invalid Input (" + str(remove_choice) + "). Try again!")     
        else:                                                                                     
            print("\n" * 2 + "ERROR: Invalid Input (" + str(remove_choice) + "). Try again!")        

#Payment
def payment():
#Sums Each Price For Every Item Ordered
    price = sum(price_list)
    price = str(price)
#Prints Price Total
    print("You order comes to a total of ${} ".format(price))
    print("_" * 72  )
    time.sleep(0.4)
    if (len(delivery_list) == 1):
        print("That will be delivered to {} in 45mins \n".format(adderess))
        print("_" * 72  )
    time.sleep(0.4)
    if (len(delivery_list) == 0):
        print("You order will be ready to pick up in 30mins")
    re_order()
  
#Order Again
def re_order():
    while True:
        print("\n" + "_" * 72  )
        print("\t(N) New..Order\n"    
              "\t(E) Exit\n" +
              "_" * 72)   
        order_again = input("Is that all today? or Would you like to make another order? ").upper()
        if (len(order_again) == 1):                                    
            if (order_again == 'N'): #Make a New Order                                 
                print("\n" * 2)
                order_list.clear()
                drink_list.clear()
                price_list.clear()
                topping_list.clear()
                delivery_list.clear()                                               
                order()
                break                               
            elif (order_again == 'E'):  #Exit     
                print("\n" * 2)                                      
                print("Okay then. \n" + "Thank you for placing a order. \n" + "Have a lovely day.")
                print("\n" + "_" * 72  )
                break
            else: #<----- Making my Code Robust             
                print("\n" * 2 + "ERROR: Invalid Input (" + str(order_again) + "). Try again!")
        else:  #<----- Making my Code Robust   
            print("\n" * 2 + "ERROR: Invalid Input (" + str(order_again) + "). Try again!") 
            
main_menu() 
