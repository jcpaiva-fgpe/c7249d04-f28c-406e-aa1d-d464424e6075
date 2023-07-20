class Adres:
    def __init__(self, miejscowosc, kod_pocztowy, ulica, nr_domu, nr_mieszkania="", kraj = "Polska"):
        self.kraj = kraj
        self.miejscowosc = miejscowosc
        self.kod_pocztowy = kod_pocztowy
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.nr_mieszkania = nr_mieszkania                

    def __str__(self):        
        adres = self.ulica + " " + self.nr_domu
        if self.nr_mieszkania: adres += "/" + self.nr_mieszkania
        adres += ", " + self.kod_pocztowy + " " + self.miejscowosc + ", " + self.kraj
        return adres

    def podaj_adres(self):
        for x in ["miejscowosc", "kod_pocztowy", "ulica", "nr_domu", "nr_mieszkania", "kraj"]:
            dotychczasowe = ""
            if self.__dict__.get(x, ""): dotychczasowe = " (" + self.__dict__[x] + ")"
            x_sformatowane = x.title().replace("_", " ")
            while True:
                v = input(x_sformatowane + dotychczasowe + ": ")
                if v:
                    self.__dict__[x] = v
                    break
                if dotychczasowe or x == "nr_mieszkania": break
                print(x_sformatowane, "wymaga podania wartości.")
				
w=Wlasciciel("Jan", "Kowalski", "ABC 123456", "Szczecin", "71-101", "Mickiewicza", "64")
print(w.nr_dowodu)
#ABC 123456
