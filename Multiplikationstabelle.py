"""def multiplita(number):
    result = 0

    for reihe in range(1, 11):
        result = number * reihe
        print(f"{reihe} * {number} = {result}")
    else:
        reihe = 11
        print("Ende")


multiplita(3)"""


def multiplita(number):
    result = 0
    tabelle = ""
    for reihe in range(1, 11):
        result = number * reihe
        tabelle += f"{reihe} * {number} = {result}\n"
    return tabelle


print(multiplita(5))
