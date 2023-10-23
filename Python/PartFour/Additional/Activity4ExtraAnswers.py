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


def calculate_account_balance(transactions):
    balance = 0
    for transaction in transactions:
        balance +- transaction
    return balance

# Sample list of transactions
transactions = [100.50, -50.25, 75.0, -30.75, 200.0]

# Call the calculate_account_balance function and pass the transactions list as an argument
balance = calculate_account_balance(transactions)

# Print the calculated balance
print(f"Account balance: ${balance:.2f}")


# Or
def calculate_account_balance2(transactions):
    try:
        balance = 0
        for transaction in transactions:
            # Attempt to add the transaction to the balance
            balance += transaction
    except (TypeError, ValueError) as e:
        print(f"An error occurred: {e}")
        balance = 0  # Set the balance to 0 in case of an error
    return balance


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

Return the with something like this (Want to see origional price, tax amount and new price): 
Purchase: £32.50 | Tax: £0.00 | Total: £32.50
Purchase: £20.50 | Tax: £0.00 | Total: £20.50
Purchase: £110.00 | Tax: £13.20 | Total: £123.20
Purchase: £46.00 | Tax: £0.00 | Total: £46.00
Purchase: £1065.00 | Tax: £127.80 | Total: £1192.80
Purchase: £178.25 | Tax: £21.39 | Total: £199.64
"""


def calculate_tax(transactions):
    results = []

    for transaction in transactions:
        if transaction > 100:
            tax_rate = 0.12  # 12% tax for purchases over £100
        else:
            tax_rate = 0  # 10% tax for purchases £100 or less

        tax = transaction * tax_rate
        total_with_tax = transaction + tax
        results.append((transaction, tax, total_with_tax))

    return results


transactions = [32.50, 20.50, 110, 46, 1065, 178.25]
results = calculate_tax(transactions)

for purchase, tax, total in results:
    print(f"Purchase: £{purchase:.2f} | Tax: £{tax:.2f} | Total: £{total:.2f}")







"""3)
Write a function to validate whether an account number is in the correct format for a banking app.(10 Character and all numbers)"""


def validate_account_number(account_number):
    if len(account_number) == 10 and account_number.isdigit():
        return True
    else:
        return False

print(validate_account_number('1234567891'))

"""4)
Create a Python function that calculates the interest earned on a savings account over a specified period.
For example
£1000 in savings
3.2% intrest
Over 5 years

Print out initial amount, interest earned and total after x number of years."""


def calculate_savings_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal_amount = 1000  # Initial amount in the savings account
annual_interest_rate = 3.2  # Annual interest rate (3.2%)
time_period = 5  # Number of years

# Call the function to calculate the interest
interest_earned = calculate_savings_interest(
    principal_amount, annual_interest_rate, time_period
)

# Calculate the final amount after interest
final_amount = principal_amount + interest_earned

print(f"Initial principal amount: ${principal_amount:.2f}")
print(f"Interest earned: ${interest_earned:.2f}")
print(f"Amount after {time_period} years: ${final_amount:.2f}")

"""5)
Write a function that determines whether a customer is eligible for a loan based on their credit score and income.
For example:
Credit score over 700 and annual income £20,000 and over eligible for a loan."""


def check_loan_eligibility(credit_score, annual_income):
    if credit_score >= 700 and annual_income >= 30000:
        return True
    else:
        return False


print(
    f"Am I eligible for a load with a credit score of 751 and an income of £30,000? {check_loan_eligibility(751, 30000)}."
)
