from abc import ABC, abstractmethod

class AbstractBangunRuang(ABC):
    def __init__(self, warna, panjang, lebar, tinggi):
        self.warna = warna
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    @abstractmethod
    def hitung_volume(self):
        pass

    @abstractmethod
    def hitung_luas_permukaan(self):
        pass

    @abstractmethod
    def hitung_keliling(self):
        pass

class Kubus(AbstractBangunRuang):
    def __init__(self, warna, panjang, lebar, tinggi, massa, bahan):
        super().__init__(warna, panjang, lebar, tinggi)
        self.massa = massa
        self.bahan = bahan

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_luas_permukaan(self):
        return 6 * (self.panjang * self.lebar)

    def hitung_keliling(self):
        return 12 * self.panjang


class Tabung(AbstractBangunRuang):
    def __init__(self, warna, panjang, lebar, tinggi, jari_jari, phi):
        super().__init__(warna, panjang, lebar, tinggi)
        self.jari_jari = jari_jari
        self.phi = phi

    def hitung_volume(self):
        return self.phi * (self.jari_jari ** 2) * self.tinggi

    def hitung_luas_permukaan(self):
        return 2 * self.phi * self.jari_jari * (self.jari_jari + self.tinggi)

    def hitung_keliling(self):
        return 2 * self.phi * self.jari_jari

class Balok(AbstractBangunRuang):
    def __init__(self, warna, panjang, lebar, tinggi, orientasi, fungsi):
        super().__init__(warna, panjang, lebar, tinggi)
        self.orientasi = orientasi
        self.fungsi = fungsi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_luas_permukaan(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def hitung_keliling(self):
        return 4 * (self.panjang + self.lebar + self.tinggi)

if __name__ == "__main__":
    list_bangun_ruang = [
        Kubus("Merah", 5, 5, 5, 10, "Kayu"),
        Tabung("Biru", 0, 0, 10, 7, 22/7),
        Balok("Hijau", 10, 5, 4, "Horizontal", "Kemasan")
    ]

    for bangun in list_bangun_ruang:
        print(f"Informasi Bangun Ruang: {bangun.__class__.__name__}")
        print(f"Warna\t\t: {bangun.warna}")

        if isinstance(bangun, Kubus):
            print(f"Massa\t\t: {bangun.massa} kg")
            print(f"Bahan\t\t: {bangun.bahan}")

        elif isinstance(bangun, Balok):
            print(f"Orientasi\t: {bangun.orientasi}")
            print(f"Fungsi\t\t: {bangun.fungsi}")

        elif isinstance(bangun, Tabung):
            print(f"Jari-jari\t: {bangun.jari_jari} cm")

        print(f"Volume\t\t: {bangun.hitung_volume():.2f}")
        print(f"Luas Permukaan\t: {bangun.hitung_luas_permukaan():.2f}")
        print(f"Keliling\t: {bangun.hitung_keliling():.2f}")
        print("-" * 30, "\n")