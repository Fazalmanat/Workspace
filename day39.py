class BankAccount:
    def __init__(self): 
        self.balance=0
        self.__pin=0000 
    def add_to_account(self):
        amount = int(input("Enter Amount to add: "))
        self.balance+=amount
        print("Amount Added Successfully")
    def show_balance(self):
        print("\nBalance: ",self.balance)
        
    def withdraw(self):
        amount = int(input("Enter amount to withdraw : "))
        if amount<=self.balance:
            self.balance-=amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")
    def check_pin(self):
        pin = int(input("Enter pin: "))
        if pin==self.__pin:
            return 1
        else:
            print("Wrong Pin Entered!!")
            return False
    def change_pin(self):
        new_pin=int(input("Enter new Pin : "))
        if new_pin//10000!=0:
            print("pin number should be 4 numbers!!")
            self.change_pin()
        else:
            confirm_pin=int(input("Confirm New Pin : "))
            if confirm_pin!=new_pin:
                print("Confirm Pin Doesn't match")
                self.change_pin()
            else:
                self.__pin=new_pin
                print("Pin Changed Successfully")
bact = BankAccount()
while True:
            print("\n===== Bank =====")
            print("1. Add Money")
            print("2. Show Balance")
            print("3. Withdraw Money")
            print("4. Change Pin")
            print("5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                if bact.check_pin():
                    bact.add_to_account()
            elif choice == 2:
                if bact.check_pin():
                    bact.show_balance()
            elif choice == 3:
                if bact.check_pin():
                    bact.withdraw()
            elif choice == 4:
                if bact.check_pin():
                    bact.change_pin()
            elif choice == 5:
                print("Thank you")
                break
            else:
                print("Invalid choice")