class BankAccount:
    def __init__(self, accNumber, owner_name, net_balance, pincode):
        self.accountNumber = accNumber
        self.name = owner_name
        self.balance = net_balance
        self.pin = pincode

    @staticmethod
    def create(accountNum, holder_name, balance_deposited, password):
        obj = BankAccount(accountNum, holder_name, balance_deposited, password)
        ls.append(obj)
        print("Account with account_number " + str(accountNum) + " is created successfully.")
        # print("your account number is " + str(accountNum))

    def deposit(self, amount_deposited):
        print("Earlier balance: " + str(self.balance))
        self.balance = self.balance + amount_deposited
        print("Current balance: " + str(self.balance))
        print("\n")

    def withdraw(self, amount_deposited):
        print("Earlier balance: " + str(self.balance))
        if self.balance < amount_deposited:
            print('Not enough balance!')
        else:
            self.balance -= amount
        print("Current balance: " + str(self.balance))

    def getBalance(self):
        return self.balance

    def display(self):
        print("Account_Number : ", self.accountNumber)
        print("Name : ", self.name)
        print("Net_Balance : ", self.balance)
        print("\n")

    def delete(self):
        ls.remove(self)
        print("Deletion Successful..")


ls = []
if len(ls) == 0:
    print("No accounts are there. Start with create new account.. ")
else:
    print("Choose any action.")
while 1:
    print("0. Hit 0 to exit")
    print("1. Create Account")
    print("2. Deposit")
    print("3. WithDraw")
    print("4. GetBalance")
    print("5. Display detailed_list of all Accounts")
    print("6. Delete Account")
    print("\n")
    choice = int(input("Enter your choice: "))  # taking user choice
    print("\n")
    # if user choose to exist
    if choice == 0:
        break

    # if user choose to create account
    elif choice == 1:
        a_no = len(ls) + 1
        name = input("Enter name of Account_Holder: ")
        balance = int(input("Enter Deposited Balance: "))
        print("Your Account_Number is " + str(a_no) + ".")
        acc_numb = int(input("Enter Your Account_Number: "))
        pin = int(input("Enter pin for your Account: "))
        BankAccount.create(acc_numb, name, balance, pin)

    # if user choose to deposit amount in existing account
    elif choice == 2:
        account_id = int(input("Enter your Account_Number: "))
        for i in ls:
            if i.accountNumber == account_id:
                safety_pin = int(input("Enter yor pin: "))
                if i.pin == safety_pin:
                    amount = int(input("Enter balance to deposit: "))
                    i.deposit(amount)
                    break
                else:
                    print("Incorrect Pin..")
                    break
        else:
            print("Account not Found..")

    # if user choose to withdraw an amount from an existing account
    elif choice == 3:
        account_id = int(input("Enter your Account_Number: "))
        for i in ls:
            if i.accountNumber == account_id:
                safety_pin = int(input("Enter yor pin: "))
                if i.pin == safety_pin:
                    amount = int(input("Enter balance to deposit: "))
                    i.withdraw(amount)
                    break
                else:
                    print("Incorrect Pin..")
                    break
        else:
            print("Account not Found..")

    # if user choose to look for the balance of an existing account
    elif choice == 4:
        account_id = int(input("Enter your Account_Number: "))
        for i in ls:
            if i.accountNumber == account_id:
                safety_pin = int(input("Enter yor pin: "))
                if i.pin == safety_pin:
                    i.getBalance()
                    break
                else:
                    print("Incorrect Pin..")
                    break
        else:
            print("Account not Found..")

    # if user choose to display detailed_list of all account
    elif choice == 5:
        for i in ls:
            i.display()

    # if user choose to delete a account
    elif choice == 6:
        account_id = int(input("Enter your Account_Number: "))
        for i in ls:
            if i.accountNumber == account_id:
                safety_pin = int(input("Enter yor pin: "))
                if i.pin == safety_pin:
                    print("Do you really want to delete your Account?")
                    print("1. Press Y for yes.")
                    print("2. Press N for no.")
                    confirmation = input()
                    if confirmation == "Y" or confirmation == "y":
                        i.delete()
                        break
                    else:
                        break
                else:
                    print("Incorrect Pin..")
                    break
        else:
            print("Account not Found..")
            