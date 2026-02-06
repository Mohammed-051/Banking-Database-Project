-- Bank Management System - Audit Trail Setup
-- Tracks changes to account balances

-- Audit Table
CREATE TABLE Account_Audit (
    Audit_Id NUMBER PRIMARY KEY,
    Account_No VARCHAR2(15),
    Operation VARCHAR2(10),
    Old_Balance NUMBER(15,2),
    New_Balance NUMBER(15,2),
    Change_Date TIMESTAMP,
    Changed_By VARCHAR2(50),
    CONSTRAINT fk_audit_account FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);

-- Sequence for audit IDs
CREATE SEQUENCE audit_seq
    START WITH 1
    INCREMENT BY 1
    NOCACHE
    NOCYCLE;

-- Trigger for balance changes
CREATE OR REPLACE TRIGGER account_balance_change
AFTER UPDATE OF Account_Balance ON Account
FOR EACH ROW
BEGIN
    INSERT INTO Account_Audit (
        Audit_Id,
        Account_No,
        Operation,
        Old_Balance,
        New_Balance,
        Change_Date,
        Changed_By
    ) VALUES (
        audit_seq.NEXTVAL,
        :NEW.Account_No,
        'UPDATE',
        :OLD.Account_Balance,
        :NEW.Account_Balance,
        SYSTIMESTAMP,
        USER
    );
END;
/
