#Print
print("Python is a cool programming language.")
print("\"Python\" is a cool programming language.")
print("'Python' is a cool programming language.")
print("Matthew \n" * 8)
#Combining Strings
string1 = "The quick brown fox "
string2 = "jumps over the lazy dog"
#Combine the strings
print(string1 + string2)
#Pizza
DELIVERY = 10
PIZZA_PRICE = 15
# Set variable equal to input
num_pizzas = int(input("How many pizzas do you want? \n"))
#Set variable to pizzas times price
order_total = num_pizzas * PIZZA_PRICE
# if pizzas are less than 3
if num_pizzas < 3:
  print("Delivery will cost ${}".format(DELIVERY))
  order_total += DELIVERY
else:
  print("Free delivery for 3 or more pizzas!")
#Print "Your order comes to:..."
print("Your order comes to: ${}".format(order_total))
