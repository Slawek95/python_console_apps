# To DO List
import sys, os
# TODO sprawdz jak zrobić zmieną cons w Pythonie
PATH_TO_FILE = "PythonProjekty\\toDoList.txt"

def list_counter(list):
    counter = 0
    for item in list:
        counter += 1
    return counter

def return_user_choice():
    # TODO stwórz walidacje danych (jeżeli input będzie nieprawidłowy funkcja ma zwrócić -1,
    #  nieprawidłowa wartość wprowadz ponownie)
    print("Jeżeli chcesz zobaczyć listę wpisz 1")
    print("Jeżeli chcesz dodać element do listy wpisz 2")
    print("Jeżeli chcesz zapisać zmiany wpisz 3")
    print("Jeżeli chcesz wyjść wpisz 4")
    print("Jeżeli chcesz usunąć zadanie wpisz 5")
    return int(input())
    
def show_titled_list(list, title):
    print(title)
    counter = 1
    sign = "->"
    for list_elemnt in list:
        print(counter, sign, list_elemnt.strip())
        counter +=1
# program sprawdza czy plik istnieje, następnie otwiera plik i konwertuje do listy
# jeżeli nie komunikuje o błędzie
try:
    file = open(PATH_TO_FILE, "r")
    to_do_list = file.read()
    file.close()
    to_do_list = to_do_list.split(",")
except:
    print("Wystąpił błąd przy otworzeniu pliku!")
    sys.exit()
    
show_titled_list(to_do_list, "Twoja lista zadań to: ")

# zmienna przyjmuje niewłaściwą wartość aby pętla się rozpoczeła, po czym pobiera zmienną od użytkownika
user_choice = -1
while user_choice != 4:
    user_choice = return_user_choice()
    # program porównuję zmienną, po czym wyświetla listę
    if user_choice == 1:
        show_titled_list(to_do_list, "Twoja lista zadań to: ")
        continue
    # program dodaje zadanie do listy
    if user_choice == 2:
        print("Wpisz zadanie!(wprowadz pusty wiersz, aby zakończyć)")
        task = input()
        while len(task) != 0:
            to_do_list.append(task)
            task = input()
        show_titled_list(to_do_list, "Twoja lista zadań to: ")

    # program zmienia listę w stringa po czym zapisuję w pliku 
    if user_choice == 3:
        try:
            to_do_string = ", ".join(to_do_list)
            file = open(PATH_TO_FILE, "w")
            file.write(to_do_string)
            file.close()
            print("zapisano listę")
        except:
            print("wystąpił błąd przy otworzeniu pliku!")
            break

    #TODO dodać usuwanie zadań
    # 1 użytkownik ma wprowadzić indeks zadania które chce usunąć - wykonane
    # 2 wciskając enter ztwierdza zmianę - wykonane
    # program pyta czy na pewno chce zatwierdzić zmianę - wykonane
    # użytkownik potwierdza wybierając y, neguje wpisując n - wykonane
    # gdy zostanie wprowadzona nieprawidłowa wartość program wyświetla informację i pyta o indeks
    # program ma wrócić do kolejnego zapytania o usunięcie zadania
    
     
    if user_choice == 5:
        show_titled_list(to_do_list, "Twoja lista zadań to: ")
        print("Wprowadź indeks zadania które chcesz usunąć")
        num_of_chore = int(input())
        num_of_chore = num_of_chore -1
        while num_of_chore <= list_counter(to_do_list) or num_of_chore >= 0:
            show_titled_list(to_do_list, "Twoja lista zadań to: ")
            print("Wprowadź indeks zadania które chcesz usunąć")
            print("Wprowadź enter aby wyjść")
            num_of_chore = input()
            if len(num_of_chore) != 0:
                num_of_chore = int(num_of_chore)
                num_of_chore = num_of_chore -1 
                print(f"Zadanie które chcesz usunąć to: {to_do_list[num_of_chore]}")
                print("Jeżeli chcesz usunąć to zadanie wpisz: y\n jeżeli nie wpisz: n")
                yes_or_no = input()
                if yes_or_no == "y":
                    print("zadanie zostało usunięte")
                    to_do_list.pop(num_of_chore)
                elif yes_or_no == "n":
                    print("nie usunięto zadania")
                    show_titled_list(to_do_list, "Twoja lista zadań to: ")
                    break
            elif len(num_of_chore) == 0:
                break
                    

        
#    os.system("cls") # wywołuje komendę w konsoli





