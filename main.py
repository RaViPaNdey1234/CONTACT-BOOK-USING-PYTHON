contacts = {}

def add_contact(name, number):
    contacts[name] = number

def view_contacts():
    for name, number in contacts.items():
        print(f"Name: {name}, Number: {number}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter the contact name: ")
        number = input("Enter the contact number: ")
        add_contact(name, number)
        print(f"Contact '{name}' added.")
    elif choice == "2":
        print("Your contacts:")
        view_contacts()
    elif choice == "3":
        name = input("Enter the contact name to delete: ")
        delete_contact(name)
        print(f"Contact '{name}' deleted.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
