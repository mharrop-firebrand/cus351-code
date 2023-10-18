'''
Your task is to create a Python function that simulates basic bank account management. The function, named manage_balance, should accept three parameters:

balance (default value: 0) - The initial balance in the bank account.
deposit (default value: 0) - The amount to be deposited.
withdraw (default value: 0) - The amount to be withdrawn.
The function should perform the following operations:

Check if the deposit and withdraw amounts are non-negative. If either of them is negative, return the message: "Invalid deposit or withdraw amount. Please enter non-negative values."

Update the balance by adding the deposit amount.

Check if the updated balance is greater than or equal to the withdraw amount. If it is, subtract the withdraw amount from the balance.

If the updated balance is not sufficient to cover the withdraw amount, return the message: "Insufficient funds. Withdrawal amount exceeds the available balance."

Finally, return a message indicating the new balance: "Balance: £[new_balance]".

Example usage: 
print(manage_balance(balance=100, deposit=50, withdraw=30))


'''