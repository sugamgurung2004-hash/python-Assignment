# Greet user based on time .Take time and name as input .5-11 =Good morning, 12-7=Good Afternoon, 18-20=Good Evening, 20-4=Good Night else display invalid time.[{Greeting},{user_name}]

name=input("Enter the name:").capitalize()
time = int(input("Enter time in 24-hour format (0-23): "))

if 5 <= time <= 11:
    greeting = "Good Morning"
elif 12 <= time <= 17:
    greeting = "Good Afternoon"
elif 18 <= time <= 20:
    greeting = "Good Evening"
elif (21 <= time <= 23) or (0 <= time <= 4):
    greeting = "Good Night"
else:
    greeting = "Invalid time"

print(f"[{greeting}, {name}]")
