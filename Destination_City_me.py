"""Funktion zur Suche der letzten Stadt"""


def finalcity(cities):
    # Startstädte sammeln = jeweils 1. Wert vom jeweiligen Index
    cityA = []
    for index in cities:
        cityA.append(index[0])
    # Endstädte sammeln = jeweils 2. Wert vom jeweiligen Index
    cityE = []
    for index in cities:
        cityE.append(index[1])
    # vergleichen ob die Endstädte auch in den Startstädten vorkommen
    for c in range(len(cityE)):
        if cityE[c] not in cityA:  # Wert nicht in Liste
            return cityE[c]


# * Example 1
print("----")  # Hilfslinien für Lesbarkeit im Terminal
paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# Gesucht wird Sao Paulo
print(finalcity(paths1))

# * Example 2
print("----")  # Hilfslinien für Lesbarkeit im Terminal
paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
# Gesucht wird A
print(finalcity(paths2))

# * Example 3
print("----")  # Hilfslinien für Lesbarkeit im Terminal
paths3 = [["A", "Z"]]
# Gesucht wird Z
print(finalcity(paths3))
