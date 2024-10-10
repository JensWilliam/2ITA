# Laget av: Jens William Egeland
# Dato: 24.09.2024
# Klasse: 2ITA




def areal_rektangel(h, b):                              # Definerer en funskjon med parameterene h og b (høyde og bredde)
    return h * b                                        # Når funksjonen kalles, returnerer jeg verdien av h * b, altså arealet

rektangel_hoyde = int(input("Skriv inn høyde: "))       # Input for høyde
rektangel_bredde = int(input("Skriv inn bredde: "))     # Input for bredde

areal = areal_rektangel(rektangel_hoyde, rektangel_bredde)  # Variabel som gir verdiene fra input til funksjonens parametere. 
print("Areal av rektangel = ", areal)                       # Printer arealet av rektangelen, ved bruk av variabelen over. 


def areal_sirkel(r):                                    # Definerer en funskjon med parameteren r (radius)
    return 3.14 * r * r                                 # Når funksjonen kalles, returnerer jeg pi(3.14) * verdien av r. altså areal av sirkel

sirkel_radius = int(input("Skriv inn radius til sirkel: ")) # input for radius

a_sirkel = areal_sirkel(sirkel_radius)                  # Variabel som gir verdien fra input til funksjonens parameter. 
print("Areal av sirkel = ", a_sirkel)                   # Printer arealet av sirkelen, ved bruk av variabelen over. 