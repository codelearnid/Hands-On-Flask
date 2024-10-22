# Tugas Fungsi
#
#
# Mari kita lihat apakah Anda dapat menyelesaikan masalah-masalah ini dengan membuat fungsi.
# "Skeleton" fungsi telah disiapkan untuk Anda isi di bawah deskripsi masalah,
# serta contoh output apa yang harus dikembalikan fungsi tersebut jika diberikan input tertentu. Semoga berhasil, beberapa dari ini akan menantang!
#
# Tugas-tugas akan dimulai dengan mudah dan akan semakin sulit.

# ## Tugas 1
#
# Buat sebuah fungsi yang mengambil dua bilangan bulat dan mengembalikan
## Boolean True jika jumlahnya adalah 10, False jika jumlahnya adalah yang lain.

def cek_sepuluh(n1,n2):

    return (n1 + n2) == 10




cek_sepuluh(10,0)




cek_sepuluh(5,5)




cek_sepuluh(2,7)



# ## Tugas 2
#
# Buat sebuah fungsi yang mengambil dua bilangan bulat dan mengembalikan True jika jumlahnya
# adalah 10, otherwise, return the actual sum value.

def cek_sepuluh_jumlah(n1,n2):
    if (n1+n2) == 10:
        return True
    else:
        return n1+n2




cek_sepuluh_jumlah(10,0)



cek_sepuluh_jumlah(2,7)

# ## Tugas 3
#
# Buat sebuah fungsi yang mengambil sebuah string dan mengembalikan karakter pertama dari string tersebut dalam huruf besar.



def pertama_besar(mystring):
    # Kode Di Sini
    return mystring[0].upper()


pertama_besar('hello')




pertama_besar('agent')


# ## Tugas 4
#
# Buat sebuah fungsi yang mengambil sebuah string dan mengembalikan dua karakter terakhir.
# Jika ada kurang dari dua karakter, kembalikan string: "Error".
# Gunakan tautan ini jika Anda membutuhkan bantuan/petunjuk.
# (https://stackoverflow.com/questions/7983820/get-the-last-4-characters-of-a-string)



def dua_terakhir(mystring):
    if len(mystring) < 2:
        return "Error"
    else:
        return mystring[-2:]



dua_terakhir('hello')


dua_terakhir('hi')


dua_terakhir('a')


# ## Tugas 5
#
# Diberikan sebuah daftar bilangan bulat, kembalikan True jika urutan [1,2,3] ada di mana-mana
# di dalam daftar. Petunjuk: Gunakan slicing dan for loop.





def cek_urutan(nums):

    # Note: iterate with length-2, so can use i+1 and i+2 in the loop
    for i in range(len(nums)-2):
        # Check in sets of 3 if we have 1,2,3 in a row
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False



cek_urutan([1,2,3])



cek_urutan([7,7,7,1,2,3,7,7,7])



cek_urutan([3,2,1,3,2,1,1,1,2,2,3,3,3])


# ## Tugas 6
#
# Diberikan 2 string, buat sebuah fungsi yang mengembalikan perbedaan panjang
# di antara keduanya. Perbedaan panjang ini harus selalu menjadi angka positif
# (atau hanya 0). Petunjuk: Nilai Mutlak.**



def bandingkan_panjang(s1,s2):
    return abs(len(s1)-len(s2))



bandingkan_panjang('aa','aa')


bandingkan_panjang('a','bb')


bandingkan_panjang('bb','a')



# ## Tugas 7
#
# Diberikan sebuah daftar bilangan bulat, jika panjang daftar adalah bilangan genap,
# kembalikan jumlah dari daftar. Jika panjang daftar adalah ganjil, kembalikan nilai maksimum
## di dalam daftar tersebut.



def jumlah_atau_maks(mylist):
    length = len(mylist)

    if length % 2 == 0:
        return sum(mylist)
    else:
        return max(mylist)



jumlah_atau_maks([1,2,3])



jumlah_atau_maks([0,1,2,3])
