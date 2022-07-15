
from this import s


weight = int(input("Enter the weight of your product:"))
choice = int(input("Choose your shipping option - 1 for Ground, 2 for Ground Premium, 3 for Drone:"))
#need to limit integer choices - range from 1-3

shipping_dict = {
    "Ground Shipping": ["ground_shipping"],
    "Ground Shipping Premium": ["ground_shipping_premium"],
    "Drone Shipping": ["drone_shipping"]
}

choice_1 = shipping_dict["Ground Shipping"]
choice_2 = shipping_dict["Ground Shipping Premium"]
choice_3 = shipping_dict["Drone Shipping"]


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
