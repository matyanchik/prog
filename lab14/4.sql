SELECT Transactions.transaction_id, Transactions.transaction_date, Transactions.amount, Transactions.transaction_type, Accounts.account_number, Clients.name
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id
JOIN Clients ON Accounts.client_id = Clients.client_id;