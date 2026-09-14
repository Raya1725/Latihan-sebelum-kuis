from OrangAnggrek import OrangAnggrek

class PedagangAnggrek(OrangAnggrek):

    def __init__ (self):
        self.jam_buka = ""
    def setJamBuka(self, jam_buka):
        self.jam_buka = jam_buka
    def getJamBuka(self):
        return self.jam_buka