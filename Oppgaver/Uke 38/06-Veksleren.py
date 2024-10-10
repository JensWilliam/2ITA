# Laget av: Jens William Egeland
# Dato: 17.09.2024
# Klasse: 2ITA




    #bruker input for kjøpspris
Kjopspris = int(input("Skriv kjøpesummen her: "))

    #bruker input for hvilken seddel som skal betales med
Betalings_lapp = int(input("Hvilken seddel vil du betale med? "))
 
    #Lapper er hvor mange Betalings_lapp som får plass i kjopsprisen, f.eks: Lapper = 3, siden det er plass til 3 stk 50-lapper i kjopsprisen(151)
Lapper = Kjopspris // Betalings_lapp
    #Hvis seddelen ikke er like mye som prisen, legger jeg til 1, på "Lapper". (fordi da har bruker råd, og får bare veksel for det ekstra som ble betalt.)
if Betalings_lapp != Kjopspris:
    Lapper += 1
    #Veksel er hvor mye KR bruker ga minus prisen. 
Veksel = Lapper * Betalings_lapp - Kjopspris
    
print(f"Du bruker {Lapper} stk seddler og får Kr {Veksel},- i veksel:")

    #for hvert par i dictionaryen "rest":
        #belop er hvor mange veksel-lapper/mynter som dekker totale veksel-beløpet. 
        #hvis belop er større enn 0, printes hvor mange av gjeldene seddel/mynt, bruker får i veksel. 
        #Veksel %= int, sier at totale veksel-beløpet blir mindre med hvor mye som ble gitt i veksel.


    #denne dictionaryen brukes av en for-løkke, for løkken iterer gjennom key, "value" parrene
rest = [
    (1000, "1000-lapp"),
    (500, "500-lapp"),
    (200, "200-lapp"),
    (100, "100-lapp"),
    (50, "50-lapp"),
    (20, "20-krone"),
    (10, "10-krone"),
    (5, "5-krone"),
    (1, "1-krone"),
    ]

for int, string in rest:
    belop = Veksel // int

    if belop > 0:
        print(f"{belop} stk: {string}")
    
    Veksel %= int