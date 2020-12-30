# import time
# start_time = time.time()

# print("Heloo")
# a = 10
# print (a)


# kita bisa compile python ke bytecode
# python -m py_compile Main.py

# print(time.time() - start_time, "detik")

#  Tipe data yang diambil dari bahasa C
# from ctypes import c_double, c_char

# data_c_double = c_double(10.5)
# print("data : ", data_c_double)
# print("- bertipe : ", type(data_c_double))

# casting tipe data
# data_int = 9;
# print("data = ", data_int, ",type =",type(data_int))


# data_float = float(data_int);
# print("data = ", data_float, ",type =",type(data_float))

# # Kita belajar Casting
# # merubah dari satu tipe ke tipe lain
# # tipe data = int, float, str, bool

# ## INTEGER
# print("====INTEGER====")
# data_int = 9;
# print("data = ", data_int, ",type =",type(data_int))

# data_float = float(data_int)
# data_str   = str(data_int)
# data_bool  = bool(data_int) # akan false jika nilai int = 0
# print("data = ", data_float, ",type =",type(data_float))
# print("data = ", data_str, ",type =",type(data_str))
# print("data = ", data_bool, ",type =",type(data_bool))

# ## FLOAT
# print("====FLOAT====")
# data_float = 0;
# print("data = ", data_float, ",type =",type(data_float))

# data_int = int(data_float) # akan dibulatkan ke bawah
# data_str   = str(data_float)
# data_bool  = bool(data_float) # akan false jika nilai float = 0
# print("data = ", data_int, ",type =",type(data_int))
# print("data = ", data_str, ",type =",type(data_str))
# print("data = ", data_bool, ",type =",type(data_bool))

# ## BOOLEAN
# print("====BOOLEAN====")
# data_bool = True;
# print("data = ", data_bool, ",type =",type(data_bool))

# data_int = int(data_bool) # akan dibulatkan ke bawah
# data_str   = str(data_bool)
# data_float  = float(data_bool) # akan false jika nilai float = 0
# print("data = ", data_int, ",type =",type(data_int))
# print("data = ", data_str, ",type =",type(data_str))
# print("data = ", data_float, ",type =",type(data_float))

# ## STRING
# print("====STRING====")
# data_str = "10";
# print("data = ", data_str, ",type =",type(data_str))

# data_int    = int(data_str) # string harus angka
# data_float  = float(data_str)  # string harus angka
# data_bool   = bool(data_str) # false jika string kosong
# print("data = ", data_int, ",type =",type(data_int))
# print("data = ", data_float, ",type =",type(data_float))
# print("data = ", data_bool, ",type =",type(data_bool))

# Episode input user

# data yang dimasukan pasti string
# data = input("Masukan data: ")

# print("data = ",data,",type =",type(data))

# # jika kita ingin mengambil int, maka
# angka = float(input("masukan angka: "))
# angka = int(input("masukan angka: "))

# print("data = ",angka,",type =",type(angka))

# # bagaimana dengan boolean
# biner = bool(int(input("masukan nilai boolean: ")))

# print("data = ",biner,",type =",type(biner))

# operasi aritmatika

# a = 10
# b = 3

# # operasi tambah +
# hasil = a + b
# print(a,'+',b,'=',hasil)

# # operasi pengurangan -
# hasil = a - b
# print(a,'-',b,'=',hasil)

# # operasi perkalian *
# hasil = a * b
# print(a,'*',b,'=',hasil)

# # operasi pembagian /
# hasil = a / b
# print(a,'/',b,'=',hasil)

# # operasi eksponen (pangkat) **
# hasil = a ** b
# print(a,'**',b,'=',hasil)

# # operasi modulus %
# hasil = a % b
# print(a,'%',b,'=',hasil)

# # operasi floor division //
# hasil = a // b
# print(a,'//',b,'=',hasil)

# # prioritas operasi, operational precedence
# '''
#     1. ()
#     2. exponen **
#     3. perkalian dan teman-teman * / ** % //
#     4. pertambahan dan pengurangan + -
# '''
# x = 3
# y = 2
# z = 4

# hasil = x ** y * (z + x) / y - y % z // x
# print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# hasil = x + y * z
# print(x,'+',y,'*',z,'=',hasil)
# # kurung akan mengambil langkah paling pertama
# hasil = (x + y) * z 
# print('(',x,'+',y,') *',z,'=',hasil)

