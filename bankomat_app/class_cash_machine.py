from class_data_source import data_source
import sys, os

class cash_machine:

    def __init__(self,data_source):
        self.data_source = data_source

    usr_name = ""
    usr_PIN = ""
    stetement = False



    def display_main_menu(self):
        print("-"*20)
        print("Wybierz 1, aby zobaczyć stan konta")
        print("Wybierz 2 aby wpłacić gotówkę")
        print("Wybierz 3 aby wypłacić gotówkę")
        print("Wybierz 4 aby zmienić PIN")
        print("Wybierz 5 aby zakończyć operację")
        print("-"*20)
        usr_choice = int(input())
        return usr_choice

    def display_welcome_menu(self):
        print("Witaj w bankomacie wprowadź imię oraz PIN aby przejść dalej")
        usr_name = input("Podaj Imię: ")
        usr_PIN = input("Podaj PIN: ")
        return usr_name, usr_PIN 

    def app_close(self):
        final_d = input("Czy napewno chcesz zakończyć operacje y/n:\n")
        if final_d == "y":  
            print("Zakończono opercaję")
            sys.exit(1)
        else:
            pass


    def choice_service(self,usr_choice, name): # dobry pomysł ale chyba zła klasa
        if usr_choice == 1:
            self.data_source.get_account_balance(name)
        elif usr_choice == 2:
            self.data_source.add_to_account(name)
        elif usr_choice == 3:
            self.data_source.took_from_account(name)
        elif usr_choice == 4:
            self.data_source.change_PIN(name)
        elif usr_choice == 5:
            self.app_close()


    def run(self):
        #print(self.data_source.usr_list[1].name)
        u_name, u_PIN  = self.display_welcome_menu()
        statement = self.data_source.verify_login_data(u_name, u_PIN)
        while statement == True:
            usr_choice = self.display_main_menu()
            self.choice_service(usr_choice, u_name)
            #choice_service(usr_choice)

        pass