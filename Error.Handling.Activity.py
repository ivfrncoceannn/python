def check_balance(balance):
    print(f"\n Current balance: ₱{balance:.2f}\n")


def withdraw_money(balance):
    while True:
        try:
            amount = float(input("Enter amount to withdraw: ₱"))

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.\n")
                continue

            if amount > balance:
                print("\n Insufficient funds!")
                print("1. Exit program")
                print("2. Check current balance")
                print("3. Re-enter withdrawal amount")

                choice = input("Choose an option (1-3): ")

                if choice == "1":
                    print("Program exited.")
                    return balance, False
                elif choice == "2":
                    check_balance(balance)
                elif choice == "3":
                    continue
                else:
                    print("Invalid choice. Pls Try again.\n")

            else:
                balance -= amount
                print(f"Withdrawal successful! Remaining balance: ₱{balance:.2f}\n")
                return balance, True

        except ValueError:
            print("Invalid input! Please enter numbers only.\n")

        finally:
            print("Transaction attempt finished.\n")


def main():
    balance = 1000.00
    print("Welcome to the Simple Money Withdrawal System\n")

    while True:
        print("Menu:")
        print("1. Withdraw Money")
        print("2. Check Balance")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            balance, continue_program = withdraw_money(balance)
            if not continue_program:
                break
        elif choice == "2":
            check_balance(balance)
        elif choice == "3":
            print("Thank you for using my system.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")


#i-run ang program
main()