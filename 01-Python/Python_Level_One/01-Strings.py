##############################
###### Strings ###############
##############################

# Strings digunakan dalam Python untuk merekam informasi teks, seperti nama. Strings
# dalam Python sebenarnya adalah sebuah *urutan*, yang berarti Python melacak
# setiap elemen dalam string sebagai urutan tertentu. Misalnya, Python mengerti
# string "hello" sebagai urutan huruf dalam urutan tertentu. Ini berarti
# kita akan dapat menggunakan indeks untuk mengambil huruf tertentu (seperti huruf pertama,
# atau huruf terakhir).
#
# Ide ini tentang urutan adalah salah satu yang penting dalam Python dan kita akan membahas
# lebih lanjut tentang ini di masa depan.
#
# Dalam kuliah ini kita akan belajar tentang:
#
#     1.) Membuat Strings
#     2.) Mencetak Strings
#     3.) Indeks dan Slicing Strings
#     4.) Properti Strings
#     5.) Metode Strings
#     6.) Format Pencetakan

# Membuat String
# Untuk membuat string dalam Python, Anda perlu menggunakan tanda kutip tunggal atau ganda. Contoh:

# Kata tunggal
'hello'

# Frase lengkap
'This is also a string'

# Kita juga dapat menggunakan tanda kutip ganda
"String dibangun dengan tanda kutip ganda"


# Berhati-hati dengan tanda kutip!
' I\'m using single quotes, but will create an error'


# Alasan untuk kesalahan di atas adalah karena tanda kutip tunggal dalam I'm menghentikan
# string. Anda dapat menggunakan kombinasi tanda kutip tunggal dan ganda untuk mendapatkan pernyataan lengkap.

"Now I\'m ready to use the single quotes inside a string!"


# Sekarang mari kita belajar tentang mencetak strings!

# ## Mencetak String
#
# Menggunakan REPL dengan hanya string dalam sel akan secara otomatis menghasilkan
# strings, tetapi cara yang benar untuk menampilkan strings dalam output Anda adalah dengan menggunakan fungsi print.

# Kita dapat menyatakan string
'Hello World'

# perhatikan bahwa kita tidak dapat menghasilkan beberapa strings dengan cara ini
'Hello World 1'
'Hello World 2'


# Kita dapat menggunakan pernyataan print untuk mencetak string.

print('Hello World 1')
print('Hello World 2')
print('Gunakan \n untuk mencetak baris baru')
print('\n')
print('Lihat apa yang saya maksud?')


# Dasar Strings

# Kita juga dapat menggunakan fungsi yang disebut len() untuk memeriksa panjang string!

len('Hello World')


# ## Indeks Strings
# Kita tahu bahwa strings adalah urutan, yang berarti Python dapat menggunakan indeks untuk memanggil
# bagian dari urutan. Mari kita belajar bagaimana ini bekerja.
#
# Dalam Python, kita menggunakan kurung [] setelah objek untuk memanggil indeksnya. Kita juga harus
# mencatat bahwa indeks dimulai dari 0 untuk Python. Mari kita membuat objek baru
# yang disebut s dan berjalan melalui beberapa contoh indeks.

# Tetapkan s sebagai string
s = 'Hello World'

#Check
s

# Cetak objek
print(s)


# Mari kita mulai indeksing!

# Tampilkan elemen pertama (dalam hal ini huruf)
s[0]

# Elemen berikutnya
s[1]

# Elemen berikutnya
s[2]


# Kita dapat menggunakan : untuk melakukan *slicing* yang mengambil semuanya
# hingga titik yang ditentukan. Misalnya:

# Ambil semuanya setelah istilah pertama hingga panjang s yang adalah len(s)
s[1:]


# Perhatikan bahwa tidak ada perubahan pada s asli
s

# Ambil semuanya HINGGA indeks ke-3
s[:3]


