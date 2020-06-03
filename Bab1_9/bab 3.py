#Nama: Rivaldo Marta Dinata
#NBI : 1461900135
import numpy
print("menghitung standar devasi -std()")
nilai_mahasiswa =[80,87,76,88,86,81,63,49,62,93,97,75,55,86,90]
x= numpy.std(nilai_mahasiswa)
print("Std       : ",x)
x= numpy.mean(nilai_mahasiswa)
print('Rata-rata : ',x)
kesimpulan="terdapat 13 nilai yang mendekati nilai rata rat di dalam nilai tersebut"
print("Kesimpulan: ",kesimpulan)
print('')
print("Menghitung varience")
kecepatan = [32,111,138,28,59,77,97]
x=numpy.var(kecepatan)
print("varience: ",x)

