################################################################################
####################-----------------------------###############################
####################-----------LOOPS-------------###############################
####################-----------------------------###############################
################################################################################

# Saatnya untuk mengulas kembali tentang loops di Python, seperti For Loops dan While loops
# Python unik karena menghilangkan tanda kurung dan kurawal dalam favorit sistem whitespace yang
# mendefinisikan blok kode melalui indentasi, ini memaksa pengguna untuk menulis kode yang dapat dibaca,
# yang sangat bagus untuk Anda di masa depan saat melihat kembali kode lama Anda!

#####################
### FOR LOOPS #######
#####################

# Gunakan For Loops untuk setiap urutan elemen. Jika Anda mencoba menggunakan for loop dengan
# peta seperti kamus, itu akan tetap bekerja, tetapi tidak akan berulang dengan urutan tertentu. Mari kita berjalan melalui beberapa contoh tentang bagaimana for loop berperilaku dengan
# struktur data yang kita pelajari!

## For Loop dengan list

# Lakukan tindakan dengan setiap elemen
seq = [1,2,3,4,5]

for item in seq:
    print(item)


# Lakukan tindakan untuk setiap elemen tetapi tidak benar-benar melibatkan elemen-elemen tersebut
for item in seq:
    print('Yep')


# Anda dapat memanggil variabel loop apa pun yang Anda inginkan:
for jelly in seq:
    print(jelly+jelly)

## For Loop dengan Dictionary
ages = {"Sam":3,"Frank":4,"Dan":29}

for key in ages:
    print("Ini adalah kunci")
    print(key)
    print("Ini adalah nilai")
    print(ages[key])
    print("\n")

# Sebuah daftar pasangan tuple adalah format yang sangat umum untuk fungsi mengembalikan data dalam
# Karena itu sangat umum kita dapat menggunakan un-packing tuple untuk menangani ini, contoh:

mypairs = [(1,10),(3,30),(5,50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1,item2 in mypairs:
    print(item1)
    print(item2)

#######################
### WHILE LOOPS #######
#######################

# While loops memungkinkan kita untuk terus melakukan tindakan hingga kondisi
# menjadi benar. Contoh:

i = 1
while i < 5:
    print('i adalah: {}'.format(i))
    i = i+1

#####################
### OTHER TOPICS ####
#####################

# FUNGSI RANGE
# range() dapat dengan cepat menghasilkan bilangan bulat untuk Anda, berdasarkan titik awal dan akhir

# Catatan bahwa itu adalah generator:
range(5)

list(range(5))

for i in range(5):
    print(i)

# Awal dan akhir
range(1,10)

# Argument ketiga untuk ukuran langkah
range(0,10,2)