# operasi aritmatika

# a = 10
# b = 3

# # operasi tambah +
# hasil = a + b
# print(a,'+',b,'=',hasil)

# # operasi pengurangan -
# hasil = a - b
# print(a,'-',b,'=',hasil)

# # operasi perkalian *
# hasil = a * b
# print(a,'*',b,'=',hasil)

# # operasi pembagian /
# hasil = a / b
# print(a,'/',b,'=',hasil)

# # operasi eksponen (pangkat) **
# hasil = a ** b
# print(a,'**',b,'=',hasil)

# # operasi modulus %
# hasil = a % b
# print(a,'%',b,'=',hasil)

# # operasi floor division //
# hasil = a // b
# print(a,'//',b,'=',hasil)

# # prioritas operasi, operational precedence
# '''
#     1. ()
#     2. exponen **
#     3. perkalian dan teman-teman * / ** % //
#     4. pertambahan dan pengurangan + -
# '''
# x = 3
# y = 2
# z = 4

# hasil = x ** y * (z + x) / y - y % z // x
# print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

# hasil = x + y * z
# print(x,'+',y,'*',z,'=',hasil)
# # kurung akan mengambil langkah paling pertama
# hasil = (x + y) * z 
# print('(',x,'+',y,') *',z,'=',hasil)

# latihan konversi satuan temperature

# program konversi celcius ke satuan lain

# print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input('Masukan suhu dalam celcius : '))
# print("suhu adalah",celcius, "Celcius")

# # reamur
# reamur = (4/5) * celcius
# print("suhu dalam reamur adalah ",reamur, "Reamur")

# # fahrenheit
# fahrenheit = ((9/5) * celcius) + 32
# print("suhu dalam fahrenheit adalah ",fahrenheit, "Fahrenheit")

# # Kelvin
# kelvin = celcius + 273
# print("suhu dalam kelvin adalah ",kelvin, "Kelvin")


# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

# a = 4
# b = 2

# # lebih besar dari >
# print('========== lebih besar dari (>)')
# hasil = a > 3
# print(a,'>',3,'=',hasil)
# hasil = b > 3
# print(b,'>',3,'=',hasil)
# hasil = b > 2
# print(b,'>',2,'=',hasil)

# # kurang dari <
# print('========== kurang dari (<)')
# hasil = a < 3
# print(a,'<',3,'=',hasil)
# hasil = b < 3
# print(b,'<',3,'=',hasil)
# hasil = b < 2
# print(b,'<',2,'=',hasil)

# # lebih dari sama dengan >=
# print('========== lebih dari sama dengan(>=)')
# hasil = a >= 3
# print(a,'>=',3,'=',hasil)
# hasil = b >= 3
# print(b,'>=',3,'=',hasil)
# hasil = b >= 2
# print(b,'>=',2,'=',hasil)

# # kurang dari sama dengan <=
# print('======== kurang dari sama dengan(<=)')
# hasil = a <= 3
# print(a,'<=',3,'=',hasil)
# hasil = b <= 3
# print(b,'<=',3,'=',hasil)
# hasil = b <= 2
# print(b,'<=',2,'=',hasil)

# # sama dengan (==)
# print('======== sama dengan(==)')
# hasil = a == 4
# print(a,'==',4,'=',hasil)
# hasil = b == 4
# print(b,'==',4,'=',hasil)

# # tidak sama dengan (!=)
# print('======== sama dengan(!=)')
# hasil = a != 4
# print(a,'!=',4,'=',hasil)
# hasil = b != 4
# print(b,'!=',4,'=',hasil)

# # 'is' sebagai komparasi object identity
# print('======== object identity(is)')
# x = 5 # ini adalah assignment membuat object
# y = 5
# print('nilai x =',x,',id = ',hex(id(x)))
# print('nilai y =',y,',id = ',hex(id(y)))
# hasil = x is y
# print('x is y =',hasil)

# x = 5 # ini adalah assignment membuat object
# y = 6
# print('nilai x =',x,',id = ',hex(id(x)))
# print('nilai y =',y,',id = ',hex(id(y)))
# hasil = x is y
# print('x is y =',hasil)

# print('======== object identity(is not)')
# x = 5 # ini adalah assignment membuat object
# y = 5
# print('nilai x =',x,',id = ',hex(id(x)))
# print('nilai y =',y,',id = ',hex(id(y)))
# hasil = x is not y
# print('x is y =',hasil)

