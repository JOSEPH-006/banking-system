name=input("Enter name " )
print("Good afternoon," + name)
pwd=input("Enter password" )
print("Welcome to equity banking services")

account = input("Enter email" )
print(account)
pwd = input("password")
initial_amount = 100000
if not pwd:
    print("password cannot be empty. Please enter password")
else:
    print("Login successfully")

account_balance = input( 1000)
min_withdrawal = input(100)
min_deposit = input( 50 )
jetbrains://pycharm/navigate/reference?project=ONE LOVE FAMILY&path=PycharmProjects/pythonProject/bank.py
withdrawal_amount = input("Enter the withdrawal amount: ")
if withdrawal_amount > account_balance:
        print("Insufficient funds. Withdrawal unsuccessful.")
elif withdrawal_amount < min_withdrawal:
        print("Withdrawal amount is less than the minimum required. Withdrawal unsuccessful.")
else:
    account_balance -= withdrawal_amount
    print("Withdrawal successful. Updated account balance: ${account_balance}")

    deposit_amount = input("Enter the deposit amount: ")
    if deposit_amount < min_deposit:
        print("Deposit amount is less than the minimum required. Deposit unsuccessful.")
    else:
        account_balance += deposit_amount
        print(f"Deposit successful. Updated account balance: ${account_balance}")

