class usr:
    name = ""
    statement = True
    def __init__(self,name,phone_number,email, id, PIN, account ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.id = id
        self.PIN = PIN
        self.account = account
    

    def data_check(self):
        print(f"Witaj {self.name} twój Pin to {self.phone_number}, test {self.email}, test {self.id}, test {self.account}")
"""
def main():
    a = usr("a","a", "a","a", "a")
    b = usr( "b","b", "b","b", "b")
    a.data_check()
    b.data_check()


if __name__ == "__main__":
    main()
"""