### Fungsi
#
# Secara formal, fungsi adalah perangkat yang berguna untuk mengelompokkan set instruksi sehingga dapat dijalankan lebih dari sekali. Mereka juga memungkinkan kita untuk menentukan parameter yang dapat berfungsi sebagai input untuk fungsi-fungsi tersebut.
#
# Pada tingkat yang lebih fundamental, fungsi memungkinkan kita untuk tidak harus menulis kode yang sama berulang-ulang. Jika Anda ingat kembali ke pelajaran tentang string dan list, ingat bahwa kita menggunakan fungsi len() untuk mendapatkan panjang dari sebuah string. Karena memeriksa panjang dari sebuah urutan adalah tugas yang umum, Anda ingin menulis fungsi yang dapat melakukan ini berulang-ulang sesuai perintah.
#
# Fungsi akan menjadi salah satu tingkat dasar dari penggunaan kembali kode di Python, dan ini juga akan memungkinkan kita untuk mulai berpikir tentang desain program (kita akan menyelami ide-ide desain lebih dalam ketika kita belajar tentang Pemrograman Berorientasi Objek).

# ## Pernyataan def
#
# Untuk membuat fungsi kita menggunakan kata kunci **def**. Ini adalah bentuk umum dari sebuah fungsi:



def nama_fungsi_kecil(argument1,argument2,argument3='nilai default'):
    '''
    Ini adalah DocString dari fungsi. Di sini Anda dapat menulis deskripsi yang membantu
    untuk siapa pun yang akan menggunakan fungsi Anda.
    '''
    # Setelah docstring Anda menulis kode yang melakukan sesuatu.


# Kita mulai dengan def lalu sebuah spasi diikuti oleh nama dari fungsi. Cobalah untuk menjaga nama-nama relevan, misalnya len() adalah nama yang baik untuk fungsi panjang(). Juga berhati-hati dengan nama-nama, Anda tidak ingin memanggil fungsi dengan nama yang sama seperti fungsi bawaan di Python (seperti len).
#
# Selanjutnya adalah sepasang kurung dengan sejumlah argumen yang dipisahkan oleh koma. Argumen-argumen ini adalah input untuk fungsi Anda. Anda akan dapat menggunakan input ini dalam fungsi Anda dan mengacu pada mereka. Setelah ini Anda menempatkan titik dua.
#
# Sekarang ini adalah langkah penting, Anda harus mengindent untuk memulai kode di dalam fungsi Anda dengan benar. Python menggunakan whitespace untuk mengatur kode. Banyak bahasa pemrograman lain tidak melakukan ini, jadi perhatikan itu.
#
# Selanjutnya Anda akan melihat doc-string, ini adalah tempat Anda menulis deskripsi dasar dari fungsi. Menggunakan iPython dan iPython Notebooks, Anda akan dapat membaca doc-string ini dengan menekan Shift+Tab setelah nama fungsi. Doc string tidak diperlukan untuk fungsi-fungsi sederhana, tapi ini adalah praktik yang baik untuk memasukkannya sehingga Anda atau orang lain dapat dengan mudah memahami kode yang Anda tulis.

# ____
#
# **Sekarang mari kita berjalan melalui banyak contoh dari fungsi-fungsi yang berbeda.**
# ___

# ### Contoh 1



def lapor_orang():
    print("Melaporkan Orang")


# Jika Anda memanggil fungsi tanpa kurung itu tidak akan berjalan, sebaliknya itu hanya akan melaporkan kembali apa objek itu:

print(lapor_orang)


# Gunakan kurung untuk menjalankan fungsi:
lapor_orang()


# ### Contoh 2
# ** Mengirimkan argumen/parameter **
def lapor(nama):
    print("Melaporkan {}".format(nama))




# Perhatikan kesalahan
lapor()




lapor('Bond')


# ### Contoh 3
# ** Argumen default dapat digunakan untuk mengatur nilai default. **



def lapor(nama='Jason'):
    print('Melaporkan {}'.format(nama))


lapor()




lapor('Kay')


# ## Kata kunci return
# Sampai sekarang semua fungsi kita hanya mencetak hasil, tapi bagaimana jika kita ingin menyimpan hasil aktual dari sebuah fungsi ke variabel lain? Bagaimana kita bisa melakukan ini? Mari kita lihat apa yang terjadi hanya dengan print()


def tambah(n1,n2):
    print(n1+n2)




tambah(2,3)




hasil = tambah(2,3)




print(hasil)




print(type(hasil))


# Perhatikan bagaimana kita tidak dapat menyimpan hasil dari fungsi print(). Itu karena tidak **mengembalikan** apa pun. Mari kita sekarang menggunakan kata kunci return.



def tambah(n1,n2):
    return n1+n2




tambah(2,3)




hasil = tambah(2,3)



print(hasil)








# ### Menyelesaikan Masalah dengan Fungsi
#
# Fungsi adalah blok bangunan dasar untuk skrip dan kode. Mari kita tunjukkan bagaimana Anda bisa menyelesaikan masalah dengan fungsi.

# ** Tulis fungsi yang mengembalikan boolean (True/False) yang menunjukkan apakah kata 'secret' ada dalam sebuah string. **



def cek_secret(mystring):
    return 'secret' in mystring


# In[39]:

cek_secret('This is a secret.')


# In[40]:

cek_secret('SECRET')


# Kita dapat memperbaiki ini dengan .lower()

# In[41]:

def cek_secret(mystring):
    return 'secret' in mystring.lower()


# In[43]:

cek_secret('SECRET!')


# _____

# ** Buat fungsi pembuat kode. Fungsi ini akan mengambil string nama dan menggantikan setiap vokal dengan huruf x.**

# In[53]:

def pembuat_kode(mystring):
    output = list(mystring)
    for i,letter in enumerate(mystring):
        for vowel in ['a','e','i','o','u']:
            if letter.lower() == vowel:
                output[i] = 'x'

    output = ''.join(output)
    return output


# Mari kita lihat apa yang dilakukan oleh **''.join(output)**:



''.join(['a','b','c'])




'--'.join(['a','b','c'])




'-x-'.join(['a','b','c'])




pembuat_kode('Edward')




pembuat_kode('John')


# OPERATOR LAINNYA YANG BERGUNA
print(max(2,3))

mylist = ['a','b','c']

for x in mylist:
    print(x)

for x in enumerate(mylist):
    print(x)

for i, letter in enumerate(mylist):
    print(i)
    print(letter)


#  Karena fungsi sangat penting untuk menjadi programmer Python yang kompeten,
# selanjutnya kita akan memiliki beberapa tugas untuk Anda selesaikan dengan fungsi. Selamat beruntung!
