class Adres:
    def __init__(self, miejscowosc, kod_pocztowy, ulica, nr_domu, nr_mieszkania="", kraj = "Polska"):
        self.kraj = kraj
        self.miejscowosc = miejscowosc
        self.kod_pocztowy = kod_pocztowy
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.nr_mieszkania = nr_mieszkania

a=Adres("Szczecin", "71-101", "Mickiewicza", "64")
print(a.ulica)
