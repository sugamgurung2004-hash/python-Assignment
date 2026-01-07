# Get three fruit name and price from user and print in format[note: Align fruit name left with 12 spaces]

fruit_1 = input("Enter the fruit name: ")
price_1= float(input("Enter the price: "))
fruit_2=input("Enter the fruit name: ")
price_2=float(input("Enter the price: "))
fruit_3=input("Enter the fruit name: ")
price_3=float(input("Enter the price: "))

print("Item          |price")
print("_"*20)   
print(f"{fruit_1:12} |{price_1:.2f}")
print(f"{fruit_2:12} |{price_2:.2f}")
print(f"{fruit_3:12} |{price_3:.2f}")