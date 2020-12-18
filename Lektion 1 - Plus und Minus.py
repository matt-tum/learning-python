"""
Building up dictionary
"""

zahlensystem = {
    "null": 0,
    "ein": 1, 
    "eins": 1,
    "zwei": 2, 
    "drei": 3, 
    "vier": 4, 
    "fünf": 5, 
    "sechs": 6, 
    "sieben": 7, 
    "acht": 8, 
    "neun": 9, 
    "zehn": 10, 
    "elf": 11, 
    "zwölf": 12,
    "dreizehn": 13,
    "vierzehn": 14,
    "fünfzehn": 15,
    "sechzehn": 16,
    "siebzehn": 17,
    "achtzehn": 18,
    "neunzehn": 19,
    "zwanzig": 20, 
    "dreißig": 30, 
    "vierzig": 40, 
    "fünfzig": 50, 
    "sechzig": 60, 
    "siebzig": 70, 
    "achtzig": 80, 
    "neunzig": 90, 
    "hundert": 100, 
    "tausend": 1000
    }

zahlensystem_umgekehrt = {
    0: "null",
    1: "eins",
    2: "zwei",
    3: "drei",
    4: "vier",
    5: "fünf",
    6: "sechs",
    7: "sieben",
    8: "acht",
    9: "neun",
    10: "zehn",
    11: "elf",
    12: "zwölf",
    13: "dreizehn",
    14: "vierzehn",
    15: "fünfzehn",
    16: "sechzehn",
    17: "siebzehn",
    18: "achtzehn",
    19: "neunzehn",
    20: "zwanzig",
    30: "dreißig",
    40: "vierzig",
    50: "fünfzig",
    60: "sechzig",
    70: "siebzig",
    80: "achtzig",
    90: "neunzig",
    100: "hundert",
    1000: "tausend",
}

""" 
functions
"""

def kodieren (wort):

    """
    initialising variables / lists
    """

    zahl = 0
    vorzeichen = 0
    tausender = 0
    hunderter = 0
    string = wort   # copy parameter into local variable
    string_zerlegt = []
    ergebnis = []

    """
    break-down string into parts
    """

    string = string.strip()

    vorzeichen, string = pruefeVorzeichen(string)
    tausender, string = ueberHunderter ("tausend", string)
    hunderter, string = ueberHunderter ("hundert", string)
    zahl += hunderter + tausender 

    # print (string)
    
    string_zerlegt = string.split("und")
    
    for zahlwort in string_zerlegt:
        if zahlwort in zahlensystem: 
            ergebnis.append(zahlensystem[zahlwort])

    for z in range(0,len(ergebnis)):    # aufaddieren der Zahlen in Ergebnisliste
        zahl += ergebnis[z]
    
    zahl = vorzeichen * zahl

    return (zahl)

def ueberHunderter(stellenwort, zahlenwort):
    
    if stellenwort in zahlenwort:
        x = zahlenwort[0:(zahlenwort.find(stellenwort)+len(stellenwort))]
        gekZahlenwort = zahlenwort.replace(x,"")
        x = x.replace(stellenwort,"")
        if x in zahlensystem:
            zwischenergebnis = zahlensystem[x] * zahlensystem[stellenwort]
        else:
            zwischenergebnis = 1 * zahlensystem[stellenwort]
    else:
        zwischenergebnis = 0 * zahlensystem[stellenwort]
        gekZahlenwort = zahlenwort

    return zwischenergebnis, gekZahlenwort

def pruefeVorzeichen (zahlenwort):

    if "minus" in zahlenwort:
        gekZahlenwort = zahlenwort.replace("minus ","")
        vorzeichen = -1
    elif "plus" in zahlenwort:
        gekZahlenwort = zahlenwort.replace("plus ","")
        vorzeichen = 1
    else:
        vorzeichen = 1 
        gekZahlenwort = zahlenwort

    return vorzeichen, gekZahlenwort

def dekodieren (zahl):

    wort = ""

    if zahl < 0: 
        wort += "minus "
        zahl = zahl * -1

    # Vorzeichen muss vorher rausgenommen werden aus zahl

    zahl, tausender = ueberZweistellig (zahl, 1000)
    zahl, hunderter = ueberZweistellig (zahl, 100)

    wort += tausender + hunderter

    # Ab hier sollte zahl zweistellig sein

    if zahl in zahlensystem_umgekehrt:
        wort += zahlensystem_umgekehrt[zahl]
        zahl = 0
        return wort
    
    for i in range (21, 92, 10):   # überprüfe, ob Teil der Folge [21, 31, …], um "einund" einzufügen
        if zahl == i:
            wort += "einund" + zahlensystem_umgekehrt[i-1]
            zahl = 0
            return wort

    if zahl // 10 > 1:
        wort += zahlensystem_umgekehrt[zahl%10] + "und" + zahlensystem_umgekehrt[zahl//10*10]
        zahl = 0
    
    return wort


def ueberZweistellig (zahl, zahlenstelle):

    zwischenergebnis = ""

    if zahl // zahlenstelle > 1:
        zwischenergebnis += zahlensystem_umgekehrt[zahl//zahlenstelle] + zahlensystem_umgekehrt[zahlenstelle]
    elif zahl // zahlenstelle == 1:
        zwischenergebnis += "ein" + zahlensystem_umgekehrt[zahlenstelle]
    
    zahlRest = zahl%zahlenstelle

    return (zahlRest, zwischenergebnis)

def plusminus(term):
    
    teilTerm = ""
    teilZahl = 0
    termZahlen = []
    plusminus = term.split(" ")

    for i in range (len(plusminus)):
        if plusminus[i] == "minus":
            teilTerm += "minus "
        elif plusminus[i] == "plus":
            continue
        else: 
            teilTerm += plusminus[i]
            teilZahl = kodieren (teilTerm)
            termZahlen.append(teilZahl)
            teilZahl = 0
            teilTerm = ""

    ergebnisBerechnung = 0
    ergebnisAusgabe = ""

    for i in range (len(termZahlen)):
        ergebnisBerechnung += termZahlen[i]

    ergebnisAusgabe = dekodieren (ergebnisBerechnung)

    return ergebnisAusgabe, ergebnisBerechnung

"""
programme
"""

# wort = "minus zweihundertachtzig"
# zahl = kodieren (wort)
# print (zahl)

# zahl = 121
# wort = dekodieren (zahl)
# print ("Dekodierung erfolgreich: " + wort)

print ("> Willkommen beim Programm 'PlusMinus'. Es erlaubt das einfache Rechnen mit deutschen Hauptzahlwörtern. \n> Das Programm beherrscht alle Zahlen zwischen -9999 und 9999 sowie die Grundrechenarten Plus und Minus.")
term = input("Gebe einen Term ein: ")       # Todo: Handling für orthographische Fehler bei den Hauptzahlwörtern, Fehlen von Leerzeichen als Trennzeichen

# Clean-up of input
term.strip().lower()
while term.count("  ") > 0:
    term = term.replace("  ", " ")

# term = "minus elf plus tausendachtzehn minus tausend"
simpleArithmetik, simpleArithmetikZahl = plusminus(term)
simpleArithmetikZahl = str (simpleArithmetikZahl)
print ("ERGEBNIS: " + simpleArithmetik + " (" + simpleArithmetikZahl + ")")



