#used to determine whether the user is underaged or not

age = input ("What's your age? ")

if int(age) < 18:
    print("You are underaged.")
else: 
    print("You are of legal age.")