MasterPassword = input('Enter your master password: ')


def write():
    with open('manage.txt','w') as file:
        file.write(f"Your master password is {MasterPassword}")

write()
def view():
    with open('manage.txt','r') as file:
        result = file.read()
        print(result)



while True:
    choice = input("Write 'view' to check you password and 'new' for making new password and 'q' for quit: ")
    if choice =='q':
        break

    if choice == 'view':
        view()

    elif choice == 'new':
        NewMasterPassword = input('Enter your new master password: ')
        with open('manage.txt','w') as file:
            file.write(f"The  new master password {NewMasterPassword}")

