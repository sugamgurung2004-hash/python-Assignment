#A firm deposited amount Rs.5000000 in bank at interest 7.5% p.a. calculate amount retutned at end of 3monnth .

principal =int(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter the time: "))/12

interest=(principal * time * rate )/ 100
amount=principal + interest

print("Interest earned in 3 months:", interest)
print("Total amount returned after 3 months:", amount)