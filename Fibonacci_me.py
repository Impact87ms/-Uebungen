"""
PSEUDOCODE (Fibonacci-Folge):

TEIL 1 - Grundprinzip (Naiver Ansatz ohne Gedächtnis):

FUNKTION BerechneFibonacci(n):

    1. SCHRITT - Basisfälle (Abbruchbedingungen) prüfen:
    WENN n gleich 0 ist:
        GIB 0 ZURÜCK
    WENN n gleich 1 ist:
        GIB 1 ZURÜCK

    2. SCHRITT - Aus den beiden Vorgängern berechnen:
    Berechne den ersten Vorgänger über BerechneFibonacci(n minus 1)
    Berechne den zweiten Vorgänger über BerechneFibonacci(n minus 2)
    GIB die Summe aus beiden Vorgängern ZURÜCK


TEIL 2 - Optimierter Ansatz mit Gedächtnis (Notizzettel / Zwischenspeicher):

Lege einen Notizzettel (Zwischenspeicher) an, in dem schon steht:
    Position 0 hat den Wert 0
    Position 1 hat den Wert 1

FUNKTION BerechneFibonacciMitGedächtnis(n):

    1. SCHRITT - Erst auf dem Notizzettel nachschauen:
    WENN n SCHON auf dem Notizzettel eingetragen ist:
        GIB den gespeicherten Wert für n direkt ZURÜCK

    2. SCHRITT - Falls noch nicht bekannt, einmal berechnen & aufschreiben:
    Berechne das Ergebnis als Summe aus:
        BerechneFibonacciMitGedächtnis(n minus 1) PLUS BerechneFibonacciMitGedächtnis(n minus 2)

    Trage dieses neue Ergebnis für Position n auf dem Notizzettel ein

    3. SCHRITT - Ergebnis liefern:
    GIB den eingetragenen Wert für n ZURÜCK
"""

# * Variante 1: Naiver rekursiver Ansatz (ohne Zwischenspeicher)


def berechneFibonacci(n):
    # Basisfälle (Abbruchbedingungen): F(0) = 0 und F(1) = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        # Rekursiver Aufruf für die beiden vorherigen Positionen (n - 1) und (n - 2)
        ersterVor = berechneFibonacci(n - 1)
        zweiterVor = berechneFibonacci(n - 2)
        # Summe der beiden Vorgänger bilden und zurückgeben
        summeersterzweiter = ersterVor + zweiterVor
    return summeersterzweiter


# * Variante 2: Optimierter Ansatz mit Gedächtnis (Memoization / Dictionary)

# Zwischenspeicher (Notizzettel) mit den beiden bekannten Startwerten
speicher = {0: 0, 1: 1}


def berechneFibonaccimitSpeicher(n):
    # 1. Prüfen, ob das Ergebnis für n bereits berechnet und gespeichert wurde
    if n in speicher:
        return speicher[n]
    else:
        # 2. Falls noch nicht im Speicher: einmalig aus den beiden Vorgängern berechnen
        summe_n_neu = berechneFibonaccimitSpeicher(
            n - 1
        ) + berechneFibonaccimitSpeicher(n - 2)
        # Neues Ergebnis für Position n im Dictionary merken
        speicher[n] = summe_n_neu
    # 3. Berechnetes Ergebnis zurückgeben
    return summe_n_neu


# * Example 1
print("---1.---")
n = 2
# Output 1
print(berechneFibonacci(2))
print(berechneFibonaccimitSpeicher(10))

# * Example 2
print("---2.---")
n = 3
# Output 2
print(berechneFibonacci(3))
print(berechneFibonaccimitSpeicher(20))
# * Example 3

print("---3.---")
n = 4
# Output 3
print(berechneFibonacci(4))
print(berechneFibonaccimitSpeicher(100))
