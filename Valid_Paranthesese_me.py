"""Funktion"""


class Klammern:
    # Klasse Stapel initialisieren
    def __init__(self):
        self.klammern = []

    def istleer(self):
        # Abfrage ob der Stapel leer ist
        return len(self.klammern) == 0

    def schaue(self):
        # letzten Wert auf dem Stapel anschauen
        if self.istleer():
            return None
        return self.klammern[-1]

    def oben(self, klammer):
        # Wert auf den Stapel legen
        for z in range(len(klammer)):
            if klammer[z] in ["(", "[", "{"]:  # nur die öffnenden Klammern
                self.klammern.append(klammer[z])
            elif klammer[z] in [")", "]", "}"]:  # schließende Klammern
                # Abfrage für die Klammern
                if self.schaue() == "(" and klammer[z] == ")":
                    self.klammern.pop(-1)
                elif self.schaue() == "[" and klammer[z] == "]":
                    self.klammern.pop(-1)
                elif self.schaue() == "{" and klammer[z] == "}":
                    self.klammern.pop(-1)
                else:
                    return False
        return self.istleer()  # True=leer und False=nicht leer

    def löschen(self):
        return self.klammern.clear()


meine_klammern = Klammern()

# * Example 1
print("----")  # Hilfslinie für Terminal
s1 = "()"
# Ausgabe True
print(meine_klammern.oben(s1))
meine_klammern.löschen()


# * Example 2
print("----")  # Hilfslinie für Terminal
s2 = "()[]{}"
# Ausgabe True
print(meine_klammern.oben(s2))
meine_klammern.löschen()
# * Example 3
print("----")  # Hilfslinie für Terminal
s3 = "(]"


# Ausgabe False
print(meine_klammern.oben(s3))
meine_klammern.löschen()
# * Example 4
print("----")  # Hilfslinie für Terminal
s4 = "([])"

# Ausgabe True
print(meine_klammern.oben(s4))
meine_klammern.löschen()
