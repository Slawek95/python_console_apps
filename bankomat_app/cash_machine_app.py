# TODO napisać aplikację bankomat, która pozwala zapamiętać osobę
#  odczytać stan konta, wpłacać i wypłacać środki
# aplikcja pobiera od urzytkownika PIN po czym pozwala na działanie
# Start: stan konta 1000zł, PIN: 1234

#TODO dołożyć counter przy wprowadzaniu PIN


import python_console_apps.bankomat_app.class_Person as class_Person
import sys, os
usrs_data = {'Sławek' : "1234", 'Erwina' : "0000"} # zrobić klasę dla usr
account = 1000 # TODO zrobić klase dla kont

### ACCOUNT from file ###
PATH_TO_FILE = "python_console_apps\\bankomat_app\\account_file.txt"

try:
    account_file = open(PATH_TO_FILE, "r")
    account_balance = account_file.readlines()
    account_file.close()
except:
    print("Wystąpił błąd przy otworzeniu pliku!")
    sys.exit()
for ammount in account_balance:
    ammount = account

### ACCOUNT from file ###

def show_options():
    print("-"*20)
    print("Wybierz 1, aby zobaczyć stan konta")
    print("Wybierz 2 aby wpłacić gotówkę")
    print("Wybierz 3 aby wypłacić gotówkę")
    print("Wybierz 4 aby zmienić PIN")
    print("Wybierz 5 aby zakończyć operację")
    print("-"*20)

# sprawdzenie PIN
print("Witaj w bankomacie wprowadź imię oraz PIN aby przejść dalej")
name = input("Podaj Imię: ")
if name in usrs_data:
    PIN = input("Podaj PIN: ")
    if PIN == usrs_data.get(name):
        print("Zalogowałeś się poprawnie")
        #if usr_choic
        show_options()
    else:
        print("wprowadziłeś niepoprawny PIN")
        sys.exit(0)

    usr_choice = int(input())
    while usr_choice != 5:

            #1 Wywoływanie stanu kąta
        if usr_choice == 1:
            print(account)
            show_options()
            usr_choice = int(input("Wybierz operację jaką chcesz wykonać"))

            #2 Wpłata gotówki
        elif usr_choice == 2:
            print("Wpisz ile gotówki chcesz wpłacić")
            money_added = int(input())
            account = money_added + account
            show_options()
            print(f"Wpłaciłeś {money_added} twoje saldo wynosi {account}")
            usr_choice = int(input("Wybierz operację jaką chcesz wykonać"))
                
            #3 wypłata gotówki
        elif usr_choice == 3:
            print("Wpisz ile gotówki chcesz wpłacić")
            money_take = int(input())
            account = account - money_take
            show_options()
            print(f"Wyłaciłeś {money_take} twoje saldo wynosi {account}")
            usr_choice = int(input("Wybierz operację jaką chcesz wykonać"))
            #4 zmiana nr PIN
        elif usr_choice == 4: # TODO dodać wyjście z pętli
            print("aby zmienić nr PIN wprowadź obecny nr Pin:")
            old_pin = input()
            if old_pin == usrs_data.get(name):
                print("wprowadziłeś poprawny nr Pin")
                print("wprowadź nowy PIN (4 cyfry)")
                new_pin1 =input()
                print("powtórz nowy PIN PIN (4 cyfry)")
                new_pin2 =input()
                if new_pin1 == new_pin2:
                    usrs_data[name] = new_pin1
                    print(f"twój Pin to {usrs_data[name]}")
                    show_options()
                    usr_choice = int(input("Wybierz operację jaką chcesz wykonać"))
            else:
                print("wprowadziłeś zły Pin, sprubuj ponownie!\nAby przejść dalej wciśnij enter")
                old_pin = input()
                    

        else:
            print("wybrałeś niewłaściwą wartość sprubuj ponownie")
            usr_choice = int(input())
            # 5 wyjście
    if usr_choice == 5:
        sys.exit(0)
        



