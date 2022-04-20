import sys 
PATH_TO_FILE = "python_console_apps\\bankomat_app\\account_file.txt"

try:
    file = open(PATH_TO_FILE, "r")
    WORDS = file.readlines()
    file.close()
except:
    print("Wystąpił błąd przy otworzeniu pliku!")
    sys.exit()
a = WORDS 
for x in a:
    print(x)
print(x)