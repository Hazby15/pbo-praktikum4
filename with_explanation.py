from abc import ABC, abstractmethod # untuk mengimpor modul bawaan Python yang digunakan dalam pembuatan Abstract Class
# ABC untuk mendefinisikan class abstract, abstractmethod merupakan decorator
# di dalam class abstract dan wajib di override

class AbstractBangunRuang(ABC): # abstract class parent (utama) yang tidak bisa diinstansiasi secara langsung
    def __init__(self, warna, panjang, lebar, tinggi): # constructor untuk menginisialisasi atribut warna, panjang, lebar, dan tinggi
        self.warna = warna
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    @abstractmethod # decorator untuk menandai method sebagai abstract method, yang harus diimplementasikan oleh subclass
    def hitung_volume(self):
        pass # override method, jika subclass tidak mengimplementasikan method ini maka akan memunculkan "TypeError: Can't instantiate..."

    @abstractmethod
    def hitung_luas_permukaan(self):
        pass # override method

    @abstractmethod
    def hitung_keliling(self):
        pass # override method

class Kubus(AbstractBangunRuang): # subclass dari AbstractBangunRuang yang mewarisi atribut dan method dari class parent
    def __init__(self, warna, panjang, lebar, tinggi, massa, bahan): # menggunakan constructor untuk menginisialisasi atribut tambahan massa dan bahan
        # massa dan bahan merupakan atribut tambahan yang hanya dimiliki oleh kubus
        super().__init__(warna, panjang, lebar, tinggi) # memanggil constructor dari class parent (AbstractBangunRuang) untuk menginisialisasi atribut warna, panjang, lebar, dan tinggi
        self.massa = massa
        self.bahan = bahan

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_luas_permukaan(self):
        return 6 * (self.panjang * self.lebar)
    # subclass Kubus memiliki method hitung_volume, hitung_luas_permukaan, dan hitung_keliling yang 
    # mengimplementasikan abstract method dari class parent AbstractBangunRuang

    def hitung_keliling(self): # method tambahan
        return 12 * self.panjang


class Tabung(AbstractBangunRuang): # subclass dari AbstractBangunRuang yang mewarisi atribut dan method dari class parent
    def __init__(self, warna, panjang, lebar, tinggi, jari_jari, phi): # menggunakan constructor untuk menginisialisasi atribut tambahan jari_jari dan phi
        # jari_jari dan phi merupakan atribut tambahan yang hanya dimiliki oleh tabung
        super().__init__(warna, panjang, lebar, tinggi) # memanggil constructor dari class parent (AbstractBangunRuang) untuk menginisialisasi atribut warna, panjang, lebar, dan tinggi
        self.jari_jari = jari_jari
        self.phi = phi

    def hitung_volume(self):
        return self.phi * (self.jari_jari ** 2) * self.tinggi

    def hitung_luas_permukaan(self):
        return 2 * self.phi * self.jari_jari * (self.jari_jari + self.tinggi)
    # subclass Tabung memiliki method hitung_volume, hitung_luas_permukaan, dan hitung_keliling yang 
    # mengimplementasikan abstract method dari class parent AbstractBangunRuang

    def hitung_keliling(self): # method tambahan
        return 2 * self.phi * self.jari_jari


class Balok(AbstractBangunRuang): # subclass dari AbstractBangunRuang yang mewarisi atribut dan method dari class parent
    def __init__(self, warna, panjang, lebar, tinggi, orientasi, fungsi): # menggunakan constructor untuk menginisialisasi atribut tambahan orientasi dan fungsi
        # orientasi dan fungsi merupakan atribut tambahan yang hanya dimiliki oleh balok
        super().__init__(warna, panjang, lebar, tinggi) # memanggil constructor dari class parent (AbstractBangunRuang) untuk menginisialisasi atribut warna, panjang, lebar, dan tinggi
        self.orientasi = orientasi
        self.fungsi = fungsi

    def hitung_volume(self):
        return self.panjang * self.lebar * self.tinggi

    def hitung_luas_permukaan(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)
    # subclass Balok memiliki method hitung_volume, hitung_luas_permukaan, dan hitung_keliling yang 
    # mengimplementasikan abstract method dari class parent AbstractBangunRuang

    def hitung_keliling(self): # method tambahan
        return 4 * (self.panjang + self.lebar + self.tinggi)


