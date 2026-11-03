# * Aufgabe 1:
print("\n---Aufgabe 1---")
# Variablen anlegen:
vorname = "mAx"
nachname = "mUsTeRmAnN"
geburtsjahr = 1998
aktuelles_jahr = 2006
print(
    "Vorname:",
    vorname,
    "Nachname:",
    nachname,
    "GJ: ",
    geburtsjahr,
    "AJ:",
    aktuelles_jahr,
)
# Alter berechnen
alter = aktuelles_jahr - geburtsjahr
print("Alter:", alter)
# Kuerzel erstellen und alles in groß
kuerzel = vorname[0] + nachname[0:3]
kuerzel = kuerzel.upper()
print(kuerzel)
# Beide Namen fangen mit Großbuchstaben an
vorname = vorname.capitalize()
nachname = nachname.capitalize()
print(vorname, nachname)
# Karte
laenge_name = len(vorname + nachname)
print(
    f"--- Profilkarte ---\nName: {vorname} {nachname}\nALter: {alter} Jahre\nKürzel: {kuerzel}\nNamenslänge: {laenge_name} Zeichen (ohne Leerzeichen)"
)

# * Aufgabe 2
print("\n---Aufgabe 2---")
# Variablen
alter = 20
hat_studentenausweis = True
ist_begleitet = False
ticket_nummer = 1042
# Boolsche Bedingung
darf_rein = alter >= 18 or alter >= 16 and not ist_begleitet
erhaelt_rabatt = alter < 25 and hat_studentenausweis
gewinner_ticket = ticket_nummer % 2 >= 1000

print("Einlass gewährt! Viel Spaß:", darf_rein)

# * Augabe 3
print("\n----Aufgabe 3---")
# Variablen
einkaufsliste = ["Äpfel", "Milch", "Brot", "Kaffee", "Käse"]
# Ausgabe 1. und letztes Element
print("Liste:", einkaufsliste[0], einkaufsliste[-1])
# Schokolade hinzufügen
einkaufsliste.append("Schokolade")
# Banane an 2. Stelle
# einkaufsliste = einkaufsliste.insert(1, "Banane")
# Artikel entfernen
# einkaufsliste = einkaufsliste.remove("Brot")
# Gekauft
# gekauft = einkaufsliste.pop(-1)
print("Ist Kaffee auf der Liste?", "Kaffee" in einkaufsliste)
