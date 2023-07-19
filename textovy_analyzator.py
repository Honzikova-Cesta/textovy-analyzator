"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jan Procházka
email: jan.prochazka92@gmail.com
discord: .honzikovacesta
"""

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

#seznam (datový typ=slovník) registrovaných uživatelů
registrovani_uzivatele = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

#uživatel zadá své jméno a heslo
zadane_jmeno = input('Zadejte své uživatelské jméno: ')
zadane_heslo = input('Zadejte své heslo: ')

#program zkontroluje jestli je jméno a heslo na seznamu registrovaných uživatelů
if zadane_jmeno in registrovani_uzivatele:
    if zadane_heslo == registrovani_uzivatele[zadane_jmeno]:
        print(f'Vítejte {zadane_jmeno}. Jste přihlášen a můžete analyzovat texty.')
    else:
        print('Špatně zadané heslo.')
else:
    print('Špatně zadané jméno.')

#volba textu ze zadaných možností a ošetření vyjímek (try/except jsem použil kvůli zadávání desetinných čísel které způsobovaly ValueError)
volba_textu = input('Pomocí čísla 1-3 zvolte text, který chcete analyzovat: ')
try:
    cislo = int(volba_textu)
    if cislo not in (1,2,3):
        print(f'Číslo není v možnostech. Ukončuji program!')
    else:
        print(f'Zvolili jste text číslo: {cislo}')
except ValueError:
    print('Špatně zadaná hodnota. Ukončuji program!')

#statistiky: 
#počet slov
#počet slov začínajících velkým písmenem
#počet slov psaných velkými písmeny
#počet slov psaných malými písmeny
#počet čísel (ne cifer)
#sumu všech čísel (ne cifer) v textu

zvoleny_text = TEXTS[cislo-1]
slova_textu = zvoleny_text.split()
pocet_slov = len(slova_textu)
print(slova_textu)
print(f'V textu je {pocet_slov} slov')

pocet_slov_velke_pismeno = 0
for slovo in slova_textu:
    if slovo[0].isupper() == True:
        pocet_slov_velke_pismeno += 1
print(f'{pocet_slov_velke_pismeno} slov má na začátku velké písmeno.')




