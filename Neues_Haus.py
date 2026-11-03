class Haus:
    def __init__(self, art, quadratmeter, garten, balkon, stockwerk, baujahr):
        self.art = art
        self.quadratmeter = quadratmeter
        self.garten = garten
        self.balkon = balkon
        self.stockwerk = stockwerk
        self.baujahr = baujahr

    """def pref(
        self,
    ):
        wunschart = "Haus"
        wunschgarten = True
        wunschquadratmeter = 150
        wunschbaujahr = 2000
        wunschbalkon = True
        wunschstockwerk = 2"""

    def prio(
        self,
        wunschart,
        wunschgarten,
        wunschbaujahr,
        wunschstockwerk,
        wunschbalkon,
        wunschquadratmeter,
    ):
        prio1 = wunschart
        prio2 = wunschgarten
        prio3 = wunschbaujahr
        prio4 = wunschstockwerk
        prio5 = wunschbalkon
        prio6 = wunschquadratmeter
        punkte = 0
        if prio1 == self.art:
            punkte += 6

        if prio2 is self.garten:
            punkte += 5

        if prio3 >= self.baujahr:
            punkte += 4

        if prio4 < 3:
            punkte += 3

        if prio5 is self.balkon:
            punkte += 2

        if prio6 >= self.quadratmeter:
            punkte += 1

        else:
            punkte += 0
        return punkte


place1 = Haus("Wohnung", 90, False, True, 3, 2000)
place2 = Haus("Haus", 300, True, True, 3, 2005)
place3 = Haus("Haus", 150, True, False, 2, 2008)
