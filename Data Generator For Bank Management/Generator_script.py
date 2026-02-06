import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker
faker = Faker()

# Set random seed for reproducibility
random.seed(42)
faker.seed_instance(42)

# Define the number of records for each entity
num_banks = 5
num_branches = 10
num_customers = 200
num_accounts = 400
num_employees = 50
num_loans = 50
num_payments = 200
num_credit_cards = 100
num_customer_phones = 250  # Some customers have multiple phone numbers

print("Starting data generation process...")

# Generate data for Bank table
print("Generating Bank data...")
banks = []
for _ in range(num_banks):
    banks.append({
        'Code': faker.unique.bban()[:10],
        'B_name': faker.company(),
        'City': faker.city(),
        'Address': faker.address()
    })
bank_df = pd.DataFrame(banks)

# Generate data for Branch table
print("Generating Branch data...")
branches = []
for _ in range(num_branches):
    branches.append({
        'Branch_Code': faker.unique.bban()[:10],
        'Branch_name': faker.company(),
        'Address': faker.address(),
        'Head_Office': faker.company(),
        'Branch_Details': faker.catch_phrase(),
        'City_Name': faker.city(),
        'Bank_Code': random.choice(bank_df['Code'])
    })
branch_df = pd.DataFrame(branches)

# Generate data for Customer table
print("Generating Customer data...")
customers = []
for _ in range(num_customers):
    f_name = faker.first_name()
    l_name = faker.last_name()
    customers.append({
        'Cust_Id': faker.unique.bban()[:10],
        'First_Name': f_name,
        'Last_Name': l_name,
        'Name': f_name + " " + l_name,
        'F_Name': f_name,  # Adding F_Name as mentioned in first ER diagram
        'L_Name': l_name,  # Adding L_Name as mentioned in first ER diagram
        'Birth_Date': faker.date_of_birth(minimum_age=18, maximum_age=80),
        'Street_Number': faker.building_number(),
        'Street_Name': faker.street_name(),
        'Unit': faker.secondary_address(),
        'City': faker.city(),
        'State': faker.state(),
        'Zip_Code': faker.zipcode(),
        'Email_Id': faker.email(),
        'Social_Security_Number': faker.ssn(),
        'Address': faker.address(),
        'Mobile_no': faker.phone_number(),
        'Branch_Code': random.choice(branch_df['Branch_Code'])
    })
customer_df = pd.DataFrame(customers)

# Generate data for Customer_Phone table
print("Generating Customer_Phone data...")
customer_phones = []
for _ in range(num_customer_phones):
    customer_id = random.choice(customer_df['Cust_Id'])
    customer_phones.append({
        'Phone_Number': faker.phone_number(),
        'Customer_Id': customer_id,
        'Phone_Type': random.choice(['Home', 'Work', 'Mobile', 'Other'])
    })
customer_phone_df = pd.DataFrame(customer_phones)

# Generate data for Account table
print("Generating Account data...")
accounts = []
for _ in range(num_accounts):
    account_type = random.choice(['Saving', 'Current'])
    accounts.append({
        'Account_No': faker.unique.bban()[:10],
        'Account_Balance': round(random.uniform(100, 100000), 2),
        'Account_Type': account_type,
        'Account_Type_Description': faker.catch_phrase(),
        'Customer_Id': random.choice(customer_df['Cust_Id'])
    })
account_df = pd.DataFrame(accounts)

# Generate data for specialized account types: Saving and Current
print("Generating Saving and Current Account data...")
saving_accounts = []
current_accounts = []

for _, account in account_df.iterrows():
    if account['Account_Type'] == 'Saving':
        saving_accounts.append({
            'Account_No': account['Account_No'],
            'Interest_Rate': round(random.uniform(0.5, 5.0), 2)
        })
    else:  # Current account
        current_accounts.append({
            'Account_No': account['Account_No'],
            'Overdraft_Limit': round(random.uniform(100, 10000), 2)
        })

saving_df = pd.DataFrame(saving_accounts)
current_df = pd.DataFrame(current_accounts)

# Generate data for Employee table
print("Generating Employee data...")
employees = []
for _ in range(num_employees):
    employees.append({
        'Emp_Id': faker.unique.bban()[:10],
        'Emp_name': faker.name(),
        'Mobile_no': faker.phone_number(),
        'Address': faker.address()
    })
employee_df = pd.DataFrame(employees)

