from app import Database, Entry


def interactive_menu() -> None:
    """Run the interactive console menu for CRUD operations."""
    db = Database()
    while True:
        print("\nChoose an action:")
        print("1. Add entry")
        print("2. List entries")
        print("3. Get entry")
        print("4. Update entry")
        print("5. Delete entry")
        print("6. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            entry_id = db.add_entry(name, email)
            print(f"Added entry with id {entry_id}")
        elif choice == "2":
            entries = db.list_entries()
            for entry in entries:
                print(entry)
        elif choice == "3":
            entry_id = int(input("Entry id: "))
            entry = db.get_entry(entry_id)
            if entry:
                print(entry)
            else:
                print("Entry not found")
        elif choice == "4":
            entry_id = int(input("Entry id: "))
            name = input("New name: ")
            email = input("New email: ")
            db.update_entry(entry_id, name, email)
            print("Entry updated")
        elif choice == "5":
            entry_id = int(input("Entry id: "))
            db.delete_entry(entry_id)
            print("Entry deleted")
        elif choice == "6":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    interactive_menu()

