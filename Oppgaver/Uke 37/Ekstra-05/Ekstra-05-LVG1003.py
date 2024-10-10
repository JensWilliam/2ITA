# Laget av: Jens William Egeland
# Dato: 10.09.2024
# Klasse: 2ITA


antall_folk = int(input("Skriv antall folk som kommer på pølse-festen: "))
polser_per = int(input("Skriv antall pølser per person: "))
    #To variabler, som får verdien sin av hva bruker setter inn. 



polser_totalt = antall_folk * polser_per
brod_totalt = polser_totalt
    #polser_totalt er hvor mange pølser det blir totalt. 
    #brod_totalt er hvir mange pølsebrød det blir totalt, altså samme som totale antall pølser. 

polsepakker = polser_totalt / 10
brodpakker = brod_totalt / 8
    #polsepakker deler totale antalle pølser med 10, fordi 10 pølser er 1 pakke. 
    #brodpakker gjør det samme men deler antall brød totalt på 8, fordi 1 pakke er 8 brød. 

    #Hvis polsepakker er større en pols, f.eks: 1,3 > 1, 
    #.. så legger jeg på 1, på pols-variabelen.
    #Det gjør at bruker får beskjed om å kjøpe 2 pakker pølser, og ikke 1,3. 
if polsepakker > int(polsepakker):
    polsepakker += 1
    print(f"Du trenger {int(polsepakker)} pølsepakker")

else:
    print(f"Du trenger {int(polsepakker)} pølsepakker")
    #else.. altså om polsepakker ikke er større en pols (f.eks: polsepakker = 1,0), så har pols samme verdi bare som int..
    #.. og da printes det at bruker bare trenger 1 pakke pølser. 


    #her gjør jeg det samme som over, bare med brød. 
if brodpakker > int(brodpakker):
   brodpakker += 1
   print(f"Du trenger {int(brodpakker)} brødpakker")
else:
    print(f"Du trenger {int(brodpakker)} brødpakker")










polsepakker *= 10
brodpakker *= 8

overspolser = polsepakker % polser_totalt 
oversbrod = brodpakker - brod_totalt




print(f"Du får {int(overspolser)} pølser til overs")
print(f"Du får {int(oversbrod)} pølsebrød til overs")
