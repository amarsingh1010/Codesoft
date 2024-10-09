
contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter contact address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
    print("\n")

def search_contact():
    search = input("Enter contact name or phone number to search: ")
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['phone']:
            print(f"\nFound Contact - Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}\n")
            return
    print("Contact not found!")

def update_contact():
    name = input("Enter the contact name to update: ")
    if name in contacts:
        print("What would you like to update?")
        print("1. Phone Number")
        print("2. Email Address")
        print("3. Address")
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            new_phone = input("Enter new phone number: ")
            contacts[name]['phone'] = new_phone
            print(f"Phone number updated for {name}.")
        elif choice == '2':
            new_email = input("Enter new email address: ")
            contacts[name]['email'] = new_email
            print(f"Email updated for {name}.")
        elif choice == '3':
            new_address = input("Enter new address: ")
            contacts[name]['address'] = new_address
            print(f"Address updated for {name}.")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def contact_book_interface():
    while True:
        print("\nContact Book ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Visit Again")
            break
        else:
            print("oops! Please enter a number between 1 and 6.")


contact_book_interface()
