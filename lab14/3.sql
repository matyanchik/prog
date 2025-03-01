SELECT Accounts.account_id, Accounts.account_number, Accounts.balance, Clients.name
FROM Accounts
JOIN Clients ON Accounts.client_id = Clients.client_id;