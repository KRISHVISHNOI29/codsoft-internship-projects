contacts = {}

def addcontact():
    name = input("enter the name to add-> ")
    no = input("enter the number to add-> ")
    contacts[name] = {'phone' : no}
    print(f"contact {name} added successfully")

def searchcontact():
    name = input("enter the name to search-> ")
    if name in contacts:
        print(f"Name : {name}")
        print(f"Phone : {contacts[name]['phone']}")
    else:
        print("contact not found")

def updatecontact():
    name = input("enter the name of contact to update")
    if name in contacts:
        new_num = input("enter the new number to be updated-> ")
        contacts[name] = {'phone' : new_num}
        print(f"contact {name} updated successfully!!!!!")
    else:
        print("contact not found")
        
def deletecontact():
    name = input("enter the name of contact to be deleted-> ")
    if name in contacts:
        del contacts[name]
        print(f"contact {name} deleted successfully!!!!!")
    else:
        print("contact not found")

def showallcontact():
    if contacts:
        for name in contacts.items():
            print(f"NAME : {name}, PHONE : {contacts[name]['phone']}")
    else:
        print("contact not found")
    
def optn_list():
    print("1. add contacts!!")
    print("2. search contacts!!")
    print("3. update contacts!!")
    print("4. delete contacts!!")
    print("5. show all contacts!!")
    print("6. exit!!")
    
    
while True:
    optn_list()
    n = input("enter the number of your choice!!!->  ")
    if n == '1':
        addcontact()
    elif n == '2':
        searchcontact()
    elif n == '3':
        updatecontact()
    elif n == '4':
        deletecontact()
    elif n == '5':
        showallcontact()
    elif n == '6':
        print("program exited successfully!!!!!!!!")
        break
    else:
        print("enter the correct choice")