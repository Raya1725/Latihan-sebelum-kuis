class OrangAnggrek:

    def __init__(self):
        self.nama = ""
        self.no_ktp = ""
        self.alamat = ""
        self.no_ijin = ""
        self.tahun_awal = ""
        self.list_anggrek = []
    def setNama(self, nama):
        self.nama = nama
    def getNama(self):
        return self.nama
    def setNoktp(self, no_ktp):
        self.no_ktp = no_ktp
    def getNoktp(self):
        return self.no_ktp
    def setAlamat(self, alamat):
        self.alamat =  alamat
    def getAlamat(self):
        return self.alamat
    def setNoijin(self, no_ijin):
        self.no_ijin =  no_ijin
    def getNoijin(self):
        return self.no_ijin
    def setTahunAwal(self, tahun_awal):
        self.tahun_awal =  tahun_awal
    def getTahunAwal(self):
        return self.tahun_awal
    def setListAnggrek(self, list_anggrek):
        self.list_anggrek.append(list_anggrek)
    def getListAnggrek(self):
        return self.list_anggrek
    