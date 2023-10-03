""" Author: Rawan Khaled """

class ATM_Function:
    def __init__(self):
        self.Transaction_history = {"Balance": 0, "Withdrawn": 0, "Transferred": 0,"Transferred_to": 0, "Deposited": 0}

    def set_amounts_deposit(self, Amount):
        self.Transaction_history["Deposited"] += Amount
        self.Transaction_history["Balance"] += Amount
        print(f"Deposit is successful. You added {Amount} to your balance")

    def set_amounts_withdraw(self, Amount):
        if Amount <= self.Transaction_history["Balance"]:
            self.Transaction_history["Withdrawn"] += Amount
            self.Transaction_history["Balance"] -= Amount
            print(f"Withdrawal is successful. You took {Amount} from your balance")
        else:
            print("Insufficient balance for withdrawal.")

    def set_amounts_transfer(self, Amount):
        if Amount <= self.Transaction_history["Balance"]:
            self.Transaction_history["Transferred"] += Amount
            self.Transaction_history["Balance"] -= Amount
            print(f"Transfer is successful. You removed {Amount} from your balance")
        else:
            print("Insufficient balance for transfer.")

    def set_amounts_transfer_to_me(self, Amount):
        self.Transaction_history["Transferred_to"] += Amount
        self.Transaction_history["Balance"] += Amount

    def show_transactions(self):
        print("Here is your transaction history")
        print(self.Transaction_history)

    def quit(self):
        print("Thanks for using our ATM_SIMULATOR, Goodbye!")


def main(people):
    choice=0
    bool= True
    print("Welcome to this Python Based ATM_SIMULATOR")
    while bool:
        ID = input("Please, Enter your ID, it should be unique: ")
        # Check if the ID contains at least one digit
        if not any(char.isdigit() for char in ID):
            print("ID should contain at least one digit. Try a new ID.")
        else:
            bool=False

    # Check if the ID already exists in the dictionary
    if ID not in people:
        PIN = input("Please, Enter your PIN: ")
        people[ID] = {
            "PIN": PIN,
            "ATM": ATM_Function()  # Create a new ATM instance for each user
        }
        print("New user registered successfully!")
    else:
        print("Authentication successful!")

    atm = people[ID]["ATM"]  # Retrieve the user's ATM_Function instance
    while (choice != 5):
        print("What do you want to do now: ")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Transfer money")
        print("4. Show transactions")
        print("5. Quit")

        choice = int(input("Please, choose one: "))

        if choice == 1:
            amount = int(input("Enter the amount to deposit: "))
            atm.set_amounts_deposit(amount)

        elif choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            atm.set_amounts_withdraw(amount)

        elif choice == 3:
            amount = int(input("Enter the amount to transfer: "))
            target_id = input("Enter the ID to transfer the money to: ")
            if target_id in people:
                if ID != target_id:
                    atm.set_amounts_transfer(amount)
                    people[target_id]["ATM"].set_amounts_transfer_to_me(amount)
                else:
                    print("You can't transfer money to yourself.")
            else:
                print("Invalid target ID.")

        elif choice == 4:
            atm.show_transactions()

        elif choice==5:
            atm.quit()

        else:
            print("Invalid choice. Please choose a valid option.")



if __name__ == "__main__":
    people = {}  # Dictionary to store ID and associated ATM_Function instance
    while True:
        try:
            main(people)
        except KeyboardInterrupt:
            print("\nExiting...!")
            break

