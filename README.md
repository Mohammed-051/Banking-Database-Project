# Bank Management System

A comprehensive Oracle database project for managing banking operations, including customers, accounts, loans, credit cards, and audit trails.

## Project Structure

```
Banking-Database-Project/
├── sql/                          # Database DDL scripts
│   ├── 01_create_tables.sql      # Table definitions
│   ├── 02_create_indexes.sql     # Performance indexes
│   └── 03_create_audit.sql       # Audit trail & triggers
├── src/                          # Python source code
│   ├── main.py                   # CLI application
│   └── data_generator.py         # Test data generator
├── data/                         # Sample CSV data
│   ├── bank_data.csv
│   ├── customer_data.csv
│   ├── account_data.csv
│   └── ...
├── docs/                         # Documentation
│   ├── diagrams/                 # ER diagrams
│   └── legacy/                   # Original SQL drafts
├── requirements.txt              # Python dependencies
└── README.md
```

## Database Schema

### Entity Relationships

- **Bank** → has many → **Branch**
- **Branch** → has many → **Customer**
- **Customer** → has many → **Account**, **Loan**, **Credit_Card**, **Phone**
- **Account** → specializes into → **Saving** | **Current**
- **Employee** → manages → **Account** (via Account_Management)
- **Loan** → has many → **Payment**

### Tables

| Table | Description |
|-------|-------------|
| Bank | Financial institution details |
| Branch | Bank branch locations |
| Customer | Customer personal information |
| Customer_Phone | Multi-valued phone numbers |
| Employee | Bank staff records |
| Account | Customer accounts (Saving/Current) |
| Saving | Savings account with interest rate |
| Current | Current account with overdraft |
| Account_Management | Employee-Account assignments |
| Credit_Card | Customer credit cards |
| Loan | Customer loans |
| Payment | Loan payment records |
| Account_Audit | Balance change audit trail |

## Installation

### Prerequisites

- Oracle Database 11g or higher (or Oracle XE)
- Python 3.8+
- Oracle Instant Client

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
   cd bank-management-system
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create database schema**
   ```sql
   -- Run in SQL*Plus or SQL Developer
   @sql/01_create_tables.sql
   @sql/02_create_indexes.sql
   @sql/03_create_audit.sql
   ```

4. **Generate sample data** (optional)
   ```bash
   python src/data_generator.py
   ```

5. **Run the application**
   ```bash
   python src/main.py
   ```

## Usage

### CLI Application Features

```
====== Bank Management System ======
1. Add New Customer
2. Delete Customer
3. Update Customer Info
4. Join Customer with Account
5. Filter Customers (Advanced)
6. Check Customer Info
7. Exit
```

### Database Configuration

Update connection settings in `src/main.py`:
```python
cx_Oracle.connect("username", "password", "localhost:1521/XE")
```

## Features

- **CRUD Operations** - Create, Read, Update, Delete customers
- **Advanced Filtering** - Filter by city, name, DOB, state, zip code
- **Audit Trail** - Automatic logging of account balance changes
- **Data Generator** - Creates realistic test data using Faker

## Sample Data

The data generator creates:
- 5 Banks
- 10 Branches
- 200 Customers
- 400 Accounts
- 50 Employees
- 50 Loans
- 200 Payments
- 100 Credit Cards

## License

MIT License

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Open a Pull Request
