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
                print(x_sformatowane,"wymaga podania wartości.")

class Wlasciciel(Adres):
    def __init__(self, imie, nazwisko, nr_dowodu, miejscowosc, kod_pocztowy, ulica, nr_domu,
                 nr_mieszkania="", kraj = "Polska"):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_dowodu = nr_dowodu
        super().__init__(miejscowosc, kod_pocztowy, ulica, nr_domu, nr_mieszkania, kraj)

    def __str__(self):        
        wlas = self.imie  + " " + self.nazwisko + " (nr dok. tożs. " + self.nr_dowodu + ") zam. "
        wlas += super().__str__()
        return wlas

    def podaj_dane_wlas(self):
        for x in ["imie", "nazwisko", "nr_dowodu"]:
            dotychczasowe = ""
            if self.__dict__.get(x, ""): dotychczasowe = " (" + self.__dict__[x] + ")"
            x_sformatowane = x.title().replace("_", " ")
            while True:
                v = input(x_sformatowane + dotychczasowe + ": ")
                if v:
                    self.__dict__[x] = v
                    break
                if dotychczasowe: break
                print(x_sformatowane,"wymaga podania wartości.")
        self.podaj_adres()

    
class Konto():
    zalozone_konta = []
    def __init__(self):
        self.__class__.zalozone_konta.append(self)
        self.nr_konta = f"{len(self.__class__.zalozone_konta):03}"
        self.data_zablokowania = None
        self.saldo = 0.0
        self.wlasciciel = Wlasciciel("", "", "", "Szczecin", "", "", "")
        print("Wprowadź dane właściciela nowego konta")
        self.wlasciciel.podaj_dane_wlas()
    def __str__(self):        
        opis = "Konto nr: " + self.nr_konta
        if self.data_zablokowania:
            opis += "\tZablokowane dn.: " + str(self.data_zablokowania)
        else:
            opis += "\tAktywne"
        opis += f"\t\tSaldo: {self.saldo:.2f} zł\n"
        opis += "Właściciel: " + self.wlasciciel.__str__()
        return opis
    @classmethod
    def dostep_do_konta(cls, powod):
        nr_konta = input("Podaj nr rachunku " + powod)[:3]
        try:
            nr_konta = int(nr_konta)
            if nr_konta < 1: raise ValueError
            if nr_konta > len(cls.zalozone_konta): raise ValueError
        except ValueError:
            print("Błędny numer konta!")
            return
        k = cls.zalozone_konta[nr_konta - 1]
        if k.data_zablokowania:
            print("Konto zablokowane dn.: " + str(k.data_zablokowania))
            return
        return k
    @classmethod
    def wplata(cls):       
        k = cls.dostep_do_konta("do wpłaty: ")
        if not k: return
        kwota = input("Podaj kwotę wpłaty:")
        try:
            kwota = float(kwota)
            if kwota < 0.0: raise ValueError
        except ValueError:
            print("Niewłaściwa kwota wpłaty!")
            return
        k.saldo += kwota
        print(f"Saldo po wpłacie: {k.saldo:.2f} zł")
    @classmethod
    def wyplata(cls):       
        k = cls.dostep_do_konta("do wypłaty: ")
        if not k: return
        kwota = input("Podaj kwotę do wypłaty:")
        try:
            kwota = float(kwota)
            if kwota < 0.0: raise ValueError
        except ValueError:
            print("Niewłaściwa kwota wypłaty!")
            return
        if kwota > k.saldo:
            print("Kwota do wypłaty przewyższa saldo konta!")
            return
        k.saldo -= kwota
        print(f"Saldo po wypłacie: {k.saldo:.2f} zł")
    @classmethod
    def przelew(cls):       
        k = cls.dostep_do_konta("- źródła środków: ")
        if not k: return
        k2 = cls.dostep_do_konta("docelowego przelewu: ")
        if not k2: return
        kwota = input("Podaj kwotę do przelewu:")
        try:
            kwota = float(kwota)
            if kwota < 0.0: raise ValueError
        except ValueError:
            print("Niewłaściwa kwota przelewu.")
            return
        if kwota > k.saldo:
            print("Kwota do wypłaty przewyższa saldo konta - źródła środków!")
            return
        k.saldo -= kwota
        k2.saldo += kwota
        print(f"Saldo konta {k.nr_konta} po wypłacie: {k.saldo:.2f} zł")
        print(f"Saldo konta {k2.nr_konta} po wypłacie: {k2.saldo:.2f} zł")
    @classmethod
    def odsetki(cls):       
        stopa = input("Podaj stopę procentową do naliczenia odsetek (w %):")
        try:
            stopa = float(stopa)
        except ValueError:
            print("Niewłaściwa stopa procentowa.")
            return
        stopa += 100.0
        stopa /= 100.0
        for k in cls.zalozone_konta:
            if not k.data_zablokowania:
                k.saldo *= stopa        
                print(f"Saldo konta {k.nr_konta} po naliczeniu odsetek: {k.saldo:.2f} zł")