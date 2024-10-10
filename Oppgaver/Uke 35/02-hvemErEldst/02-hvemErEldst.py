#Laget av: Jens William Egeland
#Dato: 26.08.2024
#Klasse: 2ITA


Kari = int(input("Kari sin alder:"))           #Lager 2 variabler og skriver int.(input) for å la brukeren sette verdien (alderen) på dem selv
Henrik = int(input("Henrik sin alder:"))

if Henrik in range(1, 121) and Kari in range(1, 121):   # Hvis Henrik er innenfor 1 og 121 OG hvis kari er innenfor 1 og 121 kjøres koden under.
                                                        # Når man tilordner verdi til range, så gjelder ikke siste verdien, altså gyldige verdiene er fra 1 til og med 120. 
                                                        # men om man bare har ett tall i range. eksempel: range(121), så er også 0 gyldig. 
   
    if Kari > Henrik:                              # Hvis Kari er eldre enn Henrik (eller verdien til variablen egentlig), så printes det
        print("Kari er eldre")
    elif Kari < Henrik:                            # Hvis Henrik er eldre enn kari, så printes det
        print("Henrik er eldre")
        
    else:                                          # Hvis ikke det er en av de to over, betyr det at de har samme verdi/alder. og da printes det
        print("Kari og Henrik er samme alder")
    
else:
    print("Alderen må være mellom 1 og 120!")