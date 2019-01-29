question = input("Are you going out?")



while question == "yes" or "maybe ":
  if question == "no":
    break
  temperature = float(input("What is the temperature? "))
  if temperature in range(60, 70):
    print("Wear a light jacket or long sleeve shirt. ")
  elif temperature in range(50, 59):
    print("Wear a light vest under your jacket. ")
  elif temperature in range(40, 49):
    print("Wear a sweater under your jacket, wear gloves and bring your hat. ")
  elif temperature < 40:
    print("It's too cold outside, watch some netflix. ")
  elif temperature > 70:
    print("Get some sunscreen and go to the pool. ")
  break
  
