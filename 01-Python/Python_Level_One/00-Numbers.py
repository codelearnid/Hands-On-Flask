#####################################
#### Angka dan lebih di Python! ####
#####################################

# Dalam kuliah ini, kita akan belajar tentang angka di Python dan cara menggunakannya.
#
# Kita akan belajar tentang topik berikut:
#
#     1.) Jenis Angka di Python
#     2.) Aritmatika Dasar
#     3.) Perbedaan antara Python 2 vs 3 dalam pembagian
#     4.) Penugasan Objek di Python

# Jenis angka
#
# Python memiliki berbagai "jenis" angka (literal numerik). Kita akan fokus terutama pada
# bilangan bulat dan bilangan pecahan.
#
# Bilangan bulat hanyalah angka bulat, positif atau negatif. Misalnya: 2 dan -2 adalah
# contoh bilangan bulat.
#
# Bilangan pecahan dalam Python menonjol karena memiliki titik desimal
# di dalamnya, atau menggunakan eksponensial (e) untuk mendefinisikan angka. Misalnya 2.0 dan -2.1
# adalah contoh bilangan pecahan. 4E2 (4 kali 10 pangkat 2) juga merupakan contoh bilangan pecahan di Python.
#
# Sepanjang kursus ini, kita akan terutama bekerja dengan
# bilangan bulat atau jenis bilangan pecahan sederhana.


# Sekarang mari kita mulai dengan beberapa aritmatika dasar.

# Aritmatika Dasar
# Penambahan
2+1

# Pengurangan
2-1

# Perkalian
2*2


# Pembagian
3/2

# Pangkat
2**3

# Juga bisa melakukan akar dengan cara ini
4**0.5

# Urutan Operasi yang diikuti di Python
2 + 10 * 10 + 3

# Bisa menggunakan tanda kurung untuk menentukan urutan
(2+10) * (10+3)


## Penugasan Variabel
#
# Sekarang setelah kita melihat cara menggunakan angka di Python sebagai kalkulator, mari kita lihat bagaimana
# kita bisa menetapkan nama dan membuat variabel.
#
# Kita menggunakan tanda sama dengan tunggal untuk menetapkan label ke variabel.
# Anda juga tidak perlu menentukan kata kunci var.
# Mari kita lihat beberapa contoh bagaimana kita bisa melakukannya.

# Mari buat objek bernama "a" dan tetapkan angka 5 kepadanya
a = 5

# Sekarang jika saya memanggil a dalam skrip Python saya, Python akan memperlakukannya sebagai angka 5.

# Menambahkan objek
a+a

# Apa yang terjadi pada penugasan ulang? Apakah Python membiarkan kita menulisnya lagi?

# Penugasan Ulang
a = 10

# Periksa
a


# Ya! Python memungkinkan Anda menulis ulang nama variabel yang ditugaskan. Kita juga bisa menggunakan
# variabel itu sendiri saat melakukan penugasan ulang. Berikut adalah contoh dari apa yang saya maksud:

# Periksa
a

# Gunakan A untuk mendefinisikan ulang A
a = a + a

# Periksa
a


# Nama yang Anda gunakan saat membuat label ini perlu mengikuti beberapa aturan:
#
#     1. Nama tidak boleh dimulai dengan angka.
#     2. Tidak boleh ada spasi dalam nama, gunakan _ sebagai gantinya.
#     3. Tidak boleh menggunakan salah satu simbol ini :'",<>/?|\()!@#$%^&*~-+
#     3. Dikatakan praktik terbaik (PEP8) bahwa nama-nama itu huruf kecil.
#
# Menggunakan nama variabel bisa menjadi cara yang sangat berguna untuk melacak berbagai
# variabel di Python. Misalnya:

# Gunakan nama objek untuk lebih memahami apa yang terjadi dalam kode Anda!
puppies = 6

weight = 2

total_weight = puppies*weight

# Tampilkan total_weight saya
total_weight


# Jadi apa yang telah kita pelajari? Kita belajar beberapa dasar angka di Python.
# Kita juga belajar cara melakukan aritmatika dan menggunakan Python sebagai kalkulator dasar.
# Kita kemudian mengakhiri dengan belajar tentang Penugasan Variabel di Python.
#
# Selanjutnya kita akan belajar tentang String!
