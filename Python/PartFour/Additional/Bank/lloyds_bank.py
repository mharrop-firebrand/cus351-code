def manage_balance(balance=0, deposit=0, withdraw=0):
    if deposit < 0 or withdraw < 0:
        return "Invalid deposit or withdraw amount. Please enter non-negative values."

    balance += deposit
    if balance >= withdraw:
        balance -= withdraw
        return f"Balance: £{balance}"
    else:
        return "Insufficient funds. Withdrawal amount exceeds the available balance."

# Function Call
print(manage_balance(balance=100, deposit=50, withdraw=30))