
def sequential():
  shipping_dict = {
      "Ground Shipping": ["ground_shipping"],
      "Ground Shipping Premium": ["ground_shipping_premium"],
      "Drone Shipping": ["drone_shipping"]
  }

  choice_1 = shipping_dict["Ground Shipping"]
  choice_2 = shipping_dict["Ground Shipping Premium"]
  choice_3 = shipping_dict["Drone Shipping"]

  print("To calculate the cost of your shipping, enter your item information below:")

  weight = int(input("Enter the weight of your product:"))

  while weight < 1:
    print("You must enter a viable weight.")
    weight = int(input("Enter the weight of your product:"))

  choice = int(input("Choose your shipping option - 1 for Ground, 2 for Ground Premium, 3 for Drone:"))

  while choice < 1 or choice > 3:
    print("You must choose a value between 1 and 3")
    choice = int(input("Choose your shipping option - 1 for Ground, 2 for Ground Premium, 3 for Drone:"))
    

  if choice == 1:
    choice_1
  elif choice == 2:
      choice_2
  elif choice == 3:
      choice_3

  if weight <= 2 and choice_1:
    print("Ground Price per Pound = $1.50 + Flat charge of $20. Total cost: " + str((weight * 1.5) + 20))
  elif weight > 2 and weight <= 6 and choice_1:
    print("Ground Price per Pound = $3.00 + Flat charge of $20. Total cost: " + str((weight * 3.0) + 20))
  elif weight > 6 and weight <= 10 and choice_1:
    print("Ground Price per Pound = $4.00 + Flat charge of $20. Total cost: " + str((weight * 4.0) + 20))
  elif weight > 10 and choice_1:
    print("Ground Price per Pound = $4.75 + Flat charge of $20. Total cost: " + str((weight * 4.75) + 20))
    #choice_2
  elif choice_2:
      print("Ground Shipping Premium has a flat charge of $125.00")
  #choice_3
  elif weight <= 2 and choice_3:
    print("Ground Price per Pound = $4.50, no flat charge. Total cost: " + str(weight * 4.5))
  elif weight > 2 and weight <= 6 and choice_3:
    print("Ground Price per Pound = $9.00, no flat charge. Total cost: " + str(weight * 9.0))
  elif weight > 6 and weight <= 10 and choice_3:
    print("Ground Price per Pound = $12.00, no flat charge. Total cost: " + str(weight * 12.0))
  elif weight > 10 and choice_3:
    print("Ground Price per Pound = $14.25, no flat charge. Total cost: " + str(weight * 14.25))

def all_options():
  weight = int(input("Enter the weight of your product:"))

  #Ground Shipping
  if weight <= 2:
    print("Ground Shipping: Ground Price per Pound = $1.50 + flat charge of $20. Total cost: $" + str((weight * 1.5) + 20))
  elif weight > 2 and weight <= 6:
    print("Ground Shipping: Ground Price per Pound = $3.00 + flat charge of $20. Total cost: $" + str((weight * 3.0) + 20))
  elif weight > 6 and weight <= 10:
    print("Ground Shipping: Ground Price per Pound = $4.00 + flat charge of $20. Total cost: $" + str((weight * 4.0) + 20))
  elif weight > 10:
    print("Ground Shipping: Ground Price per Pound = $4.75 + flat charge of $20. Total cost: $" + str((weight * 4.75) + 20))
    
  #Premium Ground
  premium_ground = 125.00
  print("Ground Shipping Premium: $", premium_ground)

  #Drone Shipping
  if weight <= 2:
    print("Ground Shipping: Ground Price per Pound = $4.50, no flat charge. Total cost: $" + str(weight * 4.5))
  elif weight > 2 and weight <= 6:
    print("Ground Shipping: Ground Price per Pound = $9.00, no flat charge. Total cost: $" + str(weight * 9.0))
  elif weight > 6 and weight <= 10:
    print("Ground Shipping: Ground Price per Pound = $12.00, no flat charge. Total cost: $" + str(weight * 12.0))
  elif weight > 10:
    print("Ground Shipping: Ground Price per Pound = $14.25, no flat charge. Total cost: $" + str(weight * 14.25))    



customer_choice = input("To calculate the exact cost of your chosen shipping method for your item, enter 'calculate'. To see the price of all different shipping methods for your item, enter 'all'.\n").lower()

while customer_choice != 'calculate' and customer_choice != 'all':
  print("Please enter a valid choice.")
  customer_choice = (input("To calculate the exact cost of your chosen shipping method for your item, enter 'Calculate'. To see the price of all different shipping methods for your item, enter 'All'.\n")).lower()

if customer_choice.lower() == "calculate":
  sequential()
elif customer_choice.lower() == "all":
  all_options()

