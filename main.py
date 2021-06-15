from Distance import Distance
import pandas as pd
from Distance import Distance


def getResult(l):
    li = []
    for i in range(len(l)):
        li.append([l[i], i])
    li.sort()
    sort_index = []

    for x in li:
        sort_index.append(x[1])
    return sort_index[:3]


df = pd.read_excel('./mobil.xls')

print("INPUT")
ukuran = float(input("ukuran: "))
kenyamanan = float(input("kenyamanan: "))
irit = float(input("irit: "))
kecepatan = float(input("kecepatan: "))
harga = float(input("harga: "))

test = {
    'Ukuran': ukuran,
    'Kenyamanan': kenyamanan,
    'Irit': irit,
    'Kecepatan': kecepatan,
    'Harga (Ratus Juta)': harga
}

d = Distance(df, test)
e = d.Euclidean()
ma = d.Manhattan()
mi = d.Minkowski()

print("Euclidean : ", getResult(e))
print("Manhattan : ", getResult(ma))
print("Minkowski : ", getResult(mi))
