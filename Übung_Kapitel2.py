# * 1. Steckbrief
print("---1.---")
"""Bevor der Roboter eingeschaltet wird, musst du seine Grunddaten festlegen. Überlege dir für deinen Roboter:

Der Name: Wie lautet sein Name? (Ein schönes Wort / Text)
Die Schrauben: Wie viele Schrauben wurden insgesamt verbaut? (Eine ganze Zahl)
Das Gewicht: Wie schwer ist der Roboter in Kilogramm? (Eine Zahl mit Kommastelle)
Die Rakete: Hat er eine Geheim-Rakete auf dem Rücken? (Nur die klare Antwort „Ja / Wahr“ oder „Nein / Falsch“)"""

name_roboter = "Jürgen"
schrauben = 250
gewicht = 115.25
rakete = True

print(
    f"Mein Name ist {name_roboter}, ich besteh aus {schrauben} Schrauben und bin {gewicht}kg schwer."
)

# * 2. Taschen, Pässe und Sammelkisten
print("---2.---")
"""Dein Roboter braucht verschiedene Ablagen und Fächer für seine Abenteuer:

Der Rucksack (Geordnete Liste):
Lege 4 Werkzeuge oder Spielsachen in seinen Rucksack (zum Beispiel: Schraubenzieher, Taschenlampe, Gummiente, Kompass).
In diesen Rucksack dürfen Dinge in einer festen Reihenfolge hineingesteckt, neue Sachen dazugepackt oder kaputte Dinge wieder herausgenommen werden.
Die Ausweis-Plakette (Feste, unveränderliche Karte):
Notiere sein Baujahr und die Seriennummer fest auf einer Metallplakette. Diese Werte sind wie in Stein gemeißelt und dürfen sich im Nachhinein niemals mehr verändern!
Der Zauberstein-Beutel (Sammlung ohne doppelte Dinge):
Der Roboter sammelt im Garten bunte Zaubersteine. In diesem Beutel darf jeder Stein (z. B. Roter Rubin, Blauer Saphir) nur ein einziges Mal vorkommen. Wenn er versehentlich einen zweiten roten Stein hineinstecken will, rollt dieser von selbst wieder heraus!
Das Roboter-Tagebuch (Steckbrief-Lexikon mit Begriff & Bedeutung):
Erstelle ein Verzeichnis, in dem zu jedem Stichwort genau eine passende Information zugeordnet ist. Zum Beispiel:
Was ist sein Lieblings-Treibstoff?
Wie lautet sein Geheim-Code?
An welchem Lieblings-Ort steht seine Ladestation?"""

rucksack = ["Schraubenzieher", "Kompass", "Taschenlampe", "Messer"]
ausweis = (1337, 1987)
zauber_beutel = {"roter Rubin", "blauer Saphier"}
tagebuch = {"Treibstoff": "High-Voltage", "Geheimcode": 1904, "Ladestation": "Infinity"}

print("Inhalt Rucksack:\n", rucksack)
print(f"Meine Plakette: {ausweis[0]} Seriennummer, {ausweis[1]} Baujahr")
print("Inhalt Zauberbeutel:", zauber_beutel)
print(
    f"Lieblingsgetränk: {tagebuch['Treibstoff']}, Code: {tagebuch['Geheimcode']}, Lieblingsstation: {tagebuch['Ladestation']}"
)

# * 3. Schlaue Entscheidungen
print("---3.---")
"""Dein Roboter muss in verschiedenen Situationen selbstständig nachdenken und reagieren können:

Die Akku-Prüfung:
Wenn sein Akku-Stand unter 20 Prozent fällt, soll er sofort Alarm schlagen („Achtung, ich muss schlafen!“) und selbstständig zur Ladestation rollen.
Wenn der Akku aber zwischen 20 und 80 Prozent liegt, soll er fröhlich rufen: „Alles super, lass uns spielen!“.
Wenn der Akku sogar über 80 Prozent voll ist, darf er in den schnellen Turbo-Flitz-Modus schalten!"""

akku_stand = 5
turbo_modus = False
alarm_modus = False

if akku_stand >= 80:
    turbo_modus = True
    print("Turbo_Modus aktiviert!!", turbo_modus)

if akku_stand < 80 and akku_stand >= 20:
    print("Alles super, lass uns spielen!")

if akku_stand < 20:
    alarm_modus = True
    print("Achtung, ich muss schlafen!", alarm_modus)