# Perhatikan slicing di atas. Di sini kita memberitahu Python untuk mengambil semuanya dari
# 0 hingga 3. Tidak termasuk indeks ke-3. Anda akan melihat ini banyak di
# Python, di mana pernyataan dan biasanya dalam konteks "hingga, tapi tidak termasuk".

# Semua
s[:]


# Kita juga dapat menggunakan indeks negatif untuk bergerak mundur.
# Huruf terakhir (satu indeks di belakang 0 sehingga berputar kembali)
s[-1]

# Ambil semuanya tapi huruf terakhir
s[:-1]


# Kita juga dapat menggunakan notasi indeks dan slice untuk mengambil elemen dari urutan dengan ukuran langkah tertentu (ukuran langkah default adalah 1). Misalnya:

# Ambil semuanya, tapi pergi dalam ukuran langkah 1
s[::1]

# Ambil semuanya, tapi pergi dalam ukuran langkah 2
s[::2]

# Kita dapat menggunakan ini untuk mencetak string terbalik
s[::-1]


# ## Properti Strings
# Penting untuk dicatat bahwa strings memiliki properti yang penting yaitu
# keabadian. Ini berarti bahwa sekali string dibuat, elemen dalamnya tidak dapat diubah atau diganti. Misalnya:

s

# Mari kita coba mengubah huruf pertama menjadi 'x'
s[0] = 'x'


# Perhatikan bagaimana kesalahan itu memberitahu kita langsung apa yang tidak dapat kita lakukan,
# mengubah penugasan item!
#
# Sesuatu yang dapat kita lakukan adalah menggabungkan strings!
s

# Menggabungkan strings!
s + ' concatenate me!'

# Kita dapat mengubah s sepenuhnya meskipun!
s = s + ' concatenate me!'

print(s)

# Kita dapat menggunakan simbol perkalian untuk membuat pengulangan!

letter = 'z'

letter*10


# ## Metode Strings Dasar
#
# Objek dalam Python biasanya memiliki metode bawaan. Metode-metode ini adalah fungsi
# di dalam objek (kita akan belajar lebih lanjut tentang ini nanti) yang dapat melakukan
# tindakan atau perintah pada objek itu sendiri.
#
# Kita memanggil metode dengan titik dan kemudian nama metode. Metode-metode ini dalam bentuk:
#
# object.method(parameters)
#
# Di mana parameters adalah argumen tambahan yang kita dapat lewatkan ke metode.
# Jangan khawatir jika detailnya tidak 100% masuk akal sekarang. Nanti kita akan
# membuat objek dan fungsi kita sendiri!
#
# Berikut adalah beberapa contoh metode bawaan dalam strings:

# Huruf Besar sebuah string
s.upper()

# Huruf Kecil
s.lower()

# Pisahkan string dengan ruang kosong (ini adalah default)
s.split()

# Pisahkan oleh elemen tertentu (tidak termasuk elemen yang dipisahkan)
s.split('W')

# Ada banyak metode lainnya yang tidak ditutupi di sini.

########################
### Format Pencetakan ###
########################

# Kita dapat menggunakan metode .format() untuk menambahkan objek yang diformat ke pernyataan cetak string.
#
# Cara termudah untuk menunjukkan ini adalah melalui contoh:

'Insert another string with curly brackets: {}'.format('The inserted string')

# Menggunakan metode string .format()
# Cara terbaik untuk memformat objek ke dalam pernyataan cetak Anda adalah menggunakan
# metode format. Sintaksnya adalah:
#
#  'String here {var1} then also {var2}'.format(var1='something1',var2='something2')
#
# Mari kita lihat beberapa contoh:


print('This is a string with an {p}'.format(p='insert'))

# Beberapa kali:
print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi!'))


# Beberapa Objek:
print('Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3))


# Itu dasar dari format string!
# Seringkali kita akan menggunakan bentuk yang lebih sederhana dengan literal f-string (HARUS GUNAKAN PY 3.6 UNTUK INI)
username = "Jose"
color = "Blue"
print(f"The name is {username} and color is {color}")
