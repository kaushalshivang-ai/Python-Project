contacts = []                        #empty contact dictionary

#To add contacts
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email id : ")
    contact = {"Name": name, "Phone No.": phone, "Email Id": email}
    contacts.append(contact)
    print("Contact added successfully")

#To view contacts
def view_contacts():
    if not contacts:
        print("No contacts found")
        return
    for index, contact in enumerate(contacts):
        print(f"{index + 1}. Name: {contact['Name']}, Phone: {contact['Phone No.']}, Email: {contact['Email Id']}")
    print()

#To search contacts
def search_contact():
    search_name = input("Enter the name to search: ")
    found = False
    for contact in contacts:
        if contact['Name'].lower() == search_name.lower():
            print(f"Name: {contact['Name']}, Phone: {contact['Phone No.']}, Email: {contact['Email Id']}")
            found = True
            break
    if not found:
        print("No contacts found")

#To delete contacts
def delete_contact():
    del_name = input("Enter the name to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == del_name.lower():
            contacts.remove(contact)
            print("Contact deleted")
            return
    print("No contact found")

def main():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid option. Try again.")
if __name__=="__main__":
    main()

