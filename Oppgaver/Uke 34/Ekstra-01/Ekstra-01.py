# Laget av Jens William Egeland
# Dato: 26.08.2024
# Klasse: 2ITA



import random

correct_answers = 0                                    # denne variablen brukes for å telle antall riktige svar

for _ in range(10):
    tall1 = random.randint(1, 10)                      # random.randint() dette sette verdien til en tilfeldig integer innenfor rangen(1, 10)
    tall2 = random.randint(1, 10)
    product = tall1 * tall2                            # product er svaret til tall1 * tall2

    print(f"{tall1} * {tall2} = ?")                    # printer ut regnestykket. "f" gjør det mulig å bruke krøllparanteser{} i en streng
    user_answer = int(input("Enter your answer: "))     # int(input("bla bla bla")) brukes for å la brukeren skrive inn en integer som svar

    if user_answer == product:                        
        correct_answers += 1                            # hvis bruker sitt svar er samme som svaret til regnestykke,
                                                        # blir correct_answer variablen +1 

if correct_answers == 10:                               # hvis correct_answer variablen er 10 så printes noe
    print("Supert! Du er god!")
elif correct_answers == 9:                              # hvis correct_answer variablen er 9 så printes noe annet
    print("Dette var bra!")
elif correct_answers == 8:                              # hvis correct_answer variablen er 8 så printes noe annet
    print("Bra, men du kan øve mer!")
else:                                                   # hvis noe annet enn det over gjelder, altså svaret er 7 eller mindre, printes noe annet
    print("Du må øve mer")