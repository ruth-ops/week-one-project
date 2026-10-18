#cafee order system
input("Welcome to our cafe! Please place your order.")

user_name = input("What is your name? ")
cup_str = input("How many cups of coffee would you like to order? ")
cup_count = int(cup_str)
total_cost = cup_count * 50
print("Thank you, " + user_name + ". Your order of " + str(cup_count) + " cups of coffee has been placed.")
print("The total cost of your order is Ksh " + str(total_cost) + ".")