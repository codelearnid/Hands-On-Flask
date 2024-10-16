##################################
## Tuple, Set, dan Boolean ####
##################################
#
# Dalam Python, tuple sangat mirip dengan list, namun, tidak seperti list, mereka
# tidak dapat diubah. Anda akan menggunakan tuple untuk menyajikan
# hal-hal yang tidak seharusnya diubah, seperti hari dalam seminggu, atau tanggal pada kalender.
#
# Dalam bagian ini, kita akan mendapatkan gambaran singkat tentang hal-hal berikut:
#
#     1.) Membangun Tuple
#     2.) Metode Tuple Dasar
#     3.) Ketidakubahannya
#     4.) Kapan Menggunakan Tuple.
#
# Anda akan memiliki intuisi tentang bagaimana menggunakan tuple berdasarkan apa yang telah Anda pelajari
# tentang list. Kita dapat mengobati mereka sangat mirip dengan perbedaan utama bahwa tuple tidak dapat diubah.
#
############################
#### Membangun Tuple ###
############################
#
# Pembangunan tuple menggunakan () dengan elemen yang dipisahkan oleh koma. Contoh:

# Dapat membuat tuple dengan tipe campuran
t = (1,2,3)

# Cek panjang seperti pada list
len(t)

# Dapat juga mencampur tipe objek
t = ('one',2)

# Tampilkan
t

# Gunakan indeks seperti yang kita lakukan pada list
t[0]

# Slicing seperti pada list
t[-1]

############################
### Metode Tuple Dasar ####
############################

# Tuple memiliki metode bawaan, tetapi tidak sebanyak yang dimiliki list.
# Mari kita lihat dua di antaranya:

# Gunakan .index untuk memasukkan nilai dan mengembalikan indeks
t.index('one')

# Gunakan .count untuk menghitung jumlah kali nilai muncul
t.count('one')

####################
### Ketidakubahannya ###
####################

# Tidak dapat ditekankan cukup bahwa tuple tidak dapat diubah.
# Untuk menekankan hal ini:

t[0]= 'ubah'

# Karena ketidakubahannya ini, tuple tidak dapat tumbuh.
# Setelah tuple dibuat, kita tidak dapat menambahkannya.

t.append('tidak')

############################
### Kapan Menggunakan Tuple #####
############################

# Anda mungkin bertanya, "Mengapa repot menggunakan tuple ketika mereka memiliki metode yang lebih sedikit?" Untuk jujur, tuple tidak digunakan sebanyak list dalam pemrograman,
# tapi digunakan ketika ketidakubahannya diperlukan. Jika dalam program Anda sedang melewati objek dan perlu memastikan bahwa objek tersebut tidak berubah, maka tuple menjadi solusinya. Ini menyediakan sumber integritas data yang nyaman.
#
# Anda sekarang harus dapat membuat dan menggunakan tuple dalam pemrograman Anda serta memiliki pemahaman tentang ketidakubahannya.
#

########################################################
########################################################
############## SETS DAN BOOLEANS #######################
########################################################
########################################################
#
# Ada dua tipe objek lainnya dalam Python yang kita harus singkatkan. Set dan Boolean.
#
############
### Sets ###
############

# Set adalah koleksi elemen *unik* yang tidak berurutan. Kita dapat membuat mereka dengan menggunakan fungsi set(). Mari kita lihat bagaimana cara membuat set untuk melihat bagaimana mereka bekerja!

x = set()

# Kita menambahkan ke set dengan metode add()
x.add(1)

#Tampilkan
x


# Perhatikan bahwa set memiliki entri yang unik saja. Jadi apa yang terjadi ketika kita mencoba menambahkan sesuatu yang sudah ada dalam set?

# Tambahkan elemen yang berbeda
x.add(2)

#Tampilkan
x

# Coba tambah elemen yang sama
x.add(1)

#Tampilkan
x


# Perhatikan bahwa itu tidak akan menempatkan 1 lainnya di sana. Itu karena set hanya peduli dengan elemen yang unik! Kita dapat mengubah list dengan elemen yang berulang menjadi set untuk mendapatkan elemen yang unik. Contoh:

# Buat list dengan ulangan
mylist = [1,1,2,2,3,4,5,6,1,1]

# Ubah menjadi set untuk mendapatkan elemen yang unik
set(mylist)

##########################
######## Booleans ########
##########################
# Python datang dengan Boolean (dengan tampilan True dan False yang telah ditentukan) yang pada dasarnya hanya bilangan 1 dan 0. Itu juga memiliki objek placeholder yang disebut None. Mari kita berjalan melalui beberapa contoh Boolean yang cepat (kita akan membahas lebih lanjut tentang mereka nanti dalam kursus ini).

# Tetapkan objek sebagai Boolean
a = True

#Tampilkan
a


# Kita juga dapat menggunakan operator perbandingan untuk membuat Boolean. Kita akan membahas semua operator perbandingan nanti dalam kursus ini.

# Output adalah Boolean
1 > 2


# Kita dapat menggunakan None sebagai placeholder untuk objek yang kita tidak ingin mengubahnya lagi:

# Placeholder None
b = None


# Itu saja! Anda sekarang harus memiliki pemahaman dasar tentang objek dan tipe data struktur dalam Python. Selanjutnya, silakan lakukan Latihan Ulasan!
