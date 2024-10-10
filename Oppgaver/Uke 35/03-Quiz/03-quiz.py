# Laget av: Jens William Egeland
# Dato: 30.08.2024
# Klasse: 2ITA






riktige_svar = 0                                                        # Variabel som skal telle antall riktige svar 

svarene = ["SKIEN", "M1", "H121", "PER", "RANDOM", "OSLO", "APPLE", "HUND", "HERKULES", "JA"]

                                                                        # En Liste med alle de korrekte svarene




spørsmålene = {                 
    0: "I hvilken kommune finner du Brekkeparken? ",
    1: "Hvilken buss går fra gulset til langesund? ",
    2: "Hva heter klasserommet til 2ITA? ",
    3: "Hva heter kontaktlæreren til 2ITA? skriv kun fornavn: ",
    4: "For å kunne tildele tilfeldige verdier i python skriver man: 'import ...",
    5: "Hva er hovedstaden i Norge? ",
    6: "Hva heter bedriften bak iPhone? ",
    7: "Hva er det vanligste kjæledyret? ",
    8: "Hva er det største kjøpesenteret i skien? ",
    9: "Er det vanskelig å tenke ut quiz-spørsmål? (ja/nei): "
}
                                                                        # En dictionary som holder alle spørsmålene, navnet på Key'sa er fra 0 til 9 pga listen over også er slik.
                                                                        # da kan "i" på for-loopen hente ut nytt spørsmål og gjeldene svar for hver gang den looper. 
                                                         
                                                                        
for i in range(len(svarene)):                                           # Denne for-loopen sier at koden under kjøres fra i = 0 til i = len(svarene). Altså til i = antall svar/spørsmål.
    spørsmål = str(input(spørsmålene[i]))                               
                                                                        # Variablen har en input der bruker setter inn svaret de tror stemmer. 
                                                                        # "i'en" inni "spørsmålene[i]" henter ut hvilket spørsmål den skal vise brukeren.
    
    if spørsmål.upper() == svarene[i]:                                  # Hvis "spørsmål.upper()" stemmer med svaret printes det og teller 1 poeng
        print("Riktig svar!")                                           # .upper() gjør om svaret fra bruker til STORE BOKSTAVER, sånn at stor eller liten bokstav ikke påvirker. 
        riktige_svar += 1                                               # Teller 1 poeng for hvert riktig svar
        print(f"Du har {riktige_svar} poeng")                           # Printer hvor mange poeng du har etter hvert riktig svar.                             
    else:
        print("feil svar!")

print(f"Du fikk totalt: {riktige_svar} av {len(svarene)} mulige poeng") 
                                                                        # Når loopen stopper printes antall riktige poeng.




# Hei Jens!
# Mye bra kode her.
# Stå på videre!
# Staale

