# Laget av Jens William Egeland
# Dato: 27.08.24
# Klasse: 2ITA



import random                                               #Jeg importerer en modul som skal tilordne en tilfeldig verdi til terningen. 



antall_kast = 0                                             #Jeg deklarerer en variabel som skal telle antall kast.

while True:                                                 #Jeg lager en while-loop som går helt til den leser "break".
    terning_kast = random.randint(1, 6)                     #Jeg deklarerer en variabel som tilordnes en tilfeldig verdi mellom 1 og 6
    antall_kast += 1                                        #antall kast går opp med 1
    
    if terning_kast == 6:                                   #Hvis terningen lander på 6, skal det printes antall kast og at den landet på 6
        print(f"Kast nummer {antall_kast}: Du rullet en {terning_kast}'er!!!")
        break                                               #Etter det printes ut så stopper looper her. 

    print(f"Kast nummer {antall_kast}: Du rullet en: {terning_kast}'er")  #Her printes kast nummeret, og hva terningen landet på, hvis det ikke ble en 6'er. 




