def geburtsjahr(gebjahr, jahr):
    text = ""
    if gebjahr == jahr:
        text += f"You were born this very year!"
        return text
    elif gebjahr > jahr:
        result = gebjahr - jahr
        if result == 1:
            text += f"You will be born in {result} year."
            return text
        else:
            text += f"You will be born in {result} years."
            return text
    else:
        gebjahr < jahr
        result = jahr - gebjahr
        if result == 1:
            text += f"You are {result} year old."
            return text
        else:
            text += f"You are {result} years old."
            return text


print(geburtsjahr(1995, 2026))
