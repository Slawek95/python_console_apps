# Napisz aplikację BMI Kalkulato za pomocą klas
# aplikacja informuję usr o sposobie działania
# przyjmuje dane od usr
# przelicza dane 

# BMI CALCULATOR APP
# TODO napisac klasę osoba która będzie przyjmowałą (imię, wiek, wzrost,wagę)

class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def person_introduction(self):
        print(f"Witaj, nazywasz się {self.name} masz {self.age} lat, {self.height} cm wzrostu, {self.weight} kg wagi" )

    def BMI(self):
        BMI = self.weight / (self.height/100 * self.height/100)
        print(f"{self.name} twoje BMI to: {BMI}")
        return BMI

    def check_BMI(self,BMI):
        if BMI > 30:
            print("Jesteś otyły")
        elif BMI > 24:
            print("Masz nadwagę")
        elif BMI > 19:
            print("Twoja waga jest w normie")
        else:
            print("niewłaściwa wartość")

def main():
    
    print("Witaj w aplikacji kalkulator BMI!\npodaj odpowiedzi na następujące pytania aby dowiedzieć się jakie jest twoje BMI oraz czy masz nadwagę")
    name1 = input("Podaj imię: ")
    age1 = int(input("Podaj swój wiek: "))
    height1 = int(input("Podaj swój wzrost w cm: "))
    weight1 = int(input("Podaj wagę w kg: "))


    name1 = Person(name = name1, age = age1, height = height1, weight = weight1)
    # Erwina = Person(name = "Erwina", age = 24, height = 164, weight = 52)

    name1.person_introduction()
    #Erwina.person_introduction()

    print("-"*20)

    BMI_name1 = name1.BMI()
    #BMI_Erwina = Erwina.BMI()

    print("-"*20)

    name1.check_BMI(BMI_name1)
    #Erwina.check_BMI(BMI_Erwina)

if __name__ == "__main__":
    main()

