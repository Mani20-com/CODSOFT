contacts = []
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()
def search_contact():
    query = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if query == contact['name'] or query == contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            print("Leave blank to keep current value.")
            contact['phone'] = input(f"New phone (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"New email (current: {contact['email']}): ") or contact['email']
            contact['address'] = input(f"New address (current: {contact['address']}): ") or contact['address']
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")
def main():
    while True:
        print("=== Contact Book Menu ===")
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
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")
main()
