class Atm:
    def __init__(self):     # Constructor
        self.pin = 1234     # Given a default pin number
        self.balance = 0
        self.menu()         # Calling the menu function as we create the instance of Atm class

    def menu(self):
        user_input = input(
            """Hello, How would you like to proceed?
                       1. Enter 1 to create pin
                       2. Enter 2 to deposit
                       3. Enter 3 to withdraw
                       4. Enter 4 to check balance
                       5. Enter 5 to change pin
                       6. Enter 6 to exit
                       """
        )

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.change_pin()
        else:
            print("Bye")

    # PIN Generation function
    def create_pin(self):
        if self.pin == None:
            self.pin = int(input("Enter you PIN: "))
            print("Pin generation successful")
        else:
            print("Your already generated your new PIN")

    # Deposit function
    def deposit(self):
        temp = int(input("Enter your PIN: "))
        if temp == self.pin:
            amount = int(input("Enter Amount to deposit: "))
            self.balance = +amount
            print("Deposti Successful")
        else:
            print("Invalid PIN")

    # Withdraw function
    def withdraw(self):
        temp = int(input("Enter your PIN: "))
        if temp == self.pin:
            amount = int(input("Enter Amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw Successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    # Check Balance Function
    def check_balance(self):
        temp = int(input("Enter your pin: "))
        if temp == self.pin:
            print(f"Your have a balance of Rs.{self.balance}")
        else:
            print("Invalid pin")

    def change_pin(self):
        temp = int(input("Enter your PIN: "))
        if temp == self.pin:
            new_pin = int(input("Enter New PIN: "))
            self.pin = new_pin
        else:
            print("Invalid PIN")


hdfc = Atm()