# x = 5 # ini adalah assignment membuat object
# y = 6
# print('nilai x =',x,',id = ',hex(id(x)))
# print('nilai y =',y,',id = ',hex(id(y)))
# hasil = x is not y
# print('x is y =',hasil)

# # operasi logika atau boolean

# # not, or, and, xor

# # NOT
# print('====NOT====')
# a = False
# c = not a
# print('data a =',a)
# print('-------------- NOT')
# print('data c =',c)

# # OR (jika salah satu true, maka hasilnya adalah true)
# print('====OR====')
# a = False
# b = False
# c = a or b
# print(a,'OR',b,'=',c)
# a = False
# b = True
# c = a or b
# print(a,'OR',b,' =',c)
# a = True
# b = False
# c = a or b
# print(a,' OR',b,'=',c)
# a = True
# b = True
# c = a or b
# print(a,' OR',b,' =',c)

# # AND (jika dua buah nilai true, maka hasil true)
# print('====AND====')
# a = False
# b = False
# c = a and b
# print(a,'AND',b,'=',c)
# a = False
# b = True
# c = a and b
# print(a,'AND',b,' =',c)
# a = True
# b = False
# c = a and b
# print(a,' AND',b,'=',c)
# a = True
# b = True
# c = a and b
# print(a,' AND',b,' =',c)

# # XOR (akan true jika salah satu true, sisanya false)
# print('====XOR====')
# a = False
# b = False
# c = a ^ b
# print(a,'XOR',b,'=',c)
# a = False
# b = True
# c = a ^ b
# print(a,'XOR',b,' =',c)
# a = True
# b = False
# c = a ^ b
# print(a,' XOR',b,'=',c)
# a = True
# b = True
# c = a ^ b
# print(a,' XOR',b,' =',c)


# episode latihan logika dan komparasi

# membuat gabungan area rentang dari angka

# ++++++3--------10+++++++

# inputUser = float(input("masukan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# # ++++++3-----------------
# # Memeriksa angka kurang dari 3
# isKurangDari = (inputUser < 3)
# print("Kurang dari 3 =", isKurangDari)

# # ---------------10++++++++
# # Memeriksa angka lebih dari 10
# isLebihDari = (inputUser > 10)
# print("Lebih dari 10 =", isLebihDari)

# # ++++++3--------10+++++++

# isCorrect = isKurangDari or isLebihDari
# print("angka yang anda masukan: ", isCorrect)


# # -----3++++++++10--------
# # kasus irisan
# print("\n",10*"=","\n")
# inputUser = float(input("masukan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# # -----3++++++++++++++++++
# # lebih dari 3
# isLebihDari = inputUser > 3
# print("Lebih dari 3 = ",isLebihDari)

# # +++++++++++++++10-------
# # kurang dari 10
# isKurangDari = inputUser < 10
# print("Kurang dari 10 = ",isKurangDari)

# # -----3++++++++10--------
# isCorrect = isKurangDari and isLebihDari
# print("angka yang anda masukan: ", isCorrect)


# episode operator bitwise, operasi biner, binary

# a = 9
# b = 5

# # bitwise OR (|)
# c = a | b
# print('\n=========OR=========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('nilai :',b,' , binary :',format(b,'08b'))
# print('----------------------------- (|)')
# print('nilai :',c,' , binary :',format(c,'08b'))

# # bitwise AND (&)
# c = a & b
# print('\n=========AND========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('nilai :',b,' , binary :',format(b,'08b'))
# print('----------------------------- (&)')
# print('nilai :',c,' , binary :',format(c,'08b'))

# # bitwise XOR (^)
# c = a ^ b
# print('\n=========XOR========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('nilai :',b,' , binary :',format(b,'08b'))
# print('----------------------------- (^)')
# print('nilai :',c,' , binary :',format(c,'08b'))

# # bitwise NOT (~)
# c = ~a
# print('\n=========NOT========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('----------------------------- (~)')
# print('nilai :',c,' , binary :',format(c,'08b'))
# print('----------------------------- (^)')
# d = 0b0000001001
# e = 0b1111111111
# print('nilai :',e^d,' , binary :',format(e^d,'08b'))

# # shifting

# # shift right (>>)
# c = a >> 2
# print('\n=========>>=========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('----------------------------- (>>)')
# print('nilai :',c,' , binary :',format(c,'08b'))

