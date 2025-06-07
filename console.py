import os

from database import Database

# ANSI color codes for a slightly nicer looking menu
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"

BANNER = (
    f"{BOLD}{CYAN}==============================\n"
    f"   CRUDex Interactive Menu\n"
    f"=============================={RESET}"
)


def interactive_menu() -> None:
    """Run the interactive console menu for CRUD operations."""
    with Database() as db:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(BANNER)
            print(f"{GREEN}1{RESET}. Add entry")
            print(f"{GREEN}2{RESET}. List entries")
            print(f"{GREEN}3{RESET}. Get entry")
            print(f"{GREEN}4{RESET}. Update entry")
            print(f"{GREEN}5{RESET}. Delete entry")
            print(f"{GREEN}6{RESET}. Exit")
            choice = input(f"{YELLOW}Select an option: {RESET}")
            if choice == "1":
                name = input("Name: ")
                email = input("Email: ")
                try:
                    entry_id = db.add_entry(name, email)
                    print(f"{MAGENTA}Added entry with id {entry_id}{RESET}")
                except ValueError as exc:
                    print(f"Error: {exc}")
                input("Press Enter to continue...")
            elif choice == "2":
                entries = db.list_entries()
                for entry in entries:
                    print(entry)
                input("Press Enter to continue...")
            elif choice == "3":
                entry_id = int(input("Entry id: "))
                entry = db.get_entry(entry_id)
                if entry:
                    print(entry)
                else:
                    print("Entry not found")
                input("Press Enter to continue...")
            elif choice == "4":
                entry_id = int(input("Entry id: "))
                name = input("New name: ")
                email = input("New email: ")
                try:
                    db.update_entry(entry_id, name, email)
                    print("Entry updated")
                except ValueError as exc:
                    print(f"Error: {exc}")
                input("Press Enter to continue...")
            elif choice == "5":
                entry_id = int(input("Entry id: "))
                try:
                    db.delete_entry(entry_id)
                    print("Entry deleted")
                except ValueError as exc:
                    print(f"Error: {exc}")
                input("Press Enter to continue...")
            elif choice == "6":
                print(f"{MAGENTA}Goodbye!{RESET}")
                break
            else:
                print("Invalid option")
                input("Press Enter to continue...")


if __name__ == "__main__":
    interactive_menu()
