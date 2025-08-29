import art

phonebook = {
    "Аня": {
       "phone": "12345",
        "email" : ""
    }, 
    "Борис": {
       "phone": "67890", 
        "email" : ""
    }, 
}

programme_on = True

print(art.logo)


while programme_on:
    
    type = input('''Type 'Add'  ➕  to add a new contact
Type 'Find' 🔍  to search for a contact
Type 'All'  📋  to show all contacts
Type 'End'  ❌  to exit the programme \n''').lower()

    def add_number(new_person):
        name = input("Enter the name of the person: ")
        number = input(f"Enter the phone number of {name}:")
        email = input(f"Write email of {name} ")
        new_person[name] = {}
        new_person[name]["phone"] = number
        new_person[name]["email"] = email

        print(f"✅ Contact has been added successfully! {name} and phone number {number}")
        print("\n"*2)
    
    def find_number(the_person):
        name = input("Please enter the name you want to search:")
        if name in the_person:
             
            print(name," phone number: ",the_person[name]["phone"], "email:", the_person[name]["email"])
            print("\n"*10)
        else:
            print("❌ Sorry, this contact was not found.")
            print("\n"*10)

    def print_all_phonebook(user_phonebook):
        for name in user_phonebook:
            
            print(name," phone number: ",user_phonebook[name]["phone"], "email:", user_phonebook[name]["email"])
            



    if type == "add":
        print("\n"*5)
        print('''=== ➕ ADD NEW CONTACT ===''')
        add_number(phonebook)

    elif type == "find":
        print("\n"*5)
        print("=== 🔍 SEARCH CONTACT ===")
        find_number(phonebook)
    elif type == "all":
        print("\n"*5)
        print('''
    === 📋 ALL CONTACTS ===
Here are all saved contacts:
              ''')
        print_all_phonebook(phonebook)
        print("\n"*5)
    else:
        print('''
              === 👋 EXIT PROGRAM ===
Thank you for using My Phonebook App!
Goodbye! 
              
⚠️ Note: The program will not save your updated contacts after exit. ⚠️  
              ''')
        programme_on = False
    
    

