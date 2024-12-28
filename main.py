"""Class based banking system project"""
import json
class Transaction:
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note
    
    def display_info(self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note:{self.note}"

class Bank:
    def __init__(self):
        self.walllet = []

    #Add
    def add_transaction(self, transaction):
        self.walllet.append(transaction)

    #Remove
    def del_transaction(self, title):
        for trans in self.walllet:
            if trans.title == title:
                self.walllet.remove(trans)
                return f"{title} has been removed"
        return f"{title} is not found"
    
    #Display all
    def display(self):
        if not self.walllet:
            return f"No transactions available in your wallet."
        return f"\n".join([Transaction.display_info() for transaction in self.walllet])
    
    #Search
    def search_wallet(self, query):
        found = [trans for trans in self.walllet if query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return f"No transactions!"
        return "\n".join([Transaction.display_info() for transaction in found])
    
    #Save
    def save_file(self, filename="wallet.json"):
        data = [{'Expense': Transaction.title, 'Amount': Transaction.amount, 'Type': Transaction.type, 'Note': Transaction.note} 
                for transaction in self.walllet]
        with open(filename, "w") as file:
            json.dump(data, file)

    #Load
    def load_file(self, filename="wallet.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.walllet = [Transaction(trans['title'], trans['amount'], trans['type'], trans['note'])
                                for trans in data]
        except FileNotFoundError:
            print("We don't have that file...")
                





def main():
    wallet = Bank()
    while True:
        print("\n ======== Personal Banking System ====")
        print("1. Add a Transaction")
        print("2. Remove a transaction")
        print("3. Display all transactions")
        print("4. Search for a transaction")
        print("5. Save transaction file")
        print("6. Load transaction from file")
        print("7. Exit")
        choice = input("Enter your choice (1-7)")

        if choice == "1":
            title = input("Enter the title:")
            amount = float(input("Enter amount:"))
            type = input("Expense or deposit:")
            transaction = Transaction(title,amount, type)
            wallet.add_transaction
            print(f"{title} added successfully!")

        elif choice == "2":
            title = input("Enter the title:")
            print(wallet.del_transaction(title))

        elif choice == "3":
            print(wallet.display())

        elif choice == "4":
            query = input("Enter the title:")
            print(wallet.search_wallet(query))

        elif choice == "5":
            wallet.save_file()
            print("Saved as JSON")

        elif choice == "6":
            wallet.load_file()
            print("Loaded JSON")

        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")




if __name__ in "__main__":
    main()