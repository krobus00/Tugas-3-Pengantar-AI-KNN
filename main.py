import pandas as pd
from Distance import Distance


def normalize(df, column, factor=10):
    result = df.copy()
    for col in column:
        max_value = df[col].max()
        min_value = df[col].min()
        result[col] = ((df[col] - min_value) / (max_value - min_value))*factor
    return result


def getResult(df, distanceResult, k):
    result = []
    for idx, val in enumerate(distanceResult):
        result.append([val, df['Nama Mobil'][idx]])
    result.sort(key=lambda x: x[0])
    no = 1
    for data in result[:k]:
        print('{}. {} {}'.format(no, data[1], round(data[0], 4)))
        no += 1
    return result[:k]


def saveData(result, model):
    row = []
    for car in result:
        row.append(car[1])
    pd.DataFrame(row, columns=['Rekomendasi']).to_excel(
        'rekomendasi_{}.xls'.format(model),
        engine='openpyxl',
        index=False
    )


df = pd.read_excel('./data/mobil.xls')
# normalisasi seluruh data
df = normalize(df, df.columns.values[1:])

print("INPUT")
ukuran = float(input("ukuran: "))
kenyamanan = float(input("kenyamanan: "))
irit = float(input("irit: "))
kecepatan = float(input("kecepatan: "))
harga = float(input("harga: "))

# membuat data test
col = ['Ukuran', 'Kenyamanan', 'Irit', 'Kecepatan',
       'Harga (Ratus Juta)']
val = [[ukuran, kenyamanan, irit, kecepatan, harga]]
dfTest = pd.DataFrame(val, columns=col)

# mengambil hasil pemrosesan data
d = Distance(df, dfTest)
result = d.getAllDistance()

print("RESULT")
# Menampilkan hasil dari setiap model distance
for model in result:
    print("-"*17)
    print(model)
    print("-"*17)
    best = getResult(df, result[model], 3)
    saveData(best, model)
