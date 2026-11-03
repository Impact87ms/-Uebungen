"""Übung 1: Das Gaming-Profil 🎮
• Variablen erstellen:
        • gamer_tag: Ein String mit einem Wunschnamen (z. B. "PixelHeld").
        • score: Eine ganze Zahl (Integer) für den Punktestand (z. B. 9500).
        • play_time: Eine Gleitkommazahl (Float) für die Spielzeit in Stunden (z. B. 42.5).
• Ausgabe & Typen:
        • Gib alle drei Variablen mit print() aus.
        • Nutze type(), um die Datentypen aller drei Variablen in der Konsole anzuzeigen.
• Konvertierung & Satzbau:
        • Konvertiere score in einen String und speichere ihn in score_str.
        • Gib folgenden Satz aus, indem du die Variablen kombinierst:
                • "Der Spieler [gamer_tag] hat aktuell [score_str] Punkte erreicht."
"""

# Variablen erstellen
gamertag1 = "PixelHeld"
score1 = 1337
playtime1 = 9000.67

# Ausgabe & Typen
print(gamertag1, score1, playtime1, type(gamertag1), type(score1), type(playtime1))

# Konvertierung & Satzbau
scorestr1 = str(score1)
print(
    "Der Spieler",
    gamertag1,
    "hat aktuell",
    scorestr1,
    "Punkte erreicht",
    "und eine Spielzeit von",
    playtime1,
    "Stunden.",
)
