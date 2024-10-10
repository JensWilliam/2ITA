# Laget av: Jens William Egeland
# Dato: 06.09.2024
# Klasse: 2ITA








while True:                                                                         # Denne while loopen går evig. det betyr at bruker ikke trenger å kjøre koden på  nytt for å få en ny gangetabell.
    bruker_tallet = int(input("Skriv tallet du ønsker gangetabell til her: "))      # Her taster brukeren inn tallet han ønsker gangetabellen til. 
    
    for i in range(1, 11):                                                          # i-en går gjennom verdiene i rangen for hver loop, den starter på 1 og går helt til 10 før den stopper på 11.
        
        if bruker_tallet > 10 or bruker_tallet < 1:                                 # Hvis bruker taster inn et tall over 10 eller under 1, printes det at tallet må være mellom 1 og 10 og så avsluttes for-loopen.
            print("tallet må være mellom 1 og 10")  
            break
        
        print(bruker_tallet * i)                                                    # Her ganges brukertallet med i, på første loop har i verdi = 1.
          










