"""
Lösungsansatz (Words from same keyboard row):
Man prüft für jedes Wort in der Liste, ob alle seine Buchstaben aus nur einer
einzigen Reihe der amerikanischen Tastatur stammen.
- Sind alle Buchstaben des Wortes in einer Reihe enthalten?
    - ja: Originalwort an die neue Ergebnisliste anhängen
    - nein: Wort überspringen und das nächste Wort prüfen
- Umsetzung mit Sets & Teilmengen (.issubset()):
  Das Wort wird für den Vergleich kleingeschrieben und in ein Set umgewandelt.
  Ist dieses Buchstaben-Set eine Teilmenge der 1., 2. oder 3. Reihe, ist es gültig.
"""

# Die drei Tastaturreihen als Sets aus einzelnen Kleinbuchstaben anlegen
first_row, second_row, third_row = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")


def ausgabe_wort(words):
    # Ergebnisliste für alle gültigen Wörter vorbereiten
    neue_wörter_liste = []

    # Jedes Wort einzeln durchgehen
    for word in words:
        # Für den Abgleich kleinschreiben und in ein Buchstaben-Set umwandeln
        word_set = set(word.lower())

        # Prüfen, ob alle Buchstaben komplett in der 1., 2. ODER 3. Reihe liegen
        if (
            word_set.issubset(first_row)
            or word_set.issubset(second_row)
            or word_set.issubset(third_row)
        ):
            # Das Wort in seiner Originalschreibweise speichern
            neue_wörter_liste.append(word)

    # Fertige Liste zurückgeben (bleibt automatisch leer, falls kein Wort passt)
    return neue_wörter_liste


# * Example 1
print("---1.---")
words = ["Hello", "Alaska", "Dad", "Peace"]
# Output ["Alaska", "Dad"]
print(ausgabe_wort(words))
# * Example 2
print("---2.---")
words = ["omk"]
# Output []
print(ausgabe_wort(words))
# * Example 3
print("---3.---")
words = ["asdf", "sfd"]
# Output ["asdf", "sfd"]
print(ausgabe_wort(words))
