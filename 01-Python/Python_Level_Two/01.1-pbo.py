class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def deskripsi(self):
        return f"'{self.judul}' oleh {self.penulis}, diterbitkan pada {self.tahun_terbit}"

# Membuat objek buku
buku1 = Buku("Belajar Python", "John Doe", 2020)
buku2 = Buku("Pemrograman Lanjut", "Jane Smith", 2018)

# Mengakses deskripsi buku
print(buku1.deskripsi())  # Output: 'Belajar Python' oleh John Doe, diterbitkan pada 2020
print(buku2.deskripsi())  # Output: 'Pemrograman Lanjut' oleh Jane Smith, diterbitkan pada 2018
print(buku1.judul)