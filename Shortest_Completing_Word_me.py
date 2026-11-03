"""
PSEUDOCODE (Shortest Completing Word):

FUNKTION ausgabewort(Kennzeichen, WörterListe):

    1. SCHRITT - Kennzeichen vorbereiten & Buchstaben zählen:
    Wandle Kennzeichen komplett in Kleinbuchstaben um
    Lege ein leeres Dictionary (buchstabenzähler) an

    FÜR JEDES Zeichen IM kleingeschriebenen Kennzeichen:
        WENN Zeichen ein Buchstabe ist (keine Zahl, kein Leerzeichen):
            WENN Zeichen SCHON IM buchstabenzähler steht:
                Erhöhe den Wert dieses Zeichens im buchstabenzähler um 1
            SONST:
                Setze den Wert dieses Zeichens im buchstabenzähler auf 1


    2. SCHRITT - Alle Wörter prüfen und das kürzeste passende merken:
    Setze kürzesteswort auf None (noch kein Treffer gefunden)

    FÜR JEDES wort IN WörterListe:
        Setze wortpasst auf True

        FÜR JEDEN buchstabe, benötigte_anzahl IN buchstabenzähler:
            WENN (Anzahl von buchstabe im aktuellen wort) KLEINER ALS benötigte_anzahl:
                Setze wortpasst auf False
                Brich diese innere Schleife ab

        WENN wortpasst immer noch True ist:
            WENN kürzesteswort noch None ist ODER (Länge von wort) KLEINER ALS (Länge von kürzesteswort):
                Setze kürzesteswort = wort


    3. SCHRITT - Ergebnis zurückgeben:
    GIB kürzesteswort ZURÜCK
"""


def ausgabewort(plate, wörter):
    # --- Schritt 1: Kennzeichen aufbereiten und Buchstaben zählen ---
    # Groß-/Kleinschreibung vereinheitlichen
    new_plate = plate.lower()
    # Dictionary (Hash Map) zum Zählen der benötigten Buchstaben anlegen
    buchstabenzähler = {}

    for c in new_plate:
        # Nur echte Buchstaben berücksichtigen (Zahlen und Leerzeichen ignorieren)
        if c.isalpha():
            if c in buchstabenzähler:
                buchstabenzähler[c] += 1
            else:
                buchstabenzähler[c] = 1

    # --- Schritt 2: Jedes Wort prüfen und das kürzeste gültige Wort merken ---
    kürzesteswort = None

    for wort in wörter:
        # Zunächst annehmen, dass das aktuelle Wort alle Buchstaben enthält
        wortpasst = True

        # Jeden benötigten Buchstaben samt seiner Mindestanzahl überprüfen
        for buchstabe, anzahl in buchstabenzähler.items():
            # Kommt der Buchstabe im Wort seltener vor als benötigt, fällt das Wort raus
            if wort.count(buchstabe) < anzahl:
                wortpasst = False
                break

        # Wenn das Wort alle Bedingungen erfüllt hat:
        if wortpasst == True:
            # Speichern, falls es der erste Treffer ist oder echt kürzer als der bisherige
            # (Durch '<' bleibt bei gleicher Länge automatisch das zuerst gefundene Wort erhalten)
            if kürzesteswort == None or len(wort) < len(kürzesteswort):
                kürzesteswort = wort

    # --- Schritt 3: Kürzestes passendes Wort zurückgeben ---
    return kürzesteswort


# * Example 1
print("---1.---")
licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
# Output "steps"
print(ausgabewort(licensePlate, words))
# * Example 2
print("---2.---")
licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
# Output "pest"
print(ausgabewort(licensePlate, words))
