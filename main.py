from Distance import Distance
import pandas as pd
from Distance import Distance


def getTop3(l):
    li = []
    for i in range(len(l)):
        li.append([l[i], i])
    li.sort()
    sort_index = []
    for x in li:
        sort_index.append(x[1])
    return sort_index[:3]


def getResult(df, d):
    no = 1
    for i in getTop3(d):
        print('{}. {}'.format(no, df.iloc[i]['Nama Mobil'], d[i]))
        no += 1


df = pd.read_excel('./data/mobil.xls')

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
s = d.Supremum()

print("RESULT: ")
print("Euclidean : ")
getResult(df, e)
print("Manhattan : ")
getResult(df,  ma)
print("Minkowski : ")
getResult(df, mi)
print("Supremum : ")
getResult(df, s)
