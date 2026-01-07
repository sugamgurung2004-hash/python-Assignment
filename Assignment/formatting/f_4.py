# Take input of year,month and day and print full date in format: Data:YYYY/MM/DD

year=int(input("enter the year: "))
month=int(input("enter the month: "))
day=int(input("enter the day: "))
print(f"{year}/{month:0>2}/{day:0>2}")
