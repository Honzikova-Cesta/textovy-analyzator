"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie
author: Jan Procházka
email: jan.prochazka92@gmail.com
discord: .honzikovacesta
"""
import sys

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = '----------------------------------------'

#seznam registrovaných uživatelů a jejich hesel
registrovani_uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

#uživatel zadá své jméno a heslo
zadane_jmeno = input('Zadejte své uživatelské jméno: ').lower()
zadane_heslo = input('Zadejte své heslo: ').lower()
print(oddelovac)

#program zkontroluje zadané jméno a heslo jestli odpovídá některému z registrovaných uživatelů
if zadane_jmeno in registrovani_uzivatele:
    if zadane_heslo == registrovani_uzivatele[zadane_jmeno]:
        print(f'Vítejte {zadane_jmeno}. Jste přihlášen a můžete analyzovat texty.')
    else:
        print('Špatně zadané heslo. Ukončuji program...')
        sys.exit()
else:
    print('Neregistrovaný uživatel. Ukončuji program...')
    sys.exit()

#volba textu ze zadaných možností a ošetření vyjímek (try/except jsem použil kvůli zadávání desetinných čísel které způsobovaly ValueError)
volba_textu = input('Pomocí čísla 1-3 zvolte text, který chcete analyzovat: ')

try:
    cislo = int(volba_textu)
    if cislo not in (1,2,3):
        print(f'Číslo není v možnostech. Ukončuji program...')
        sys.exit()

except ValueError:
    print('Špatně zadaná hodnota. Ukončuji program...')
    sys.exit()

zvoleny_text = TEXTS[cislo-1]

#rozklad textu na jednotlivá slova a jejich očištění od nežádoucích znaků
slova_textu = zvoleny_text.split()
ocistena_slova = []
for slovo in slova_textu:
    ocistena_slova.append(slovo.strip('.,'))

#statistické údaje z vybraného textu 
pocet_slov = len(ocistena_slova)        #počet slov
slova_prvni_pismeno_velke = 0
slova_velka_pismena = 0
slova_mala_pismena = 0
pocet_cisel = 0
soucet_cisel = 0

for slovo in slova_textu:
    if slovo[0].isupper() is True:      #počet slov začínajících velkým písmenem
        slova_prvni_pismeno_velke += 1
    elif slovo.isupper() is True:       #počet slov psaných velkými písmeny
        slova_velka_pismena += 1
    elif slovo.islower() is True:       #počet slov psaných malými písmeny
        slova_mala_pismena += 1
    elif slovo.isdigit() is True:       
        pocet_cisel += 1                #počet čísel (ne cifer)
        soucet_cisel += int(slovo)      #sumu všech čísel (ne cifer) v textu

#vytištění statistických údajů s textem
print(oddelovac)
print(f'V textu je {pocet_slov} slov.')
print(f'{slova_prvni_pismeno_velke} slov má na začátku velké písmeno.')
print(f'{slova_velka_pismena} slov je psáno velkými písmeny.')
print(f'{slova_mala_pismena} slov je psáno malými písmeny.')
print(f'Celkový počet čísel v textu je {pocet_cisel}.')
print(f'Součet všech čísel v textu je {soucet_cisel}.')
print(oddelovac)

#graf
#delka slova - vyskyt graficky - pocet cislem
slova_podle_poctu_pismen = {}
for slovo in ocistena_slova:
    if len(slovo) not in slova_podle_poctu_pismen:
        slova_podle_poctu_pismen[len(slovo)] = 1
    else:
        slova_podle_poctu_pismen[len(slovo)] += 1

serazena_slova = {klic: slova_podle_poctu_pismen[klic] for klic in sorted(slova_podle_poctu_pismen)}

#nejvetsi hodnota ze slovniku
nej_hodnota = 0
for hodnota in serazena_slova.values():
    if hodnota > nej_hodnota:
        nej_hodnota = hodnota
odsazeni = len('DÉLKA')

#graf, který se umí přizpůsobit podle nejvyžší hodnoty
print(f'{"DÉLKA":>{odsazeni}}|{"VÝSKYT":^{nej_hodnota}}|{"POČET"}')

print(oddelovac)

for klic, hodnota in serazena_slova.items():
    pocet_vyskytu_graficky = hodnota * '*'
    print(f'{klic:>{odsazeni}}|{pocet_vyskytu_graficky:<{nej_hodnota}}|{hodnota}')

print(oddelovac)
