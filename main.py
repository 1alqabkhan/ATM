

class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__instruction()

    def __instruction(self):
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
        self.__pin = input("Create your 4 digit PIN: ")
        print("PIN generate successfully. ")
        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":
            self.__instruction()

    def deposit(self):
        if self.__pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.__pin:
                amount = int(input("Enter deposit amount : "))
                self.__balance = self.__balance + amount
                print("Deposit Successfully")
            else:
                print("Incorrect PIN.")
        else:
            print("Create your PIN First.")
            self.create_pin()

        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.__instruction()

    def withdraw(self):
        if self.__pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.__pin:
                amount = int(input("Enter withdrawal amount : "))
                if amount <= self.__balance:
                    self.__balance = self.__balance - amount
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

            self.__instruction()

    def check_balance(self):
        if self.__pin != "":
            pin = input("Enter your PIN : ")
            if pin == self.__pin:
                print(f"Your current balance is Rs. {self.__balance}.")
            else:
                print("Incorrect PIN. Try Again.")
        else:
            print("Create your PIN First.")
            self.create_pin()
        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.__instruction()

    def reset_pin(self):
        if self.__pin != "":
            self.__pin = input("Enter your new 4 digit reset PIN : ")
            print("PIN Reset successful.")
        else:
            print("Create your PIN First.")
            self.create_pin()
        enterbutton = input("Press enter to menu ->")
        if enterbutton == "":

            self.__instruction()


icici = Atm()

