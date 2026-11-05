# Exercise
# Write a program that allows the user to manage a phonebook using a dictionary array. Implement functionalities to;
# 1. Add contacts
# 2. Search for contacts
# 3. Display the phonebook
# 4. Delete a contact
# 5. Edit contact

phonebook = {}

while True:
    choice = input("\n1. Add contact  2. Search for a contact  3. Display  4. Delete  5. Edit contact  6. Exit: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        phonebook[name] = number

    elif choice == "2":
        name = input("Search name: ")
        if name in phonebook:
            print(name, ":", phonebook[name])
        else:
            print("Not found")

    elif choice == "3":
        for name in phonebook:
            print(name, ":", phonebook[name])


    elif choice == "4":
        name = input("Name to delete: ")

        if name in phonebook:
            del phonebook[name]
            print("Deleted")
        else:
            print("Not found")

    elif choice == "5":
        name = input("Name to edit: ")
        if name in phonebook:
            new_number = input("New number: ")
            phonebook[name] = new_number
            print("Updated")
        else:
            print("Not found")