"""
PSEUDOCODE (Check if Path Exists in Graph):

FUNKTION ExistiertPfad(n, KantenListe, Start, Ziel):

    1. SCHRITT - Straßenkarte (Nachbarschafts-Übersicht) aufbauen:
    Lege ein leeres Dictionary (NachbarnKarte) an
    FÜR JEDE KnotenNummer VON 0 BIS n minus 1:
        Lege in NachbarnKarte für KnotenNummer eine leere Liste an

    FÜR JEDE Verbindung (u, v) IN KantenListe:
        Hänge v an die Nachbarn-Liste von u in NachbarnKarte an
        Hänge u an die Nachbarn-Liste von v in NachbarnKarte an (beide Richtungen!)


    2. SCHRITT - Wegsuche mit Warteschlange und Besucht-Set vorbereiten:
    Erstelle eine Warteschlange (deque), in der zu Beginn nur Start liegt
    Erstelle ein Set (Besucht), in dem zu Beginn nur Start liegt


    3. SCHRITT - Nachbarn Schritt für Schritt abklappern:
    SOLANGE Warteschlange nicht leer ist:
        Hole den vordersten Knoten (AktuellerKnoten) aus der Warteschlange (.popleft())

        WENN AktuellerKnoten gleich Ziel ist:
            GIB True ZURÜCK (Ziel erreicht!)

        FÜR JEDEN Nachbar IN NachbarnKarte an der Stelle AktuellerKnoten:
            WENN Nachbar NOCH NICHT in Besucht steht:
                Füge Nachbar zu Besucht hinzu
                Hänge Nachbar hinten an Warteschlange an


    4. SCHRITT - Kein Weg gefunden:
    (Wenn die Warteschlange komplett leer gelaufen ist, ohne auf Ziel zu treffen)
    GIB False ZURÜCK


AUSGABE IM TERMINAL:
Rufe ExistiertPfad(n, edges, source, destination) innerhalb von print() für beide Beispiele auf
"""

from collections import deque


def ExistiertPfad(n, KantenListe, Start, Ziel):
    # * Schritt 1: Straßenkarte (Nachbarschafts-Dictionary) aufbauen
    nachbarnkarte = {}
    # Für jeden Knoten von 0 bis n - 1 eine leere Nachbarn-Liste anlegen
    for z in range(n):
        nachbarnkarte[z] = []
    # Jede Kante [u, v] in beide Richtungen eintragen (ungerichteter Graph)
    for u, v in KantenListe:
        nachbarnkarte[u].append(v)
        nachbarnkarte[v].append(u)
    print(f"Die Nachbarn sind:", nachbarnkarte)  # nur zur Veranschaulichung
    # * Schritt 2: Warteschlange (Breitensuche) und Besucht-Set mit Startknoten initialisieren
    warteschlange = deque([Start])
    besucht = set([Start])

    # * Schritt 3: Knoten und ihre Nachbarn Schritt für Schritt durchsuchen
    while len(warteschlange) > 0:
        # Vordersten Knoten aus der Warteschlange holen
        knoten = warteschlange.popleft()
        # Prüfen, ob wir am Ziel angekommen sind
        if knoten == Ziel:
            return True
        # Alle direkten Nachbarn des aktuellen Knotens durchgehen
        for nachbar in nachbarnkarte[knoten]:
            # Nur Nachbarn besuchen, die wir vorher noch nicht gesehen haben
            if nachbar not in besucht:
                besucht.add(nachbar)
                warteschlange.append(nachbar)

    # * Schritt 4: Warteschlange ist leer und das Ziel wurde nicht erreicht
    return False


# * Example 1
print("---1.---")
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
# Output True
print(f" Existiert ein Pfad?", ExistiertPfad(n, edges, source, destination))

# * Example 2
print("---2.---")
n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5
# Output False
print(f" Existiert ein Pfad?", ExistiertPfad(n, edges, source, destination))
