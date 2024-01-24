import datetime
from subprocess import call
import os

try:
    os.mkdir("Predradniky",mode=0o777,dir_fd=None)
except FileExistsError:
    pass


call("cls", shell = True)

cas = str(datetime.date.today())

cas = cas.replace("-", "")
errp = "Vstupní soubor neobsahuje žádné závady předřadníků."
errz = "Vstupní soubor neobsahuje žádné závady zdrojů."
predradniky = []
zdroje = []
pocet_zavad_zdroje = 0
pocet_zavad_predradniky = 0

with open ("input_file.txt", "r") as input_file:
    readings = input_file.readlines()
readings.sort()    

for i in readings:
    if "DGS" not in i:  
        if "Porucha zdroje" in str(i):
            print (".", end = "")
            zdroje.append(i)
            pocet_zavad_zdroje = pocet_zavad_zdroje + 1
        elif "Porucha předřadníku" in str(i):
            print (".", end = "")
            predradniky.append(i)
            pocet_zavad_predradniky = pocet_zavad_predradniky +1
            

predradnik_printable = ""
for i in predradniky:
    predradnik_printable = (predradnik_printable + "".join(i))
    
zdroj_printable = ""
for i in zdroje:
    zdroj_printable = (zdroj_printable + "".join(i))

print("\nHotovo")

if predradnik_printable != "":
    cesta_predradnik = os.path.abspath("Predradniky")+"\\Predradniky_"+str(cas)+".txt"
    try:
        with open(cesta_predradnik, "w+") as predradnik_vysledek:
            predradnik_vysledek.write(predradnik_printable)
            print ("\nUloženo jako: ", os.path.abspath(cesta_predradnik))
    except FileNotFoundError:
        print ("\nNEULOŽENO: Soubor nenalezen.")
            
else:
    print ("\n" + errp)

if zdroj_printable != "":
    cesta_zdroje = os.path.abspath("Predradniky")+"\\Zdroje_"+str(cas)+".txt"
    try:
        with open(cesta_zdroje, "w+") as zdroje_vysledek:
            zdroje_vysledek.write(zdroj_printable)
            print ("Uloženo jako: ",os.path.abspath(cesta_zdroje))
    except FileNotFoundError:
        print ("\nNEULOŽENO: Soubor nenalezen.")
else:
    print ("\n" + errz)

print ("\nPočet vadných předřadníků: ",pocet_zavad_predradniky, "\nPočet vadných trubic: ", pocet_zavad_zdroje, "\nCelkem závad: ",pocet_zavad_zdroje+pocet_zavad_predradniky)

input("\nENTER pro ukončení")
