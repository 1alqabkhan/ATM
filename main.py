

class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.instruction()

    def instruction(self):
        user_input = int(input("""
                Hello, How would you like to proceed?
                    1. Enter 1 to Create PIN.
                    2. Enter 2 to Deposit.
                    3. Enter 3 to Withdraw.
                    4. Enter 4 to Check Balance.
                    5. Enter 5 to reset PIN.
                    6. Enter 6 to Exit.
        """))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            self.reset_pin()
        else:
            print("Have a Good Day!")

    def create_pin(self):
        self.pin = input("Create your 4 digit PIN: ")
        print("PIN generate successfully. ")
        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":
            self.instruction()

    def deposit(self):
        if self.pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.pin:
                amount = int(input("Enter deposit amount : "))
                self.balance = self.balance + amount
                print("Deposit Successfully")
            else:
                print("Incorrect PIN.")
        else:
            print("Create your PIN First.")
            self.create_pin()

        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.instruction()

    def withdraw(self):
        if self.pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.pin:
                amount = int(input("Enter withdrawal amount : "))
                if amount <= self.balance:
                    self.balance = self.balance - amount
                    print("Withdrawal Succesfully")
                else:
                    print("Insufficient Balance.")
            else:
                print("Incorrect PIN.")
        else:
            print("Create your PIN First.")
            self.create_pin()

        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.instruction()

    def check_balance(self):
        if self.pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.pin:
                print(f"Your current balance is Rs. {self.balance}.")
            else:
                print("Incorrect PIN. Try Again.")
        else:
            print("Create your PIN First.")
            self.create_pin()
        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.instruction()

    def reset_pin(self):
        if self.pin != "":
            self.pin = input("Enter your new 4 digit reset PIN : ")
            print("PIN Reset successful.")
        else:
            print("Create your PIN First.")
            self.create_pin()


icici = Atm()
