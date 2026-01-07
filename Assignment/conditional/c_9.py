# Store customer balance in variable . Get input of amount to withdraw as input.If withdraw amount is less than total balance display ,123 withdraw as input .If withdraw amount is less than total balance display,123 withdraw successfully .New balance:456. if balance isn't sufficient display .Insufficent balance.

total_balance=10000
withdraw_amount=float(input("Enter withdraw amount:"))


if total_balance >= withdraw_amount:
    current_blc = total_balance - withdraw_amount
    print(f"You have withdraw {withdraw_amount} amount")
    print(f"Your current balance is: {current_blc}")

else:
    print("Your balance is Insufficient")
