"""Funktionsaufbau"""

from collections import deque


class timetobuy:
    # Initialisierung
    def __init__(self):
        self.karten = deque()
        self.counter = 0

    # Prüfen ob Liste leer ist
    def istleer(self):
        return len(self.karten) == 0

    # Hinzufügen zur Warteschlange
    def enqueue(self, ticket):
        for position, kauft in enumerate(ticket):
            self.karten.append([position, kauft])

    # Entfernen aus Warteschlange
    def dequeue(self):
        if self.istleer():
            return "Keine Tickets!!!"
        return self.karten.popleft()

    # vorderstes Element anschauen
    def schaue(self):
        if self.istleer():
            return "Keine Tickets!!!"
        return self.karten[0]

    # Funktion zum Bearbeiten der Schlange
    def kaufen(self, k):
        # Wiederholen, solange die Warteschlange nicht leer ist
        while not self.istleer():
            kunde1 = self.dequeue()  # 1. Kunden "bedienen"
            kunde1[1] -= 1  # Tickets um 1 verringern
            self.counter += 1  # Zähler um 1 erhöhen
            # vergleichen ob gesuchter Kunde alle Tickets hat
            if kunde1[0] == k and kunde1[1] == 0:
                return self.counter  # Endstand des Zählers
            if kunde1[1] > 0:  # so lange hinten anstellen, wie Tickets benötigt werden
                self.karten.append(kunde1)

    # Warteschlangen und Zähler zurücksetzen
    def löschen(self):
        self.karten.clear()
        self.counter = 0


my_tickets = timetobuy()

# * Example 1
print("/--------/")  # Hilfslinie für Terminal Ausgabe
tickets = [2, 3, 2]  # Anzahl Tickets die jede Person braucht
k = 2  # Indexnummer des Kunden
# Ausgabe soll 6 sein
my_tickets.enqueue(tickets)
print(my_tickets.karten)
print(my_tickets.kaufen(k))
my_tickets.löschen()
# * Example 2
print("/--------/")  # Hilfslinie für Terminal Ausgabe
tickets2 = [5, 1, 1, 1]  # Anzahl Tickets die jede Person braucht
k = 0  # Indexnummer des Kunden
# Ausgabe soll 8 sein
my_tickets.enqueue(tickets2)
print(my_tickets.karten)
print(my_tickets.kaufen(k))
my_tickets.löschen()
