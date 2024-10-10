# Laget av: Jens William Egeland 
# Dato: 11.09.2024
# Klasse: 2ITA

import random                                                       # importerer en modul globalt som tildeler tilfeldig verdier. 

fasit_tall = random.randint(1,10)                                   # en variabel som får tildelt en tilfeldig verdi mellom 1 og 10
forsok = 0                                                          # En variabel som teller antall forsøk fra bruker

while True:                                                         # en løkke som går helt til "break" leses
    bruker_gjett = int(input("Gjett tall: "))                       # En variabel som får verdien sin av hva bruker putter inn/ gjetter. 
    forsok += 1                                                     # teller + ett forsøk. 

    if bruker_gjett == fasit_tall:                                  # hvis bruker_gjett er samme som fasit_tall
        print(f"Du gjettet riktig på {forsok} forsøk!!")            # så printes "du gjetter riktig...!"
        break                                                       # når denne leses så avsluttes while-løkken. 

    elif bruker_gjett < fasit_tall:                                 # om bruker_gjett er mindre enn fasit_tall:
        print("Du gjettet for lavt!")                               # så printes "Du gjetter for lavt!"

    else:                                                           # om noe annet:
        print("Du gjettet for høyt!")                               # så printes "Du gjettet for høyt!"