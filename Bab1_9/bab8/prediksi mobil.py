#Nama: Rivaldo Marta Dinata
#NBI : 1461900135
from scipy import stats
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]
slope, intercept,r ,p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept
speed= myfunc(12)
print("Prediksi Kecepatan mobil umur 12 thn: ",speed)
speed2= myfunc(22)
print("Prediksi Kecepatan mobil umur 22 thn: ",speed2)

