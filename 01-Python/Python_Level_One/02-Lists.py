# # List
#
# Sebelumnya, ketika membahas string, kita memperkenalkan konsep "urutan" dalam
# Python. List dapat dianggap sebagai versi yang paling umum dari "urutan" dalam
# Python. Berbeda dengan string, mereka dapat diubah, artinya elemen di dalam list dapat diubah!
#
# Dalam bagian ini kita akan belajar tentang:
#
#     1.) Membuat list
#     2.) Mengindeks dan Mengiris List
#     3.) Metode List Dasar
#     4.) Menggabungkan List
#     5.) Pengenalan ke Komprehensi List
#
# List dibuat dengan tanda kurung [] dan koma yang memisahkan setiap elemen dalam list.
#
# Mari kita lihat bagaimana kita dapat membuat list!

# Tetapkan list ke variabel bernama my_list
my_list = [1,2,3]


# Kita baru saja membuat list bilangan bulat, tapi list sebenarnya
# dapat menampung tipe objek yang berbeda. Contoh:

my_list = ['Sebuah string',23,100.232,'o']

# Sama seperti string, fungsi len() akan memberitahu Anda berapa banyak item dalam urutan list.
len(my_list)

##############################
#### Mengindeks dan Mengiris List ####
##############################

# Mengindeks dan mengiris bekerja sama seperti dalam string. Mari kita buat list baru untuk
# mengingatkan diri kita bagaimana cara ini bekerja:
my_list = ['satu','dua','tiga',4,5]

# Ambil elemen pada indeks 0
my_list[0]

# Ambil indeks 1 dan segalanya setelah itu
my_list[1:]

# Ambil segalanya HINGGA indeks 3
my_list[:3]

# Kita juga dapat menggunakan + untuk menggabungkan list, seperti yang kita lakukan untuk string.

my_list + ['item baru']

# Catatan: Ini tidak benar-benar mengubah list asli!

my_list

# Anda harus mengubah kembali list untuk membuat perubahan permanen.


# Ubah kembali
my_list = my_list + ['tambah item baru secara permanen']

my_list

# Kita juga dapat menggunakan * untuk metode duplikasi serupa dengan string:

# Buat list menjadi dua kali lipat
my_list * 2

# Lagi, duplikasi tidak permanen
my_list

# We can also use the * for a duplication method similar to strings:

# Make the list double
my_list * 2

# Again doubling not permanent
my_list

#############################
#### Metode List Dasar #####
#############################
#
# Jika Anda familiar dengan bahasa pemrograman lain, Anda mungkin mulai menggambar
# paralel antara array dalam bahasa lain dan list dalam Python. List dalam
# Python, bagaimanapun, cenderung lebih fleksibel daripada array dalam bahasa lain karena dua alasan yang baik: mereka tidak memiliki ukuran yang tetap (artinya kita tidak harus menentukan
# seberapa besar list akan), dan mereka tidak memiliki konstrain tipe yang tetap (seperti yang kita lihat di atas).
#
# Mari kita lanjutkan dan eksplorasi beberapa metode khusus untuk list:

# Buat list baru
mylist = [1,2,3]

# Gunakan metode .append() untuk secara permanen menambahkan item ke akhir list:

# Tambahkan
mylist.append('tambah saya!')

# Tampilkan
print(mylist)

# Gunakan "pop" untuk "menghapus" item dari list. Secara default pop menghapus item terakhir, tetapi Anda juga dapat menentukan indeks mana yang akan dihapus. Mari kita lihat contoh:

# Hapus item yang berindeks 0
mylist.pop(0)

# Tampilkan
mylist

# Tetapkan item yang dihapus, ingat bahwa indeks yang dihapus secara default adalah -1
popped_item = mylist.pop()

print(popped_item)

# Tampilkan list yang tersisa
print(mylist)

# Juga harus diperhatikan bahwa pengindeksan list akan mengembalikan kesalahan jika tidak ada elemen pada indeks tersebut. Contoh:
mylist[100]

#######################
#### Menggabungkan List ####
#######################
# Fitur hebat dari struktur data Python adalah bahwa mereka mendukung penggabungan.
# Ini berarti kita dapat memiliki struktur data dalam struktur data lainnya.
# Contoh: List di dalam list.
#
# Mari kita lihat bagaimana ini bekerja!

# Buat tiga list
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Buat list dari list untuk membentuk matriks
matrix = [lst_1,lst_2,lst_3]

# Tampilkan
matrix

# Sekarang kita dapat menggunakan pengindeksan untuk mengambil elemen, tapi sekarang ada dua tingkat
# untuk indeks. Item dalam objek matriks, dan kemudian item dalam list itu!

# Ambil item pertama dalam objek matriks
matrix[0]

# Ambil item pertama dari item pertama dalam objek matriks
matrix[0][0]