# Generate data for Account Management relationship
print("Generating Account Management data...")
account_management = []
for _, account in account_df.iterrows():
    account_management.append({
        'Account_No': account['Account_No'],
        'Emp_Id': random.choice(employee_df['Emp_Id']),
        'Management_Date': faker.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d')
    })
account_management_df = pd.DataFrame(account_management)

# Generate data for Credit Card table
print("Generating Credit Card data...")
credit_cards = []
for _ in range(num_credit_cards):
    credit_cards.append({
        'Credit_Card_Number': faker.credit_card_number(card_type=None),
        'Credit_Limit': round(random.uniform(1000, 50000), 2),
        'Amount_Spent': round(random.uniform(0, 40000), 2),
        'Bill_Payment_Due_Date': faker.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
        'Minimum_Payment': round(random.uniform(50, 500), 2),
        'Customer_Id': random.choice(customer_df['Cust_Id'])
    })
credit_card_df = pd.DataFrame(credit_cards)

# Generate data for Loan table
print("Generating Loan data...")
loans = []
for _ in range(num_loans):
    loan_amount = round(random.uniform(1000, 100000), 2)
    loans.append({
        'Loan_No': faker.unique.bban()[:10],
        'Amount': loan_amount,  # Use 'Amount' as in first ER diagram
        'Loan_Amount': loan_amount,  # Use 'Loan_Amount' as in second ER diagram
        'Loan_Type': random.choice(['Personal', 'Home', 'Car', 'Education', 'Business']),
        'Loan_Duration_Months': random.randint(12, 240),
        'Interest_Rate': round(random.uniform(1, 15), 2),
        'Monthly_Payment_Due_Date': faker.date_between(start_date='today', end_date='+30d').strftime('%Y-%m-%d'),
        'Monthly_Minimum_Payment': round(loan_amount / random.randint(12, 60), 2),
        'Payment_Method': random.choice(['Online', 'Cash', 'Cheque', 'Auto-debit']),
        'Customer_Id': random.choice(customer_df['Cust_Id']),
        'Emp_Id': random.choice(employee_df['Emp_Id'])
    })
loan_df = pd.DataFrame(loans)

# Generate data for Payment table
print("Generating Payment data...")
payments = []
for _ in range(num_payments):
    loan = random.choice(loan_df['Loan_No'])
    payment_date = faker.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
    payment_amount = round(random.uniform(100, 5000), 2)
    payments.append({
        'Payment_No': faker.unique.bban()[:10],
        'Payment_Date': payment_date,
        'Payment_date': payment_date,  # Both column names are in the ER diagrams
        'Payment_Amount': payment_amount,
        'Payment_amount': payment_amount,  # Both column names are in the ER diagrams
        'Loan_No': loan
    })
payment_df = pd.DataFrame(payments)

# Display the number of records in each table
print("\nDataset Summary:")
print(f"Bank: {len(bank_df)} records")
print(f"Branch: {len(branch_df)} records")
print(f"Customer: {len(customer_df)} records")
print(f"Customer_Phone: {len(customer_phone_df)} records")
print(f"Account: {len(account_df)} records")
print(f"Saving Account: {len(saving_df)} records")
print(f"Current Account: {len(current_df)} records")
print(f"Employee: {len(employee_df)} records")
print(f"Account Management: {len(account_management_df)} records")
print(f"Credit Card: {len(credit_card_df)} records")
print(f"Loan: {len(loan_df)} records")
print(f"Payment: {len(payment_df)} records")

# Create a directory for the CSV files
if not os.path.exists('banking_data'):
    os.makedirs('banking_data')

# Save the data to CSV files
print("\nSaving data to CSV files...")
bank_df.to_csv('banking_data/bank_data.csv', index=False)
branch_df.to_csv('banking_data/branch_data.csv', index=False)
customer_df.to_csv('banking_data/customer_data.csv', index=False)
customer_phone_df.to_csv('banking_data/customer_phone_data.csv', index=False)
account_df.to_csv('banking_data/account_data.csv', index=False)
saving_df.to_csv('banking_data/saving_account_data.csv', index=False)
current_df.to_csv('banking_data/current_account_data.csv', index=False)
employee_df.to_csv('banking_data/employee_data.csv', index=False)
account_management_df.to_csv('banking_data/account_management_data.csv', index=False)
credit_card_df.to_csv('banking_data/credit_card_data.csv', index=False)
loan_df.to_csv('banking_data/loan_data.csv', index=False)
payment_df.to_csv('banking_data/payment_data.csv', index=False)

print("Data generation completed!")
