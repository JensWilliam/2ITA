# Laget av Jens William Egeland
# Dato: 03.09.2024
# Klasse: 2ITA

import random

antall_kast = 0                                                                                             # Teller antall kast

while True:                                                                                                 # While loop som går helt til spiller får yatzy. 
    terning1 = random.randint(1, 6)                                                                         #Deklarerer en  variabel for hver terning som tilorndes tilfeldig tall mellom 1 og 6.
    terning2 = random.randint(1, 6)
    terning3 = random.randint(1, 6)                 
    terning4 = random.randint(1, 6)
    terning5 = random.randint(1, 6)
    antall_kast += 1                                                                                        #antall_kast blir + 1 for hver loop

    if terning1 == terning2 and terning1 == terning3 and terning1 == terning4 and terning1 == terning5:     # Hvis alle terningene er like så printes det
        print(f"På kast nummer {antall_kast} fikk du {terning1}'er yatzy")
        break                                                                                               # Siden bruker fikk yatzy, avsluttes løkken med break. 

    print(f"Kast nummer {antall_kast} : du fikk {terning1}, {terning2}, {terning3}, {terning4} og {terning5}")      #Hvis bruker ikke får yatzy printes resultat av kast, og kast nummer. 
