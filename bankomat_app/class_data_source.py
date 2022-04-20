from class_usr import usr
import sys, os



class data_source:
    usr_list = []  

    def __init__(self):  # 
        self.load()
    

    def load(self): # stworzyć obiekty klasy usr, stworzyć listę obiektów, włożyć do data source name,phone_number,email, id , account
        Sławek = usr(name = "Sławek", phone_number = 726066498, email = "logun1311d@gmail.com",PIN = "1111", id = 1, account = 1000)
        Erwina = usr(name = "Erwina", phone_number = 123456789, email = "erwa@gmail.com",PIN = "2222", id = 2, account = 2000)
        Milena = usr(name = "Milena", phone_number = 987654321, email = "mila@gmail.com",PIN = "3333", id = 3, account = 5000)
        Liliana = usr(name = "Liliana", phone_number = 111444777, email = "lila@gmail.com",PIN = "4444", id = 4, account = 3000)
        self.usr_list = [Sławek, Erwina, Milena, Liliana]
        

    def verify_login_data(self, name, PIN):
        for usr in self.usr_list:
            if usr.name == name and usr.PIN == PIN:
                print(f"wprowadzono poprawne dane twoje imię: {name}, twój Pin to {PIN}")
                return True
        print("Wprowadzono niewłaściwe dane")
        return False

    def get_account_balance(self,name): # dobry pomysł ale chyba zła klasa
        for usr in self.usr_list:
            if usr.name == name:
                print(f"Twoje aktualne saldo wynosi: {usr.account}")
                account = usr.account
                return account

    def add_to_account(self, name):
            print("Wpisz ile gotówki chcesz wpłacić")
            money_added = int(input())
            for usr in self.usr_list:
                if usr.name == name:
                    account = usr.account
                    account = usr.account + money_added
                    usr.account = account
                    print(f"Wpłaciłeś {money_added}zł. Twoje saldo wynosi: {usr.account}")
    
    def took_from_account(self, name):
            print("Wpisz ile gotówki chcesz wyłacić")
            money_took = int(input())
            for usr in self.usr_list:
                if usr.name == name:
                    account = usr.account
                    account = usr.account - money_took
                    usr.account = account
                    print(f"Wypłaciłeś {money_took}zł. Twoje saldo wynosi: {usr.account}")

    def change_PIN(self,name):
        print("aby zmienić nr PIN wprowadź obecny nr Pin:")
        old_pin = input()
        for usr in self.usr_list:
                if usr.name == name:
                    PIN = usr.PIN
                    print(PIN)
                    if old_pin == PIN:
                        print("wprowadziłeś poprawny nr Pin")
                        print("wprowadź nowy PIN (4 cyfry)")
                        new_pin1 =input()
                        print("powtórz nowy PIN PIN (4 cyfry)")
                        new_pin2 =input()
                        if new_pin1 == new_pin2:
                            usr.PIN = new_pin1
                            print(f"twój Pin to {usr.PIN}")

    


            
            
    
"""
    def get_account_balance(self,name):
        for usr in self.usr_list:
            if usr.name == name:
                print(usr.account)



    def display_account_balance(self, name):
            print(self.get_account_balance(name))
            show_options()
            usr_choice = int(input("Wybierz operację jaką chcesz wykonać"))
"""
        

        
