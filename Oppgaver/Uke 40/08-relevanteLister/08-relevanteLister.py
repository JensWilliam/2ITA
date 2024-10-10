#Laget av: Jens William Egeland
#Dato: 04.10.2024
#Klasse: 2ITA


import os


gangeTall = []

while True:                                                                         # Denne while loopen går til "break" leses.
    bruker_tallet = int(input("Skriv tallet du ønsker gangetabell til her: "))      # Her taster brukeren inn tallet han ønsker gangetabellen til. 
    
    for i in range(1, 11):                                                          # i-en går gjennom verdiene i rangen for hver loop, den starter på 1 og går helt til 10 før den stopper på 11.
        
        if bruker_tallet > 20 or bruker_tallet < 1:                                 # Hvis bruker taster inn et tall over 20 eller under 1, printes det at tallet må være mellom 1 og 20 og så avsluttes loopen.
            print("tallet må være mellom 1 og 20")  
            break
        
        print(bruker_tallet * i)                                                    # Printer gangetabbelen tall for tall helt til loopen stopper. 
        gangeTall.append(bruker_tallet * i)                                         # For hver loop legges tallene i gangetabbelen inn i listen.
    break



path = ".\\Jens\\Oppgaver\\Uke 40\\08-relevanteLister\\lagretGangetabell"           # Path til mappen der txt-filene skal lagres.
tabellene = os.listdir(path)                                                        # Denne variabelen får verdien til filene som ligger i mappen.
antallFiler = len(tabellene)                                                        # Denne variabelen får verdien til antall filer det er i variabelen over. 

with open(path + f"\\{antallFiler}.txt", "w", encoding="utf-8") as file:            # Åpner en fil i mappen med navn som er antall filer + 1.
    file.write(f"Gangetabellen for tallet: {bruker_tallet} er: \n")                 # Skriver i filen at det er gangetabellen for tallet brukeren tastet inn.
    for i in gangeTall:                                                             # For hver loop i listen gangeTall skrives tallet i filen.
        file.write(f"{i} \n")

