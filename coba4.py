#SOAL NOMOR 4
jarakAB= 125
jarakBC= 256
kecAB= 62
kecBC= 70
jamBerangkat=6
menitIstirahat=45
menitBerangkat=0

waktuPerjalanan = int(((jarakAB/kecAB)+(jarakBC/kecBC))*60)+(menitIstirahat)
print(round(waktuPerjalanan/60, 2) + jamBerangkat)
