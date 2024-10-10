# Laget av Jens William Egeland
# Dato: 27.08.24
# Klasse: 2ITA


import random                                       #Importerer random-modulen.

antall_kast = 0                                     #Deklarerer variabel som skal telle antall kast.

while True:                                         #Lager en While-loop som går helt til den bes stoppe.
    terning1 = random.randint(1, 6)                 #Deklarerer en  variabel for hver terning som tilorndes tilfeldig tall mellom 1 og 6.
    terning2 = random.randint(1, 6)
    antall_kast += 1                                #Antall kast går opp 1.

    if terning1 == terning2:                                                                     #Hvis terning1 har samme verdi som terning2
        print(f"På kast nummer {antall_kast} landet begge terninger på {terning1}!!!")           #..så printes antall kast og at de begge landet på tall: ?.
        break                                                                                    #Her avsluttes loopen
    
    print(f"Kast nummer {antall_kast}: Terningene landet på {terning1} og {terning2}")           #Om reslutatet til terningene ikke var likt, så printes det antall kast og hva terningene landet på. 