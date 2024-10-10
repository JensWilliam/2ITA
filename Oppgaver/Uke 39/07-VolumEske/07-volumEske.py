# Laget av: Jens William Egeland
# Dato: 24.09.2024
# Klasse: 2ITA


while True:

    # En funksjon som kan regner ut volum 
    # parameteren h / (høyde), får verdi fra input og/eller optimalisering.
    def volumRegneren(h):
        bredde = arkB - h * 2           #bredde er bredden av bestemt type  - høyde * 2
        lengde = arkL - h * 2           #høyde er lengden av bestemt type  - høyde * 2
        volumet = bredde * lengde * h   #Her regnes ut volumet av boksen, bredden og høyden må endres i forhold til høyden av boksen, derfor gjorde jeg det over.
        return volumet                  # Returnerer volumet

    
    # denne dictionaryen holder alle standard mål for ark: A6 til A2
    arkMal = {
        "A6" : [10.5, 14.8],
        "A5" : [14.8, 21],
        "A4" : [21, 29.7],
        "A3" : [29.7, 42],
        "A2" : [42, 59.4],
    }

    print("Velkommen til Volum Regneren !!!")
    print("Velg hvilket ark har du laget en boks av?")
    print("-----------------------------------------") # Kun for leslighet
    #printer valg-mulighetene
    print("A6")
    print("A5")
    print("A4")
    print("A3")
    print("A2")
    print("Om du vil finne maks volum av annet objekt skriv: 'ja': ")
    print("-----------------------------------------") # Kun for leslighet

    #bruker skriver inn ønsket valg, svaret omgjøres til caps for å matche dictionaryen.
    brukerArk = input("Skriv inn ønsket valg: ").upper()
    print() # Kun for leslighet

    # hvis bruker sier ja, optimaliserer jeg for å finne maks volum med bruker sin lengde og bredde.
    if brukerArk == "JA":
        arkB = float(input("Skriv inn bredden (cm): "))
        arkL = float(input("Skriv inn lengden (cm): "))
        h = 0.1                 #start verdi for høyde
        maksHoyde = arkB / 2    #maksimal høyde er bredden / 2
        maksVolum = 0           #startverdi for maksimal volum

        # mens høyde er mindre enn makshøyde:
        while h < maksHoyde:
            volum = volumRegneren(h)    # funskjon regner volum med verdi til h, og lagrer det i en variabel
            if volum > maksVolum:       # hvis volum er større enn maksVolum, så har volumet stiget siden forrige loop, og maksVolum får verdien til volum, og optimalHoyde får verdien til h
                maksVolum = volum
                optimalHoyde = h
            else:                       #om volum ikke lenger er større enn maksvolumet, så har vi funnet maksimalet volum while-loopen brytes. 
                break
            h += 0.1                    #for hver loop går høyden (h) opp 0.1 cm

        print(f"Maksimalet volumet er: {maksVolum:.2f}cm^3")
        print(f"Optimal høyde er da: {optimalHoyde:.2f}cm")
        break #denne break'en bryter ut av koden og avslutter programmet. 
    else:
        pass #om bruker ikke svarte ja, så hopper den over det og går videre. 
    

    #bruker skriver inn høyde på boksen i cm.
    brukerHoyde = float(input("Skriv inn høyde på boksen du lagde(cm): "))

    #hvis brukerArk (inputen fra bruker) finnes i dictionary'en OG brukerHoyden er gyldig så kjøres koden under.
    if brukerArk in arkMal and brukerHoyde < arkMal[brukerArk][0] / 2:
        arkB = arkMal[brukerArk][0] #henter riktig bredde fra dict
        arkL = arkMal[brukerArk][1] #henter riktig lengde fra dict
        print("Volumet av boksen din er:")
        print(f"{volumRegneren(brukerHoyde):.2f} cm^3")   # kjører og printer funskjonen med brukerHøyde som parameter (h) :.2f gjør at det kun er 2 desimaler.
        print() #kun for leslighet
    else:
        print("Ugyldig ark- eller høyde-valg, avslutter...")    # om ikke betingelsene i if, er sanne, bryter jeg ut av koden og programmet avsluttes
        break
    



    #All kode under er for optimaliseringen (finne optimal høyde på boks for størst mulig volum)

    #Variabel med input.
    optimalisering = input(f"Vil du se den optimale høyden for maksimalt volum i en {brukerArk}-boks? (ja/nei)")


    #Hvis bruker svarte ja, kjøres optimaliseringen. 
    if optimalisering.upper() == "JA":    
        h = 0.1                                                             #Startverdi for høyden 
        maksHoyde = arkMal[brukerArk][0] / 2                                #Høyeste mulige høyde på boksen
        maksVolum = 0                                                       #Startverdi for maksimalt volum
                                                                          

        # While-loop for å finne maksimalt volum. 
        while h < maksHoyde:                                                #Mens h er mindre en maksHøyde:
            volum = volumRegneren(h)                                        #Kjøres funksjonen med verdi av h, som argument
            if volum > maksVolum:                                           #Hvis volum er større en maksvolum:
                maksVolum = volum                                           #så får maksVolum verdien til volum
                optimalHoyde = h                                            #og optimalHoyde får verdien til h
            else:
                break                                                       #om ikke volum er større enn maksVolum, så avsluttes koden fordi maksimalet volumet er funnet.
            h += 0.1                                                        # h høynes med 0.1 cm for hver loop.
        
        print(f"Maksimalt volum blir: {maksVolum:.2f} cm^3")
        print(f"Den optimale høyden for maksimalt volum er da: {optimalHoyde:.2f} cm")
        break
    else:
        print(f"Du svarte '{optimalisering}'. Avslutter...")
        break
    #Hvis bruker ikke svarte ja, avsluttes programmet.


