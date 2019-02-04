firstname = input("enter first name: ")
lastname = input("enter last name : ")
age = int(input("enter your age: "))

Id = (firstname + " " + lastname)
a = len(Id)

if age >= 11: 
  print(Id)
  print(age)
  if a >= 15:
    print("Your id will be printed: " + lastname + " " + firstname[0])
  else:
    print("Your id will be printed: " + Id)
else:
  print("You are too young to go to the dance. ")
  
