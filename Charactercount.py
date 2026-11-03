def counterbuchstaben(wort):
    kleines_wort = wort.lower()
    result = bool()
    anzahl = []
    for buchstabe in kleines_wort:
        zahl = kleines_wort.count(buchstabe)
        anzahl.append(zahl)

    anzahl = set(anzahl)
    if len(set(anzahl)) == 1:
        result = True
        return result
    else:
        result = False
        return result


print(counterbuchstaben("Mercedes"))
