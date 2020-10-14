#Menghitung Tarif Sewa

tarif1= 200000
tarif2= 10000
jamMulai=6
jamSelesai=23
menitMulai=0
menitSelesai=50
lamaSewa= (jamSelesai - jamMulai) + int((menitSelesai - menitMulai)/60)
harga = (lamaSewa//12 * tarif1) + (lamaSewa%12 * tarif2)
print(harga)