# * 4. Fleißige Wiederholungen
print("---4.---")
"""Manche Dinge muss der Roboter der Reihe nach oder wiederholt ausführen:

Der Werkzeug-Check (Für jedes Teil im Rucksack):
Nimm den Rucksack aus Level 2 zur Hand.
Der Roboter soll der Reihe nach jedes einzelne Werkzeug herausholen,
kurz daran schnuppern, den Namen des Gegenstands laut aufsagen und
es dann wieder sauber einpacken – vom ersten bis zum allerletzten Ding."""
print("-4a-")
for item in range(len(rucksack)):
    item1 = rucksack.pop(0)
    print(f"*schnuppern*... der Gegenstand ist {item1}")
    rucksack.append(item1)
print("In dem Rucksack sind folgende Items:", rucksack)

"""Das Akku-Aufladen (Solange bis voll):
Solange der Akku noch nicht bei 100 Prozent angekommen ist,
soll er jede Sekunde einen Strom-Schluck trinken und den Zähler um eins erhöhen.
Erst wenn die 100 erreicht ist, darf er mit dem Trinken aufhören."""
print("-4b-")
schluck = 0
if akku_stand < 100:
    for schluck in range(100 - akku_stand):
        schluck += 1
        print("Der Ladestand ist:", akku_stand + schluck)
    else:
        akku_stand = 100
        print("Ich bin voll aufgeladen!!!")

# * 5. Der Zaubertrick-Befehl
print("---5.---")
"""Bringe deinem Roboter einen festen Kunststück-Befehl bei
– wie ein kleines Zauber-Rezept, das du jederzeit wieder abrufen kannst:

Der Befehl heißt: „Super-Salto“
Was er als Zutat braucht: Du musst ihm sagen,
wie viele Umdrehungen er in der Luft machen soll (zum Beispiel 2 oder 3 Umdrehungen).
Was er tut: Er springt mit Schwung in die Luft,
dreht sich genau so oft wie gewünscht um die eigene Achse und ruft bei der Landung laut „Tadaaa!“.
Was er zurückgibt: Eine Erfolgs-Nachricht an dich,
ob der Salto geglückt ist oder ob ihm etwas schwindelig geworden ist."""


def super_salto(salto):
    if salto <= 10:
        return f"Ich springe und mache {salto} Umdrehungen.\nTadaaaa!!!"
    else:
        return "Da wird mir schwindlig :P"


print(super_salto(10))

# * 6. Der große Meisterbauplan
print("---6.---")
"""Bringe nun alle Einzelteile zu einem großen Ganzen zusammen!

Entwirf einen Gesamt-Bauplan für deine Roboter-Rasse.
Der Bauplan legt fest, welche Eigenschaften jeder frisch gebaute Roboter von Geburt an besitzt (Name, Akku-Stand, Rucksack, Tagebuch).
Außerdem stehen im Bauplan alle Aktionen, die jeder Roboter von Natur aus beherrscht (Laufen, Schlafen, Laden, Kunststück vorführen).
Erschaffe am Ende aus diesem einen einzigen Bauplan zwei verschiedene Roboter-Geschwister (zum Beispiel Roboter „Blinki“ in Blau und Roboter „Zirpi“ in Gelb)."""


class Roboter_Rasse:
    def __init__(self, name, akkustand, rucksack, tagebuch):
        self.name = name
        self.akkustand = akkustand
        self.rucksack = rucksack
        self.tagebuch = tagebuch

    def akku_stand(
        self,
    ):
        if self.akkustand >= 80:
            turbo_modus = True
            print("Turbo_Modus aktiviert!!", turbo_modus)

        elif self.akkustand < 80 and self.akkustand >= 20:
            print("Alles super, lass uns spielen!")

        else:
            self.akkustand < 20
            alarm_modus = True
            print("Achtung, ich muss schlafen!", alarm_modus)

    def super_salto(self, salto):
        if salto <= 10:
            print(f"Ich springe und mache {salto} Umdrehungen.\nTadaaaa!!!")
        else:
            print("Da wird mir schwindlig :P")


roboter1 = Roboter_Rasse("Blinki", 80, ["Messer"], {"Ladestation": "Infinity"})
roboter2 = Roboter_Rasse("Zirpi", 55, ["Schwert"], {"Lieblingsgetränk": "Amperepower"})
roboter1.akku_stand()
roboter2.akku_stand()
roboter1.super_salto(5)
roboter2.super_salto(23)
