print("🏦 Welcome to Simple Bank System")
print("Type the number to choose an action:\n")

balance = 0
running = True

while running:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"💰 Current Balance: ${balance}\n")

    elif choice == "2":
        amount = input("Enter amount to deposit: ")
        if amount.isdigit():
            balance += int(amount)
            print(f"✅ Deposited ${amount}. New Balance: ${balance}\n")
        else:
            print("❌ Invalid amount.\n")

    elif choice == "3":
        amount = input("Enter amount to withdraw: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > balance:
                print("❌ Insufficient funds.\n")
            else:
                balance -= amount
                print(f"✅ Withdrawn ${amount}. New Balance: ${balance}\n")
        else:
            print("❌ Invalid amount.\n")

    elif choice == "4":
        print("👋 Thank you for using Simple Bank. Goodbye!")
        running = False
        

    else:
        print("❌ Invalid choice. Please select 1-4.\n")