# # shift left (<<)
# c = a << 2
# print('\n=========<<=========')
# print('nilai :',a,' , binary :',format(a,'08b'))
# print('----------------------------- (<<)')
# print('nilai :',c,' , binary :',format(c,'08b'))


# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

# a = 5 # adalah assignment
# print("nilai a =",a)

# a += 1 # artinya adalah a = a + 1
# print("nilai a += 1, nilai a menjadi",a)

# a -= 2 # artinya adalah a = a - 2
# print("nilai a -= 2, nilai a menjadi",a)

# a *= 5 # artinya adalah a = a * 5
# print("nilai a *= 5, nilai a menjadi",a)

# a /= 2 # artinya adalah a = a / 2
# print("nilai a /= 2, nilai a menjadi",a)

# b = 10
# print("\nnilai b =",b)

# # modulus dan floor division
# b %= 3
# print("nilai b %= 3, nilai b menjadi",b)

# b = 10
# print("\nnilai b =",b)

# b //= 3
# print("nilai b //= 3, nilai b menjadi",b)

# # pangkat atau eksponen
# a = 5
# print("\nnilai a =",a)
# a **= 3
# print("nilai a **= 3, nilai a menjadi",a)

# # operasi bitwise
# # OR
# c = True
# print("\nnilai c =",c)
# c |= False
# print("nilai c |= False, nilai c menjadi",c)
# c = False
# print("nilai c =",c)
# c |= False
# print("nilai c |= False, nilai c menjadi",c)

# # AND
# c = True
# print("\nnilai c =",c)
# c &= False
# print("nilai c &= False, nilai c menjadi",c)
# c = True
# print("nilai c =",c)
# c &= True
# print("nilai c &= True, nilai c menjadi",c)

# # XOR
# c = True
# print("\nnilai c =",c)
# c ^= False
# print("nilai c ^= False, nilai c menjadi",c)
# c = True
# print("nilai c =",c)
# c ^= True
# print("nilai c ^= True, nilai c menjadi",c)

# # geser geser
# d = 0b0100
# print("\nnilai d =",format(d,'04b'))
# d >>= 2
# print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
# d <<= 1
# print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))



# Pengenalan String
# data = "ini adalah string"
# print(data)
# print(type(data))

# # 1. cara membuat string

# '''
#     1. dengan menggunakan single quote '...'
#     2. dengan menggunakan double quote "..."
# '''

# data = 'Menggunakan single quote'
# print(data)

# data = "Menggunakan double quote"
# print(data)

# print('"Halo, apa kabar?"')
# print("'Halo, apa kabar?'")
# print("ini adalah hari jum'at")

# # 2. Menggunakan tanda \

# # membuat tanda ' menjadi string
# print('mari shalat jum\'at')
# print('g\'day, isn\'t it?')

# # backlash
# print("C:\\user\\Ucup")

# # tab
# print("ucup\t\t\totong, semakin jauhan")
# print("ucup\t\t\totong, semakin jauhan")
# print("ucup\t\t\totong, semakin jauhan")



# # backspace
# # backspace
# # backspace
# print("ucup \botong, jadi deketan")

# # newline
# print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
# print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
# print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# # 3. String literal atau raw

# # hati-hati
# print('C:\new folder') # akan salah pathnya

# # menggunakan raw string
# print(r'C:\new folder')

# # multiline literal string
# print("""
# Nama : Ucup
# Kelas : 3 SD   
# """)

# # multiline literal string dan RAW
# print(r"""
# Nama : Ucup
# Kelas : 3 SD\new normal 
# Website : www.ucup.com/newID
# """)


# Manipulasi String
# Operasi dan manipulasi string

# 1/ menyambnung string concatenate
# nama_pertama = "ucup"
# nama_tengah = "D"
# nama_akhir = "Pame"

# nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
# print(nama_lengkap)

# # 2. Menghitung panjang String
# panjang = len(nama_lengkap)
# print(panjang)

# # 3. operator untuk string
# # mengecek apakah ada komponen char atau string di string

# d = "d"
# status = d in nama_lengkap
# print(d + " ada di " + nama_lengkap + " = " + str(status))


# D = "D"
# status = D in nama_lengkap
# print(D + " ada di " + nama_lengkap + " = " + str(status))

# d = "d"
# status = d not in nama_lengkap
# print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# # mengulang string
# print("wk"*10)
# print(20*"wk")

