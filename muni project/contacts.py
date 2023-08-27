class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

def save_contacts(contacts):
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(f"{contact.name},{contact.phone},{contact.email}\n")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, phone, email = line.strip().split(",")
                contacts.append(Contact(name, phone, email))
    except FileNotFoundError:
        pass
    return contacts

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append(Contact(name, phone, email))
    save_contacts(contacts)
    print("Contact added successfully!")

def view_all_contacts(contacts):
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

def search_contact(contacts):
    search_name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(contacts):
    search_name = input("Enter name of contact to update: ")
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
            break
    else:
        print("Contact not found.")

def delete_contact(contacts):
    search_name = input("Enter name of contact to delete: ")
    for contact in contacts:
        if contact.name.lower() == search_name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            break
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nPersonal Contact Manager")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_all_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()