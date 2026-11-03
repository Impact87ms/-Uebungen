# * Example 1:
# vorgegebene Zahlenliste
nummern = [2, 7, 11, 15]
# Zielzahl ist 9


def suche_result(nums, result):
    werte_index = {}
    for index, zahl in enumerate(nums):
        zahl_2 = result - zahl
        if zahl_2 in werte_index:
            return f"{werte_index[zahl_2]} und {index}"
        werte_index[zahl] = index


print(suche_result(nummern, 9))

# * Example 2
print("---------")
nummern2 = [3, 2, 4]
# Ziel ist 6

print(suche_result(nummern2, 6))

# * Example 3
print("---------")
nummern3 = [3, 3]
# Ziel ist 6

print(suche_result(nummern3, 6))
