names = []
phones = []
emails = []
addresses = []

def add_con():
    x = int(input("Enter the number of contact you want to add:"))
    for i in range(x):
        name = input("Enter name :")
        try:
            phone = int(input("Enter phone number : "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        email = input("Enter email id :")
        address = input("Enter address : ")

        names.append(name)
        phones.append(phone)
        emails.append(email)
        addresses.append(address)

        print(f"CONTACT ADDED: {name}\t{phone}\t{email}\t\t{address}")

def display():
    if len(names) == 0:
        print("NO CONTACTS TO DISPLAY")
    else:
        for i in range(len(names)):
            print(f"NAME:{names[i]}\t PHONE:{phones[i]}\t EMAIL ID:{emails[i]}\t ADDRESS:{addresses[i]}")

def search_con():
    search = input("Enter search term:")
    if search in names:
        index = names.index(search)
        print(f"NAME:{names[index]}\t PHONE:{phones[index]}\t EMAIL ID:{emails[index]}\t ADDRESS:{addresses[index]}")
    else:
        print("CONTACT NOT FOUND")
        
def up_name(existing_name,new_name):
    if existing_name in names:
        index = names.index(existing_name)
        names[index] = new_name
        print("CONTACT NAME UPDATED SUCCESSFULLY")
    else:
        print("CONTACT NOT FOUND")

def up_phone(existing_num,new_num):
    try:
        existing_num = int(existing_num)
        new_num = int(new_num)
    except ValueError:
        print("Invalid input.Please enter numbers.")
        return
    print(f"DEBUG: Looking for existing phone {existing_num} in phones list {phones}")
    if existing_num in phones:
        index = phones.index(existing_num)
        phones[index] = new_num
        print("CONTACT NUMBER UPDATED SUCCESSFULLY")
    else:
        print("CONTACT NOT FOUND")

def up_email(existing_email,new_email):
    if existing_email in emails:
        index = emails.index(existing_email)
        emails[index] = new_email
        print("CONTACT EMAIL ID UPDATED SUCCESSFULLY")
    else:
        print("CONTACT NOT FOUND")

def up_address(existing_address,new_address):
    if existing_address in addresses:
        index = addresses.index(existing_address)
        addresses[index] = new_address
        print("CONTACT ADDRESS UPDATED SUCCESSFULLY")
    else:
        print("CONTACT NOT FOUND")
        
def del_con(name,phone):
    if name in names and phone in phones:
        index = names.index(name)
        if phones[index] == phone:
            del names[index]
            del phones[index]
            del emails[index]
            del addresses[index]
            print("CONTACT DELETED SUCCESSFULLY")
        else:
            print("PHONE NUMBER DOESN'T MATCH THE CONTACT NAME")
    else:
        print("CONTACT NOT FOUND")

ai = 'Y'
while ai.lower() == 'y' :

    print("""
          _______________________________

          CONTACTS:
          -------------------------------

          1. ADD NEW CONTACT

          2. VIEW CONTACT LIST

          3. SEARCH CONTACT

          4. UPDATE CONTACT NAME

          5. UPDATE CONTACT PHONE NUMBER

          6. UPDATE CONTACT EMAIL ID

          7. UPDATE CONTACT ADDRESS

          8. DELETE CONTACT

          9. EXIT
          _________________________________""")

    try:
        ch = int(input("ENTER THE NUMBER OF OPERATION YOU WANT TO DO :- "))
    except ValueError:
        print("Invalid input.Please enter a number between 1 and 9.")
        continue


    if ch == 1:
        add_con()

    elif ch == 2:
        print("DISPLAY CONTACTS")
        display()

    elif ch == 3:
        search_con()

    elif ch == 4:
        a = input("Enter existing contact name:")
        b = input("Enter new contact name:")
        up_name(a,b)

    elif ch == 5:
        try:
            c = input("Enter existing contact number:")
            d = input("Enter new contact number:")
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        up_phone(c,d)

    elif ch == 6:
        e = input("Enter existing contact email id:")
        f = input("Enter new contact email id:")
        up_email(e,f)

    elif ch == 7:
        g = input("Enter existing contact address:")
        h = input("Enter new contact address:")
        up_address(g,h)

    elif ch == 8:
        n = input("Enter contact name:")
        try:
            p = int(input("Enter phone number:"))
        except ValueError:
            print("Invalid input.Please enter number.")
            continue
        del_con(n,p)

    elif ch == 9:
        print("_____THANK____YOU______")
        break  

    else:
        print("Invalid input. Please enter a number between 1 and 9")

ai=input("DO YOU WANT TO RUN THE PROGRAM AGAIN PRESS Y/N : ")