# # indexing
# print("index ke-0 : " + nama_lengkap[0])
# print("index ke--1 : " + nama_lengkap[-1])
# print("index ke-(0:3) : " + nama_lengkap[0:4])
# print("index ke-(3:7) : " + nama_lengkap[3:8])
# print("index ke-(0,2,4,6,8,10) : " + nama_lengkap[0:10:2])

# # item paling kecil
# print("paling kecil : " + min(nama_lengkap))
# # item paling besar
# print("paling besar : " + max(nama_lengkap))

# ascii_code = ord(" ")
# print("ASCII code untuk spasi adalah " + str(ascii_code))
# data = 117
# print("char untuk ASCII 117 adalah " + chr(data))

# # 4. operator dalam bentuk method
# data = "otong surotong pararatong"
# jumlah = data.count("o")
# print("jumlah o pada " + data + " = " + str(jumlah))





# Version Lama
# List
# Data = [1,4,9,16,25,36,49,64]
# # mengakses list
# Subdata1 = Data[3]
# Subdata2 = Data[-3]
# # memotong list
# Subdata3 = Data[2:4]
# Subdata4 = Data[:4]
# Data2 = [100,200,300,400,500,600,700,800]
# # menambah list
# Data3 = Data + Data2
# # merubah content dari list
# Data[4] = 87
# # Mengcopy list ke variable baru
# a = Data[:]
# a[7] = 87
# # merubah content list dengan menggunakan metoda slicing
# Data[3:5] = [11,12]
# # List dalam list
# x = [Data,Data2]
# # mengakses list dalam multidimensional list
# y = x[1][4]
# # methods untuk list
# Data.append(30)
# # Function yang bisa kita gunakan kepada list
# panjang_list = len(Data)
# print(Data)
# print(panjang_list)

# if elif else
# nilai = 50

# if nilai == 75: # equal eksplisit
#     print("nilai anda:",nilai)

# if nilai is 60: # equal
#     print("nilai anda:", nilai)

# if nilai is not 60: # not equal
#     print("nilai anda bukan: 60")

# print(100*"=")

# nilai = 65

# if 80 <= nilai <= 100:
#     print("nilai anda adalah A")
# elif 70 <= nilai < 80:
#     print("nilai anda adalah B")
# elif 60 <= nilai < 70:
#     print("nilai anda adalah C")
# elif 50 <= nilai < 60:
#     print("nilai anda adalah T, lakukan perbaikan")
# else:
#     print("maaf anda tidak lulus mata kuliah ini")

# print(100*"+")
# print("operator logika untuk list dan string")
# print(" ")

# gorengan=["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]
# beli = "sepatu"

# if beli in gorengan:
#     print('Mamang bilang, " ya, saya jual',beli,'"')

# if not beli in gorengan:
#     print('"saya gak jual',beli,'"')

# karakter = "z"
# if karakter in beli:
#     print("ada", karakter, "di",beli)
# else:
#     print("tidak ada",karakter,"di",beli)

# for loop
# list sebagai iterable
# gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']

# for g in gorengan:
#     print(g)
#     print(len(g))

# # string sebagai iterable

# bakwan = 'bakwan'

# for i in bakwan:
#     print(i)

# for di dalam for
# gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']
# buah = ['semangka','jeruk','apel','anggur']
# sayur = ['kangkung','wortel','tomat','kentang']

# Daftar_belanja = [gorengan,buah,sayur]

# for subDaftarBelanja in Daftar_belanja:
#     print(subDaftarBelanja)
#     for komponen in subDaftarBelanja:
#         print(komponen)

# for else,range,break
# number = 50;

# for i in range(0,40):
#     print(i)

#     if i is number:
#         print('angka ditemukan',i)
#         break
# else:
#     print('angka tidak ditemukan')

# print("space di luar for")

# continous and pass
# for i in range(1,10):

#     if i is 6:
#         print("nilai i adalah",6)
#         # break : fungsinya untuk mengakhiri for (terminasi)
#         # continue : fungsinya untuk melanjutnya ke step berikutnya
#         pass
#         print("cek bro 1")

#     print('nilai saat ini adalah',i)
# else:
#     print('akhir dari loop')

# print('print diluar loop')

# while loop
# angka = 0

# while angka < 5:
#     print( 'nilai angka adalah:', angka)
#     angka = angka + 1

# print('di luar while')

