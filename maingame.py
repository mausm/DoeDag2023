import os
import random
os.chdir('/home/maurits/Desktop')

# We hebben een simpel spelletje geprogrammeerd
# alleen het te raden nummer is nu altijd 42, wel makkelijk..maar dat moet gefixt worden want het is nu geen spel
# We willen ook graag zien of je te laag of te hoog raadt, dus je moet een check inbouwen
# De score telling is ook wat simpel 1000 - het aantal keer raden. Kan je dat verbeteren?

def main():
    GESPEELDE_SPELLEN = 0
    SCORE = 0
    POGINGEN = 0
    # hier stellen we het te raden nummer voor het eerst in
    TE_RADEN_NUMMER = nummer_bepalen()
    HIGH_SCORES = [] # [("Piet" : 560), ("Ali": 555)]
    
    intro()
    
    while True:
        # De hoofd taak die de hele tijd draait    
        
        UITSLAG = nummer_raden(TE_RADEN_NUMMER)
        POGINGEN+=1
        SCORE = score_bepalen(POGINGEN)

        if (UITSLAG):
            # Wat gebeurd er als je het goed hebt geraden
            print(f'Gefeliciteerd je hebt het goed geraden, in {POGINGEN} keer met een score van: {SCORE}')
            NAAM = input("Wat is je naam? ")
            HIGH_SCORES.append((NAAM, SCORE))
            high_scores(HIGH_SCORES)
            
            # we zetten alles weer op 0 / doen alles opnieuw
            POGINGEN = 0                               
            TE_RADEN_NUMMER = nummer_bepalen()

            invoer = input('Wil je nog een keer spelen? ja/nee ').lower()
            if (invoer != 'ja' ):
                break

def intro():
    # begin tekst
    print("""Je moet in zo min mogelijk stappen de het nummer raden
Na elke keer raden krijg je te horen of je te hoog of te laag zit""")


def score_bepalen(pogingen):
    MAXIMUMSCORE = 1000
    
    # Opdracht: verzin een score telling
    # Hoe vaker je raadt hoe minder goed je het doet, dus er gaat steeds meer af van de beginscore
    # Nu gaat er per stap 1 af, dus na 5 pogingen is je score 995. 
    # Je kan haakjes gebruiker zoals 1000 - (100 * 5)

   
    SCORE = MAXIMUMSCORE - pogingen

    return SCORE


def check_stand(gekozen_nummer, TE_RADEN_NUMMER):
    
    if (gekozen_nummer != TE_RADEN_NUMMER ):
        print('Helaas het nummer klopte niet\n') 

    return gekozen_nummer == TE_RADEN_NUMMER


def nummer_raden(TE_RADEN_NUMMER):
    GEGOKT_NUMMER = input('Geef een nummer tussen 1-100  \n')
    # zet het om vam tekst naar een getal
    GEGOKT_NUMMER = int(GEGOKT_NUMMER)

    # Opdracht: wat gebeurd er als je geen nummer invoert?
    # https://www.w3schools.com/python/ref_string_isnumeric.asp

    # Hoe geef je aan of het gegokte nummer hoger of lager is dan het echte nummer?
    # Zoek op internet hoe je een check of een nummer hoger of lager is in python
 
    #  https://www.w3schools.com/python/trypython.asp?filename=demo_oper_compare4
    # if (a > b) :
    # CODE HIER

    # Als GEGOKT_NUMMER LAGER IS DAN TE RADEN NUMMER: PRINT TE LAAG
    if GEGOKT_NUMMER < TE_RADEN_NUMMER:
       print("Te laag!")
    
    # ALS GEGOKT NUMMER HOGER IS DAN TE RADEN NUMMER" PRINT TE HOOG
    if GEGOKT_NUMMER > TE_RADEN_NUMMER:
       print("Te hoog!")


    #check of je gewonnen hebt in de ander funtie
    return check_stand(GEGOKT_NUMMER, TE_RADEN_NUMMER)


def nummer_bepalen():
    TE_RADEN_NUMMER = random.randint(1,100)
    #print(TE_RADEN_NUMMER)


    # Hoe bepalen we het nummer dat we moeten raden?

    # Opdracht zoek op het internet hoe je een nummr tussen twee getallen terug krijgt (bijvoorbeeld 0 en 100)
    # https://www.w3schools.com/python/ref_random_randint.asp

    # dit wordt het nummer dat je moet raden
    return TE_RADEN_NUMMER


def high_scores(HIGH_SCORES : list):
    # dit sorteert de scores van hoog naar laag
    sorted_data = sorted(HIGH_SCORES, key=lambda x: x[1], reverse=True)

    alle_scores = ""
    for score in sorted_data:
        
        scorelijn = f'{score[0]} : {score[1]}'
        
        alle_scores += '\n ' + scorelijn
        print(scorelijn)


    with open('scores.txt', 'w') as f:
        f.write(alle_scores)        


main()
