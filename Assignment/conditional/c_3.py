# Get marks as input from user and display grade.[>=90->A, >=80->B, >=70->C, >=60->D, <60->F]

marks=float(input("Enter your marks:"))

if marks>=90:
    print("You have Obtained grade A")
elif marks>=80:
    print("You have Obtained grade B")
elif marks>=70:
    print("You have Obtained grade C")
elif marks>=60:
    print("You have obtained grade D")
elif marks<60 and marks>10:
    print("You have Obtained grade F")
else:
    print("Marks cannot be neagtive")
    