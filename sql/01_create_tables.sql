-- Bank Management System - Table Creation Script
-- Oracle Database DDL

-- Bank Table
CREATE TABLE Bank (
    Code VARCHAR2(10) PRIMARY KEY,
    B_name VARCHAR2(100) NOT NULL,
    City VARCHAR2(50) NOT NULL,
    Address VARCHAR2(200)
);

-- Branch Table
CREATE TABLE Branch (
    Branch_Code VARCHAR2(10) PRIMARY KEY,
    Branch_name VARCHAR2(100) NOT NULL,
    Address VARCHAR2(200),
    Head_Office VARCHAR2(100),
    Branch_Details VARCHAR2(200),
    City_Name VARCHAR2(50),
    Bank_Code VARCHAR2(10),
    CONSTRAINT fk_branch_bank FOREIGN KEY (Bank_Code) REFERENCES Bank(Code)
);

-- Customer Table
CREATE TABLE Customer (
    Cust_Id VARCHAR2(10) PRIMARY KEY,
    First_Name VARCHAR2(50),
    Last_Name VARCHAR2(50),
    Name VARCHAR2(100),
    Birth_Date DATE,
    Street_Number VARCHAR2(20),
    Street_Name VARCHAR2(100),
    Unit VARCHAR2(20),
    City VARCHAR2(50),
    State VARCHAR2(30),
    Zip_Code VARCHAR2(10),
    Email_Id VARCHAR2(100),
    Social_Security_Number VARCHAR2(20),
    Address VARCHAR2(200),
    Branch_Code VARCHAR2(10),
    CONSTRAINT fk_customer_branch FOREIGN KEY (Branch_Code) REFERENCES Branch(Branch_Code)
);

-- Customer Phone Table
CREATE TABLE Customer_Phone (
    Phone_Number VARCHAR2(20),
    Customer_Id VARCHAR2(10),
    Phone_Type VARCHAR2(20),
    PRIMARY KEY (Phone_Number, Customer_Id),
    CONSTRAINT fk_cusphone_customer FOREIGN KEY (Customer_Id) REFERENCES Customer(Cust_Id)
);

-- Employee Table
CREATE TABLE Employee (
    Emp_Id VARCHAR2(10) PRIMARY KEY,
    Emp_name VARCHAR2(100) NOT NULL,
    Mobile_no VARCHAR2(20),
    Address VARCHAR2(200)
);

-- Account Table
CREATE TABLE Account (
    Account_No VARCHAR2(15) PRIMARY KEY,
    Account_Balance NUMBER(15,2) NOT NULL,
    Account_Type VARCHAR2(20),
    Account_Type_Description VARCHAR2(200),
    Customer_Id VARCHAR2(10),
    CONSTRAINT fk_account_customer FOREIGN KEY (Customer_Id) REFERENCES Customer(Cust_Id)
);

-- Saving Account Table (extends Account)
CREATE TABLE Saving (
    Account_No VARCHAR2(15) PRIMARY KEY,
    Interest_Rate NUMBER(5,2),
    CONSTRAINT fk_saving_account FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);

-- Current Account Table (extends Account)
CREATE TABLE Current (
    Account_No VARCHAR2(15) PRIMARY KEY,
    Overdraft_Limit NUMBER(12,2),
    CONSTRAINT fk_current_account FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);

-- Account Management Table (Employee-Account relationship)
CREATE TABLE Account_Management (
    Account_No VARCHAR2(15),
    Emp_Id VARCHAR2(10),
    Management_Date DATE,
    PRIMARY KEY (Account_No, Emp_Id),
    CONSTRAINT fk_mngmt_account FOREIGN KEY (Account_No) REFERENCES Account(Account_No),
    CONSTRAINT fk_mngmt_employee FOREIGN KEY (Emp_Id) REFERENCES Employee(Emp_Id)
);

-- Credit Card Table
CREATE TABLE Credit_Card (
    Credit_Card_Number VARCHAR2(20) PRIMARY KEY,
    Credit_Limit NUMBER(12,2),
    Amount_Spent NUMBER(12,2),
    Bill_Payment_Due_Date DATE,
    Minimum_Payment NUMBER(12,2),
    Customer_Id VARCHAR2(10),
    CONSTRAINT fk_card_customer FOREIGN KEY (Customer_Id) REFERENCES Customer(Cust_Id)
);

-- Loan Table
CREATE TABLE Loan (
    Loan_No VARCHAR2(15) PRIMARY KEY,
    Loan_Amount NUMBER(15,2) NOT NULL,
    Loan_Type VARCHAR2(50),
    Loan_Duration_Months NUMBER(4),
    Interest_Rate NUMBER(5,2),
    Monthly_Payment_Due_Date DATE,
    Monthly_Minimum_Payment NUMBER(12,2),
    Payment_Method VARCHAR2(30),
    Customer_Id VARCHAR2(10),
    Emp_Id VARCHAR2(10),
    CONSTRAINT fk_loan_customer FOREIGN KEY (Customer_Id) REFERENCES Customer(Cust_Id),
    CONSTRAINT fk_loan_employee FOREIGN KEY (Emp_Id) REFERENCES Employee(Emp_Id)
);

-- Payment Table
CREATE TABLE Payment (
    Payment_No VARCHAR2(15) PRIMARY KEY,
    Payment_Date DATE NOT NULL,
    Payment_Amount NUMBER(12,2) NOT NULL,
    Loan_No VARCHAR2(15),
    CONSTRAINT fk_payment_loan FOREIGN KEY (Loan_No) REFERENCES Loan(Loan_No)
);
