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
		
a=Adres("", "", "Mickiewicza", "")
a.podaj_adres()
print(a)
#Miejscowosc: 
#
#Miejscowosc wymaga podania wartości.
#Miejscowosc: 
#Szczecin
#Kod Pocztowy: 
#
#Kod Pocztowy wymaga podania wartości.
#Kod Pocztowy: 
#71-101
#Ulica (Mickiewicza): 
#
#Nr Domu: 
#64
#Nr Mieszkania:
# 
#Kraj (Polska): 
#
#Mickiewicza 64, 71-101 Szczecin, Polska