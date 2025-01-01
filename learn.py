"""
asdasdsad
asdasdadssa
dasdsadsad
sadasd
adas
das
dasasdsad
sadas
d
asd
asd
asd
asd
sadasd
"""

a = str(5)
A = str(10)
# print(A)

x, y, z = "banana","apple","semangka"

# print(x)
# print(y)
# print(z)

x = y = z = "orange"

# print(x)
# print(y)
# print(z)

fruits = ["banana","apple","semangka"]
x , y , z = fruits

# print(x)
# print(y)
# print(z)

# print(x,y,z)

x = 2
y = "apple"

# print(x,y)

x = "keren"

def myFun():
    x = "mantap" # ketimpa
    print("python itu ",x)

# myFun()

def myFun():
    global x
    x = "alamak"

# myFun()

string = "hello word"
integer = 20
float = 20.5
complex = 3 + 1j + 2j - 1
list = ["apple","mangga","semangka"]
tuple = ("apple","mangga","semangka") # list permanen (tidak bisa dirubah rubah)
dict = {
    "nama":"budi",
    "hobi" : "monopoli",
    "lahir" : "2001"
}
set = {"budi","monopoli","2001"} # enggak bisa diambil satuan harus dilooping dan sifatnya unik
fronzeset = frozenset({"budi","monopoli","2001"}) # set permanen enggak bisa diapa apain
bool = True
byte = b"hello" # bisa diambil satu satu hurufnya kaya h atau ell
bytearray = bytearray(1)
memoryview = memoryview(bytes(5))


# print(memoryview)

# print(complex)
# print(complex.imag)
# print(complex.real)

# print(list[0])

def generateNumber () :
    i = 0
    while i < 100:
        i += 1
        yield i
    else:
        yield 100

angka = generateNumber()
# print(next(angka))
# print(next(angka))
# print(next(angka))
# print(next(angka))
# print(next(angka))
# print(next(angka))

x = lambda a ,b : a * b

result = x(5,3)

# if result > 10:
#     print("besar dari 10")
# elif result > 10:
#     print("kurang dari 10")
# else:
#     print("sama dengan 10")

# if result > 10 : print("besar dari 10")
# print("lebih kecil dari 10") if result < 10 else print("sama dengan 10")

# i = 0
# while i < 100:
#     if i == 10:
#         print("sudah sampe angka 10")
#         break
#     i += 1


# fruits = ["apple","banana","mangga"]
# text = "ini kalimat"

# for fruit in text:
#     print(fruit)

# for index in range(8,10):
#     print(index)

# for index in range(0,10,2):
#     print(index)
# else:
#     print("beres cuy, edan ada else di for")

# def myfun(nama = "steven"):
#     print("hai ",nama)

# myfun("budi")

# def myfun(*name):
#     print("nama pertama",name[1])

# myfun("budi","joko","dodo")

# def myfun (*,nama,kelas):
#     print(nama)
#     print(kelas)

# myfun("budi","12")

# def myfun (nama,*,kelas,umur,alamat):
#     print(nama)
#     print(kelas)
#     print(umur)
#     print(alamat)

# myfun("budi",kelas="12",umur="12",alamat="jakarta")

# def myfun(**bebas):
#     print("hai nama kamu adalah,",bebas["nama"]," dan umur kamu adalah ",bebas["umur"])

# myfun(nama="budi",umur="12")