# start = True # variable boolean
# angka = 0

# while start:
#     print("di dalam while")
#     if angka is 100:
#         start = False
#         print('oke angka 100 diketemukan')
#     angka += 1

      
# else, break, continue, pass

# angka = 0

# while angka < 10:

#     if angka is 5:
#         # print('checkpoint 1')
#         break
#         continue
#         pass
#         # print('checkpoint 2')

#     print( 'nilai angka adalah:', angka)
#     angka += 1
# else:
#     print('nilai angka diakhir while adalah',angka)

# print('di luar while')

# function
# membuat fungsi sederhana
# def suaraayam():
#     print('kukuruyuk!!!!')

# def hargaayam():
#     suaraayam()
#     print('harga ayam per 1 kg adalah Rp. 20.000')

# # membuat fungsi dengan input argumen
# def hargatotalayam(kg):
#     suaraayam()
#     harga = 20000
#     hargaTotal = kg*harga
#     print('harga',kg,'kg ayam adalah',hargaTotal)

# hargaayam()
# hargatotalayam(2)
# hargatotalayam(0.5)
# hargatotalayam(1)
# hargatotalayam(9)

# fungsi dan arguments
# fungsi dengan menggunakan argumen sederhana
# def siswa(nama):
#     print('siswa ini bernama:',nama)

# siswa('mario')

# fungsi dengan menggunakan keywords arguments

# def guru(nama,pelajaran):
#     print('guru ini bernama:',nama)
#     print('mengajar:',pelajaran)

# guru(nama='popong',pelajaran='seni rupa')
# guru(pelajaran='olah raga',nama='endang')
# guru('olah raga','raihan') # ini contoh yang salah

# # fungsi dengan menggunakan default arguments

# def penjagaSekolah(nama,shift='siang',galak='tidak'):
#     print('penjaga sekolah ini bernama:', nama)
#     print('shiftnya:', shift)
#     print('galak?:', galak)

# penjagaSekolah('Entis')
# penjagaSekolah('Maman',shift='malam')
# penjagaSekolah('Asep',galak='Sangat')
# penjagaSekolah(shift='malam',galak='iya') # menghasilkan error

# fungsi dengan return value
# def kuadrat(argumen):
#     total = argumen**2
#     print('nilai kuadrat dari',argumen,'adalah:',total)
#     return total

# a = kuadrat(4)
# print(a)

# print('+'*100)

# fungsi dengan return value dan multiple argumen
# def tambah(argumen1,argumen2):
#     total = argumen1 + argumen2
#     print(argumen1,'+',argumen2,'=',total)
#     # return total

# def kali(argumen1,argumen2):
#     total = argumen1 * argumen2
#     print(argumen1,'x',argumen2,'=',total)
#     # return total

# b = kali(3,tambah(3,4))

# print(b)

# lambda function
# def jumlah(a,b):
#     c = a+b
#     return c

# hasil = jumlah(4,5)

# # membuat anonymous function dengan lambda
# # kali = lambda argumen: print(argumen)
# # kali('test')

# kali = lambda x,y: x*y
# hasil = kali(3,4)
# print(hasil)

  
# scope variable : global

# namaKucing = 'cassandra'
# makananKucing = 'royal canin'

# def rubahNamaKucing(namaBaru):
#     global namaKucing
#     namaKucing = namaBaru # variable global
#     nama = namaBaru # variable local
#     print('saya rubah nama kucing menjadi',namaKucing)

# def kasihMakanKucing(makanan,nama):
#     global namaKucing,makananKucing
#     namaKucing = nama
#     makananKucing = makanan

# rubahNamaKucing('ketie')

# kasihMakanKucing('universal','alex')

# print('nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)

# more list
# Barang = ['kunci','ember','jaket','ban','mobil']
# print(Barang)

# # beberapa method yang bisa digunakan untuk memanipulasi list
# # method untuk menambah data kedalam list
# Barang.append('sepeda')
# print(Barang)

# Barang.extend('dompet')
# print(Barang)

# Barang.insert(3,'sepeda')
# print(Barang)

# # method untuk menghitung anggota
# jumlahSepeda = Barang.count('sepeda')
# print("Jumlah sepeda adalah: ",jumlahSepeda)

# # meremove data
# Barang.remove('sepeda')
# print(Barang)

# Barang.reverse()
# print(Barang)

