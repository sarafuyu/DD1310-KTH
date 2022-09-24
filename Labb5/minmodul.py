class Person:
    def __init__(self, n, v):
        self.namn=n
        self.vikt=v

    def bytNamn(self, nyttNamn):
        self.namn=nyttNamn
        
    def __lt__(self,den_andra_personen):
        if self.vikt < den_andra_personen.vikt:
            return True
        return False

    def __le__(self,den_andra_personen):
        if self.vikt <= den_andra_personen.vikt:
            return True
        return False

    def __eq__(self, den_andra_personen):
        if self.vikt == den_andra_personen.vikt and self.namn==den_andra_personen.namn:
            return True
        return False

    def __gt__(self,other):
        print("TEST")
        if self.vikt > other.vikt:
            return True
        return False

    def __ge__(self,other):
        if self.vikt >= other.vikt:
            return True
        return False

    def __str__(self):

        return "Personen heter "+ self.namn+ " och vager "+ str(self.vikt)+ " kg."
