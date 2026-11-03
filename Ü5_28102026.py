"""
Übung 5: Der Freizeitpark-Manager 🎢 (Querbeet-Wiederholung)
Themen:
- Aufgabe 1: Variablen, Tupel-Unpacking, String-Methoden & f-Strings (Basic & Tupel)
- Aufgabe 2: Listen, Sets & Dictionaries (Lists, Sets & Dictionary)
- Aufgabe 3: Schleifen, Bedingungen & Funktionen (Controll_Structures & Functions)
- Aufgabe 4: Klassen, __init__, __str__ & Methoden (Klassen)
- Aufgabe 5: Warteschlange mit deque (Lineare Datenstrukturen)
"""

# * --- Aufgabe 1: Das Besucher-Ticket (Basic & Tupel) ---
# 1. Lege folgendes Tupel an: besucher_daten = ("  lUkAs  ", "mÜlLeR", 2008, 17.50)
# 2. Entpacke (Unpacking) das Tupel in 4 Variablen: vorname, nachname, geburtsjahr, ticketpreis
# 3. Bereinige vorname und nachname:
#    - Entferne Leerzeichen am Rand mit .strip()
#    - Formatiere beide so, dass nur der 1. Buchstabe groß ist mit .capitalize()
# 4. Berechne das alter im Jahr 2026.
# 5. Gib mit einem f-String aus: "Besucher: Lukas Müller (18 Jahre) - Ticketpreis: 17.5 Euro"
print("\n--- Aufgabe 1 ---")
besucher_daten = (" lUkAs ", "mÜlLeR", 2008, 17.50)
vorname = besucher_daten[0]  # Wert aus Index 0
nachname = besucher_daten[1]  # Wert aus Index 1
geburtsjahr = besucher_daten[2]  # wert aus Index 2
ticketpreis = besucher_daten[3]  # Wert aus Index 3

vorname = vorname.strip()  # Leerzeichen entfernen
vorname = vorname.capitalize()  # vordersten Buchstaben groß
nachname = nachname.capitalize()  # vordersten groß

aktjahr = 2026
alter = aktjahr - geburtsjahr  # Alter ausrechnen

print(f"{vorname} {nachname} ({alter} Jahre alt) - Ticketpreis: {ticketpreis} €")


# * --- Aufgabe 2: Attraktionen & Preise (Lists, Sets & Dictionary) ---
# 1. Gegeben ist diese Liste besuchter Fahrgeschäfte:
#    gefahren = ["Achterbahn", "Geisterbahn", "Achterbahn", "Wildwasserbahn", "Geisterbahn", "Riesenrad"]
# 2. Wandle die Liste in ein Set (einzigartige_fahrten) um und gib mit len() aus,
#    wie viele VERSCHIEDENE Attraktionen besucht wurden.
# 3. Erstelle ein Dictionary 'preise' mit folgenden Werten:
#    "Achterbahn": 5, "Geisterbahn": 3, "Wildwasserbahn": 4, "Riesenrad": 3
# 4. Füge dem Dictionary 'preise' nachträglich noch "Autoscooter" mit dem Preis 2 hinzu.
print("\n--- Aufgabe 2 ---")
# Liste aller gefahrenen Attraktionen (inklusive Duplikaten)
gefahren = [
    "Achterbahn",
    "Geisterbahn",
    "Achterbahn",
    "Wildwasserbahn",
    "Geisterbahn",
    "Riesenrad",
]
# Liste in ein Set umwandeln, um doppelte Einträge automatisch zu entfernen
einzigartige_fahrten = set(gefahren)
# Anzahl der unterschiedlichen Attraktionen mit len() ausgeben
print(f"Es wurden {len(einzigartige_fahrten)} verschieden Attraktionen besucht!")
# Dictionary mit den Einzelpreisen pro Attraktion anlegen
preise = {"Achterbahn": 5, "Geisterbahn": 3, "Wildwasserbahn": 4, "Riesenrad": 3}
# Nachträglich einen neuen Schlüssel-Wert-Eintrag hinzufügen
preise["Autoscooter"] = 2