# print("="*100)
# Stuff = Barang.copy()
# Stuff.append('gelas')
# print(Stuff)
# print(Barang)


# stack and queue
# tumpukan
# tumpukan = [1,2,3,4,5,6]
# print('data sekarang: ',tumpukan)

# # memasukan data baru
# tumpukan.append(7)
# print('data masuk: ',7)
# print('data sekarang: ',tumpukan)
# tumpukan.append(8)
# print('data masuk: ',8)
# print('data sekarang: ',tumpukan)

# out = tumpukan.pop()
# print('data keluar: ',out)
# print('data sekarang: ',tumpukan)

# # antrian
# from collections import deque

# antrian = deque([1,2,3,4,5])

# print('data sekarang: ',antrian)

# # menambahkan data
# antrian.append(6)
# print('data masuk: ',6)
# print('data sekarang: ',antrian)

# antrian.append(7)
# print('data masuk: ',7)
# print('data sekarang: ',antrian)

# # mengurangi antrian
# out = antrian.popleft()
# print('data keluar: ',out)
# print('data sekarang: ',antrian)

# out = antrian.popleft()
# print('data keluar: ',out)
# print('data sekarang: ',antrian)

# out = antrian.popleft()
# print('data keluar: ',out)
# print('data sekarang: ',antrian)

# antrian.append(8)
# print('data masuk: ',8)
# print('data sekarang: ',antrian)


# tuple
# import sys

# data_list = [1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14]
# data_tuple = (1,2,3,4,5,6,7,8,9,10,"pisang goreng","syahrini","via vallen", False, 3.14)

# besar_datalist = sys.getsizeof(data_list)
# besar_datatuple = sys.getsizeof(data_tuple)

# print("besar data list:", besar_datalist)
# print("besar data tuple:", besar_datatuple)

# import timeit

# data_list = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=1000000)
# data_tuple = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=1000000)

# print("waktu untuk memproses list:",data_list)
# print("waktu untuk memproses tuple:",data_tuple)

# # List
# Ganjil = [1,3,5,7,9]

# # Tuple
# Genap = (2,4,6,6,8,10)

# print(type(Ganjil))
# print(type(Genap))

# print(Genap)

# # set
# # set, himpunan:

# superhero = set()

# superhero.add("wiro sableng")
# superhero.add("gundala")
# superhero.add("saras 008")
# superhero.add(212)

# print(superhero)

# ganjil = {1,3,5,7,9}
# genap = {2,4,6,8,10}
# prima = {2,3,5,7}

# print(ganjil.union(genap))
# print(ganjil.intersection(prima))

# dictionary

# member1 = {"ID":101,
#            "Nama":"Faqihza Mukhlish",
#            "Pekerjaan":"Mahasiswa",
#            "Status member":"Gold"
#            }

# member2 = {"ID":102,
#            "Nama":"Ujang Pintu",
#            "Pekerjaan":"reparasi pintu",
#            "Status member":"Berlian"}

# memberlist = {101:member1,102:member2}

# print(memberlist[101])

# teknik looping
# nama_band = ['Payung Teduh',
#              'Fourtwnty',
#              'Dialog Dini Hari',
#              'Mr. Sonjaya',
#              'Parahyena',
#              'Syahrini']

# kumpulan_lagu = ['Akad',
#         'Zona Nyaman',
#         'Rumahku',
#         'Sang Filsuf',
#         'Sindoro',
#         'Jodohku']

# # enumerate
# for index,band in enumerate(nama_band):
#     print(index,':',band)

# # zip
# for band,lagu in zip(nama_band,kumpulan_lagu):
#     print(band,'menyanyikan lagu yang berjudul:',lagu)

# # set
# playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang', 'jaran goyang', 'gorgom', 'kuda', 'kucing'}

# for lagu in sorted(playlist):
#     print(lagu)

# # dictionary
# print('='*100)

# playlist2 = {'Payung Teduh': 'akad',
#              'Fourtwnty':'Zona Nyaman',
#              'Dialog Dini Hari':'Rumahku',
#              }

# for i,v in playlist2.items(): 
#     # items / keys / values
#     print(i,'lagunya:',v)

# for i in reversed(range(1,10,1)):
#     print(i)

# import
# import modul

# print(modul.data)

# modul.cek_modul()

# # in file modul.py
# data = "apa kabs?"

# def cek_modul():
#     print("hallo gan")

# print("ini adalah modul saya")

