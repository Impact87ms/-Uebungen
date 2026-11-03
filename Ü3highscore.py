"""Das Szenario: Der globale Highscore-Zähler 🏆
Stell dir vor, du möchtest ein kleines Spiel programmieren.
Der Highscore soll im gesamten Programm überall verfügbar sein, egal in welcher Funktion du dich gerade befindest.
1. Die globale Variable:
Du erstellst ganz oben im Code (außerhalb aller Funktionen) eine Variable namens high_score und setzt sie auf 1000.
2. Die erste Funktion (Ablesen):
Du schreibst eine Funktion zeige_highscore(). Diese soll einfach nur auf die globale Variable zugreifen und sie auf dem Bildschirm ausgeben.
3. Die zweite Funktion (Verändern):
Du schreibst eine Funktion neuer_rekord(). Diese Funktion soll den globalen high_score auf einen neuen Wert (z. B. 1500) anheben.
(Tipp für Python: Wenn eine Funktion eine globale Variable nicht nur lesen, sondern aktiv überschreiben soll, musst du Python in der Funktion explizit mit einem bestimmten Schlüsselwort sagen: „Achtung, ich meine die Variable von ganz oben!“)

Am Ende des Programms rufst du beide Funktionen nacheinander auf, um zu sehen, ob sich der Wert auf der „großen Anzeigetafel“ für das gesamte Programm dauerhaft verändert hat.
"""

# 1. Die globale Variable
high_score = 1000.00


# print(f"Der aktuelle Highscore ist: {high_score}")


def zeige_highscore():
    """Die erste Funktion (Ablesen)"""
    print(f"Der aktuelle Highscore ist: {high_score}")


def neuer_rekord():
    """Die zweite Funktion (Verändern)"""
    global high_score  # Zugriff auf die globale Variable
    high_score = float(input("Neuer Highscore: "))  # Neuer Wert für den Highscore
    print(f"Neuer Highscore: {high_score}")


zeige_highscore()  # Zeigt den aktuellen Highscore an

print("Es gibt einen neuen Rekord!")

neuer_rekord()  # Setzt einen neuen Highscore

zeige_highscore()  # Zeigt den aktualisierten Highscore an
