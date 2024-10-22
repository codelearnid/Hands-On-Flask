##################################
### if,elif, else Statements #####
##################################

# Indentasi sangat penting dalam Python dan pada dasarnya adalah cara Python untuk
# menghilangkan kurung kurawal seperti {} yang kita lihat di masa lalu dan umum
# dengan bahasa lain. Ini menambahkan pada keterbacaan Python dan adalah bagian besar dari
# "Zen of Python". Itu juga adalah alasan besar mengapa sangat populer untuk pemula. Setiap
# editor teks atau IDE harus dapat mengindentasi secara otomatis untuk Anda, tetapi selalu periksa
# ini jika Anda pernah mendapatkan kesalahan dalam kode Anda! Blok kode kemudian dicatat oleh titik dua (:).

# Sekarang mari kita tunjukkan beberapa contoh dari pernyataan if, elif, dan else:

if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')


# If Else - Pastikan untuk mengatur else dengan pernyataan if untuk "menghubungkannya"

if 1 < 2:
    print('pertama')
else:
    print('terakhir')

###
###

if 1 > 2:
    print('pertama')
else:
    print('terakhir')


# Untuk menambahkan lebih banyak kondisi (seperti else if) Anda hanya menggunakan frase tunggal "elif"

if 1 == 2:
    print('pertama')
elif 3 == 3:
    print('tengah')
else:
    print('Terakhir')
