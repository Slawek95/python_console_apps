class Person:
    name = ""
    PIN = 0000
    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN

    def data_check(self):
        print(f"Witaj {self.name} twój Pin to {self.PIN}")

class Account(Person):
    def __init__(self, name, PIN, account):
        super().__init__(name,PIN)
        self.account = account

    def test1(self):
        print(f"Witaj {self.name} twój Pin to {self.PIN}, twój stan konta to {self.account}")  


def main():
    
    Erwina = Person(name = "Erwina", PIN = "1234")
    Erwina.data_check()
    Sławek = Account(name = "Sławek", PIN = "1111", account = 1000)
    Sławek.data_check()
    Sławek.test1()

    
if __name__ == "__main__":
    main()