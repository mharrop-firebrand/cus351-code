"""1)
Create a Python function that calculates the account balance for a list of transactions in a banking app.
Transactions:
£50
£40
£109
£60.3
= Total

Extra: Add exception handling.
"""
# list of transactions
# balance
# loop over the list
# take each transaction away from the balance


def balance(transaction_list, balance2=0):
    try:
        for transaction in transaction_list:
            balance2 -= transaction
        return f"{balance2:.2f}"
    except (TypeError, ValueError) as e:
        print(f"An Error occurred: {e}")


# all_transaction = [100, 45.50, 12.75, 38.45, 90]
# my_balance = 500
# remaining = balance(all_transaction, my_balance)
# print(f"Original balance: £{my_balance:.2f}\nRemaining balance: £{remaining}")


# or
def balance2(transaction_list):
    balance = 500
    for transaction in transaction_list:
        balance -= transaction
    return balance


# all_transaction = [100, 45.50, 12.75, 38.45, 90]
# print(f"Another Remaining balance: £{balance2(all_transaction):.2f}")


"""2)
Create a Python function that calculates the a 12% tax on purchases in a list over £100.
Example:
Transactions:
£32.50
£20.50
£110
£46
£1065
£178.25

Only these will be taxed 12%:
£110: Tax: £13.20 | Total: £123.20
£1065: Tax: £127.80 | Total: £1192.80
£178.25: | Tax: £21.39 | Total: £199.64

Return the with something like this (Want to see original price, tax amount and new price): 
Purchase: £32.50 | Tax: £0.00 | Total: £32.50
Purchase: £20.50 | Tax: £0.00 | Total: £20.50
Purchase: £110.00 | Tax: £13.20 | Total: £123.20
Purchase: £46.00 | Tax: £0.00 | Total: £46.00
Purchase: £1065.00 | Tax: £127.80 | Total: £1192.80
Purchase: £178.25 | Tax: £21.39 | Total: £199.64
"""
# List of transactions
# Each transaction over 100
# The value of 12% on each over 100 transaction
# The new price with the 12% added
# Return before tax, tax and after tax


def tax_calculator(purchases):
    result = []
    for purchase in purchases:
        if purchase > 100:
            tax_rate = 0.12
        else:
            tax_rate = 0

        tax = purchase * tax_rate
        total_with_tax = purchase + tax
        result.append((purchase, tax, total_with_tax))

    return result


purchases = [32.5, 110, 46, 1065, 178.25]
results = tax_calculator(purchases)  # [[]]

for purchase, tax, total_with_tax in results:
    print(f"Purchase: £{purchase:.2f} | Tax: £{tax:.2f} | Total: £{total_with_tax:.2f}")

# for i in results:
#     print(results)


"""3)
Write a function to validate whether an account number is in the correct format for a banking app.(10 Character and all numbers)"""
# len() == 10
# .isdigit or .isnumeric reutrns true or false


def validate_account_num(account_num):
    if len(account_num) == 10 and account_num.isnumeric():
        return True
    else:
        return False


print(validate_account_num("1234567891"))
print(validate_account_num("123456789"))
print(validate_account_num("123456789f"))


"""4)
Create a Python function that calculates the interest earned on a savings account over a specified period.
For example
£1000 in savings
3.2% intrest
Over 5 years

Print out initial amount, interest earned and total after x number of years."""

"""5)
Write a function that determines whether a customer is eligible for a loan based on their credit score and income.
For example:
Credit score over 700 and annual income £20,000 and over eligible for a loan."""
