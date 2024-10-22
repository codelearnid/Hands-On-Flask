####################
### Dictionaries ###
####################

# Kami telah belajar tentang urutan dalam Python, tetapi sekarang kita akan beralih
# ke "pemetaan" dalam Python. Jika Anda familiar dengan bahasa lain, Anda dapat berpikir tentang Dictionaries ini sebagai tabel hash (objek dalam Javascript).
#
# Bagian ini akan berfungsi sebagai pengenalan singkat tentang dictionaries dan terdiri dari:
#
#     1.) Membangun Dictionaries
#     2.) Mengakses objek dari dictionaries
#     3.) Menggabungkan Dictionaries
#     4.) Metode Dictionaries Dasar
#
# Jadi apa itu pemetaan? Pemetaan adalah koleksi objek yang disimpan oleh
# kunci, tidak seperti urutan yang menyimpan objek berdasarkan posisi relatifnya.
# Ini adalah perbedaan penting, karena pemetaan tidak akan mempertahankan urutan karena mereka
# memiliki objek yang didefinisikan oleh kunci.
#
# Dictionaries Python terdiri dari kunci dan kemudian nilai yang terkait. Nilai itu
# dapat hampir semua objek Python.
#
#
# Membangun Dictionaries
# Mari kita lihat bagaimana kita dapat membangun dictionaries untuk mendapatkan pemahaman yang lebih baik tentang bagaimana mereka bekerja!

# Buat dictionaries dengan {} dan : untuk menandai kunci dan nilai
my_dict = {'key1':'value1','key2':'value2'}

# Panggil nilai dengan kuncinya
my_dict['key2']

# Penting untuk dicatat bahwa dictionaries sangat fleksibel dalam tipe data
# yang mereka pegang. Contoh:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}

# Mari panggil item dari dictionaries
my_dict['key3']

# Dapat memanggil indeks pada nilai itu
my_dict['key3'][0]

#Dapat bahkan memanggil metode pada nilai itu
my_dict['key3'][0].upper()

# Kita juga dapat mempengaruhi nilai kunci. Contoh:
my_dict['key1']

# Kurangi 123 dari nilai
my_dict['key1'] = my_dict['key1'] - 123

# Periksa
my_dict['key1']

# Catatan cepat, Python memiliki metode bawaan untuk melakukan pengurangan atau
# penambahan sendiri (atau perkalian atau pembagian). Kita juga bisa menggunakan += atau -= untuk
# pernyataan di atas. Contoh:

# Tetapkan objek sama dengan dirinya sendiri minus 123
my_dict['key1'] -= 123
my_dict['key1']

print(my_dict)
# Kita juga dapat membuat kunci dengan penugasan. Contoh, jika kita mulai dengan
# dictionaries kosong, kita dapat terus menambahkannya:

# Buat dictionaries baru
d = {}

# Buat kunci baru melalui penugasan
d['animal'] = 'Dog'

# Dapat melakukan ini dengan objek apa pun
d['answer'] = 42

# Tampilkan
print(d)


###############################
# Menggabungkan dengan Dictionaries ###
###############################

# Semoga Anda mulai melihat betapa kuatnya Python dengan fleksibilitasnya dalam
# menggabungkan objek dan memanggil metode pada mereka. Mari kita lihat dictionaries yang
# digabungkan di dalam dictionaries yang digabungkan di dalam dictionaries lainnya:

# Dictionaries yang digabungkan di dalam dictionaries yang digabungkan di dalam dictionaries lainnya
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# Wow! Itu adalah penggabungan yang sangat dalam dari dictionaries!
# Mari kita lihat bagaimana kita dapat mengambil nilai itu:

# Terus panggil kunci-kunci itu
d['key1']['nestkey']['subnestkey']

# Semoga Anda sekarang memiliki pemahaman dasar yang baik tentang bagaimana membangun dictionaries.
# Ada banyak lagi yang perlu dipelajari di sini, tetapi kita akan kembali ke dictionaries di waktu lain.
# Setelah bagian ini, semua yang Anda perlu tahu adalah bagaimana membuat dictionaries dan bagaimana
# mengambil nilai dari itu.
