-- Bank Management System - Index Creation Script
-- Performance optimization indexes

CREATE INDEX idx_customer_name ON Customer(Name);
CREATE INDEX idx_customer_email ON Customer(Email_Id);
CREATE INDEX idx_account_customer ON Account(Customer_Id);
CREATE INDEX idx_loan_customer ON Loan(Customer_Id);
CREATE INDEX idx_payment_loan ON Payment(Loan_No);
CREATE INDEX idx_branch_bank ON Branch(Bank_Code);
CREATE INDEX idx_credit_card_customer ON Credit_Card(Customer_Id);
