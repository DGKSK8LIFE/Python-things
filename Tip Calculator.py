check = float(input("How much was the total of price of your lunch? "))
persons = int(input("How many people are dining including youreslf? "))

each = str(check / persons)

tip = str(0.18 * check)

print("Each one needs to pay " + "$" + each + ".")

print("The waiter will recieve " + "$" + tip + " as a tip.")