# membuat package
# import matematika
# matematika.tambah(3,2)
# import matematika as math
# from matematika import tambah, kurang
# from matematika import *
# from sains import tambah, kurang
# from sains

# import math
# print(math.cos(3.14))

# sains.waktu_tempuh()
# tambah(2,1)
# print(__name__) 

# class
# class Mahasiswa():
#     # pass -> class kosong
# 	nama = 'nama'

# otong = Mahasiswa()
# ucup = Mahasiswa()

# otong.nama = "otong surotong"
# ucup.nama = "michael ucup"

# print(otong.nama)
# print(ucup.nama)

# class membuat method 
#class
class Mahasiswa():
	nama = 'nama'

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)

	def tidur(self):
		print(self.nama,'tidur di kelas')

# main programnya
# otong = Mahasiswa()
# ucup = Mahasiswa()

# otong.nama = "otong surotong"
# ucup.nama = "michael ucup"

# otong.belajar('dengan giat')
# ucup.tidur()

# class init
#class
class Mahasiswa():
	nama = 'nama'

	def __init__(self, input_nama, input_nim):
		self.nama = input_nama
		self.nim = input_nim

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)

	def tidur(self):
		print(self.nama,'tidur di kelas')

# main programnya

otong = Mahasiswa("otong surotong", 13317001)
#ucup = Mahasiswa()

print(otong.nama)
otong.nama = "atong suratang"
print(otong.nama)

#ucup.nama = "michael ucup"
otong.belajar('dengan giat')
#ucup.tidur()

# class private attribute
# class
class mahasiswa():

    jurusan = "teknik tata boga"
    __nilai = 0 # private

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama,'tidak lulus')
        else:
            print(self.nama, 'lulus')

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)

otong.uts(10)
otong.uas(50)
otong.check_status()
ucup.uts(5)
ucup.uas(25)
ucup.__nilai = 60
ucup.check_status()

# class variable
# class
class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama # public
        self.nim = input_nim  # public
        mahasiswa.jumlah_mahasiswa += 1

# main programnya

otong = mahasiswa("otong surotong", 13317001)
ucup = mahasiswa("michael ucup", 13317002)
cassandra = mahasiswa("cassandra aja", 13317002)

print(mahasiswa.jumlah_mahasiswa)
# print(ucup.__dict__)

# class inheritance
class Ojek():

    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama:',self.nama,'\nmotor:',self.transmisi,'\ndaerah:',self.daerah)

class Gojek(Ojek):

    def cek_id_abang(self):
        print('cek aplikasi gojek')


ojek1 = Ojek('mario','manual','bandung selatan')
ojek2 = Gojek('jackson','automatic','tasikmalaya')

ojek1.cek_id_abang()
ojek2.cek_id_abang()


# input output file
"""
w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = write and read mode
"""
# membuat file text
file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")

file.close()

# membaca file text
file2 = open("data.txt",'r')

#print(file2.read(10))
print(file2.readline())

file2.close()


# appending mode    
file3 = open("data.txt", 'a')

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()

# Membuat GUI dengan Built-in package tkinter 
import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="aku ditekan ^_^")
    label2.pack()


label = tkinter.Label(main_window, text="halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
tombol = tkinter.Button(main_window, text="tekan akuh", command = event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()


# Menginstall eksternal package dengan pip
# pip list --format=columns
from PIL import Image

im = Image.open("foto.jpg")

print("format file: " + im.format)
print("ukuran file: " + str(im.size))
print("mode file: " + im.mode)

im.show()

# Virtual environment
# pyhton -m venv project1
# which python
# source project1/bin/activate
# deactivate

# Migrasi environment
# pip freeze  --local > requirement.txt
# pindahkan file txt ke environemtn yg diinginkan
# pip install -r requirement.txt


# try and exception
print("ini adalah program pembagian")

while True:
    try:
        import panda
        penyebut = int(input("masukan angka penyebut: "))
        pembilang = int(input("masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:
        print("angka pembilang yang anda masukan adalah nol, pilih yang lain ya bro/sist\n")
    except ImportError:
        print("gak ada modulnya bro")
    except Exception as err:
        print(err)

"""
    type of exception errors:
    1. IOError
    2. ImportError
    3. ValueError
    4. Division by zero
    5. KeyboardInterupted
    6. EOFError
"""

print("berhasil, hasil pembagian adalah: ", hasil)