if __name__ == "__main__": # fungsinya adalah untuk mengeksekusi kode hanya jika file ini dijalankan secara langsung, bukan diimpor sebagai modul
    list_bangun_ruang = [
        Kubus("Merah", 5, 5, 5, 10, "Kayu"),
        Tabung("Biru", 0, 0, 10, 7, 22/7),
        Balok("Hijau", 10, 5, 4, "Horizontal", "Kemasan")
    ] # membuat list yang berisi objek dari class Kubus, Tabung, dan Balok dengan atribut yang berbeda-beda
    # dengan menggunakan list, kita bisa menyimpan objek dari class yang berbeda-beda dalam satu variabel dan mengaksesnya secara bersamaan

    for bangun in list_bangun_ruang: # perulangan untuk menampilkan informasi dari setiap objek dalam list_bangun_ruang
        # melalui perulangan ini, kita bisa memanggil method yang sama pada objek yang berbeda-beda tanpa harus mengetahui tipe objeknya secara spesifik, konsep ini disebut polymorphism
        print(f"Informasi Bangun Ruang: {bangun.__class__.__name__}") # menampilkan nama class dari objek yang sedang diproses dalam perulangan
        print(f"Warna\t\t: {bangun.warna}") # menampilkan atribut warna dari objek yang sedang diproses dalam perulangan
        # \t digunakan untuk membuat tabulasi atau tab atau indentsi agar tampilan lebih dan sejajar

        if isinstance(bangun, Kubus): # isinstance() digunakan untuk mengenali tipe sublcass dari objek
            # yang sedang diproses dalam perulangan, sehingga kita bisa menampilkan informasi tambahan yang spesifik untuk setiap subclass
            print(f"Massa\t\t: {bangun.massa} kg") # menampilkan atribut tambahan massa yang hanya dimiliki oleh objek dari class Kubus
            print(f"Bahan\t\t: {bangun.bahan}") # menampilkan atribut tambahan bahan yang hanya dimiliki oleh objek dari class Kubus

        elif isinstance(bangun, Balok): # isinstance() digunakan untuk mengenali tipe sublcass dari objek
            print(f"Orientasi\t: {bangun.orientasi}") # menampilkan atribut tambahan orientasi yang hanya dimiliki oleh objek dari class Balok
            print(f"Fungsi\t\t: {bangun.fungsi}") # menampilkan atribut tambahan fungsi yang hanya dimiliki oleh objek dari class Balok

        elif isinstance(bangun, Tabung): # isinstance() digunakan untuk mengenali tipe sublcass dari objek
            print(f"Jari-jari\t: {bangun.jari_jari} cm") # menampilkan atribut tambahan jari_jari yang hanya dimiliki oleh objek dari class Tabung

        print(f"Volume\t\t: {bangun.hitung_volume():.2f}") # menampilkan hasil perhitungan volume dari objek yang sedang diproses dalam perulangan dengan format 2 angka di belakang koma
        print(f"Luas Permukaan\t: {bangun.hitung_luas_permukaan():.2f}") # menampilkan hasil perhitungan luas permukaan dari objek yang sedang diproses dalam perulangan dengan format 2 angka di belakang koma
        print(f"Keliling\t: {bangun.hitung_keliling():.2f}") # menampilkan hasil perhitungan keliling dari objek yang sedang diproses dalam perulangan dengan format 2 angka di belakang koma
        # .2f digunakan untuk membatasi jumlah angka di belakang koma menjadi 2 digit
        print("-" * 30, "\n")