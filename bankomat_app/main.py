from class_data_source import data_source
from class_usr import usr# TODO zmienić nazwę klasy cash machine
from class_cash_machine import cash_machine

# stworzyć obiekty klasy usr, stworzyć listę obiektów, włożyć do data source

def main():
    data = data_source()
    ATM = cash_machine(data_source = data)
    ATM.run()
    
    
    
if __name__ == "__main__":
    main()