# * --- Aufgabe 3: Gesamtkosten & Rabatt-Rechner (Controll_Structures & Functions) ---
# 1. Schreibe eine Funktion berechne_gesamtkosten(fahrten_liste, preis_dict, hat_vip_pass):
#    - Starte mit einer Variablen gesamt = 0
#    - Gehe mit einer for-Schleife durch fahrten_liste
#    - Prüfe mit if, ob die Fahrt im preis_dict enthalten ist, und rechne den Preis zu 'gesamt' dazu
#    - Nach der Schleife: Wenn hat_vip_pass True ist ODER gesamt > 15 ist, ziehe 3 Euro Rabatt ab
#    - Gib 'gesamt' mit return zurück
# 2. Rufe die Funktion mit (gefahren, preise, True) auf und gib das Ergebnis mit print() aus.
print("\n--- Aufgabe 3 ---")


def berechne_gesamtkosten(fahrten_liste, preis_dict, hat_vip_pass):
    # Startwert für die Gesamtsumme auf 0 setzen
    gesamt = 0
    # Jede einzelne Fahrt aus der Liste durchgehen
    for fahrten in fahrten_liste:
        # Prüfen, ob für diese Fahrt ein Preis im Dictionary hinterlegt ist
        if fahrten in preis_dict:
            # Preis aus dem Dictionary abrufen und zur Gesamtsumme addieren
            get_preis = preis_dict.get(fahrten)
            gesamt += get_preis
    # Nach der Schleife: Einmalig 3 Euro Rabatt abziehen bei VIP-Pass oder Summe über 15 Euro
    if hat_vip_pass == True or gesamt > 15:
        gesamt -= 3
    # Endbetrag zurückgeben
    return gesamt


# Funktion mit unseren Daten aufrufen und Ergebnis ausgeben
print(berechne_gesamtkosten(gefahren, preise, True), "Euro")


# * --- Aufgabe 4: Die Attraktions-Klasse (Klassen) ---
# 1. Erstelle eine Klasse 'Attraktion':
#    - __init__(self, name, mindestalter): speichert self.name, self.mindestalter und setzt self.ist_offen = True
#    - __str__(self): gibt zurück: "Attraktion: [name] (ab [mindestalter] Jahren)"
#    - Methode pruefe_einlass(self, alter):
#      Gibt True zurück, wenn self.ist_offen True ist UND alter >= self.mindestalter, sonst False.
# 2. Erstelle ein Objekt achterbahn = Attraktion("Achterbahn", 12)
# 3. Gib das Objekt mit print(achterbahn) aus und teste print(achterbahn.pruefe_einlass(18)).
print("\n--- Aufgabe 4 ---")


class Attraktion:
    # Konstruktor: Initialisiert Name, Mindestalter und setzt den Status standardmäßig auf offen
    def __init__(self, name, mindestalter):
        self.name = name
        self.mindestalter = mindestalter
        self.ist_offen = True

    # String-Darstellung: Bestimmt, was bei print(objekt) angezeigt wird
    def __str__(self):
        return f"Attraktion: {self.name} (ab {self.mindestalter} Jahren)"

    # Methode zur Einlasskontrolle: Prüft, ob geöffnet ist UND das Mindestalter erreicht wurde
    def pruefe_einlass(self, alter):
        if self.ist_offen == True and alter >= self.mindestalter:
            return True
        else:
            return False


# Neues Attraktions-Objekt erstellen
achterbahn = Attraktion("Achterbahn", 12)

# Objektbeschreibung und Einlassprüfung für eine 18-jährige Person ausgeben
print(achterbahn)
print(achterbahn.pruefe_einlass(18))


# * --- Aufgabe 5: Die Warteschlange an der Achterbahn (Lineare Datenstrukturen) ---
# 1. Importiere deque aus dem Modul collections (oder ganz oben in der Datei).
# 2. Erstelle eine Queue: warteschlange = deque(["Anna", "Ben", "Clara", "David"])
# 3. "Eva" stellt sich hinten an die Schlange an.
# 4. Solange die warteschlange nicht leer ist (while-Schleife):
#    - Hole die jeweils vorderste Person mit .popleft() heraus
#    - Gib aus: "[Person] darf jetzt einsteigen!"
print("\n--- Aufgabe 5 ---")
# deque für eine schnelle Warteschlange (First-In, First-Out) importieren
from collections import deque

# Warteschlange mit den ersten vier Personen initialisieren
warteschlange = deque(["Anna", "Ben", "Clara", "David"])
# Neue Person stellt sich ganz hinten an die Warteschlange an
warteschlange.append("Eva")

# Solange noch Personen in der Warteschlange stehen:
while warteschlange:
    # Vorderste Person aus der Schlange holen und entfernen
    person = warteschlange.popleft()
    # Einsteige-Meldung für diese Person ausgeben
    print(f"{person} darf jetzt einsteigen")
