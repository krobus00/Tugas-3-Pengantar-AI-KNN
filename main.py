import pandas as pd
from Distance import Distance


def normalize(df, column, factor=10):
    result = df.copy()
    for col in column:
        max_value = df[col].max()
        min_value = df[col].min()
        result[col] = ((df[col] - min_value) / (max_value - min_value))*factor
    return result


def getResult(df, distanceResult):
    result = []
    for idx, val in enumerate(distanceResult):
        result.append([val, df['Nama Mobil'][idx]])
    result.sort(key=lambda x: x[0])
    no = 1
    for data in result[:3]:
        print('{}. {} {}'.format(no, data[1], round(data[0], 4)))
        no += 1
    return result[:3]


def saveData(allDistanceResult):
    col = ['Euclidean', 'Manhattan', 'Minkowski', 'Supremum']
    row = [[], [], []]
    for model in allDistanceResult:
        for i in range(3):
            row[i].append(model[i][1])
    pd.DataFrame(row, columns=col).to_excel(
        'rekomendasi.xls',
        engine='openpyxl',
        index=False
    )


df = pd.read_excel('./data/mobil.xls')

# normalize harga
df = normalize(df, ['Harga (Ratus Juta)'])
print("INPUT")
ukuran = float(input("ukuran: "))
kenyamanan = float(input("kenyamanan: "))
irit = float(input("irit: "))
kecepatan = float(input("kecepatan: "))
harga = float(input("harga: "))

col = ['Ukuran', 'Kenyamanan', 'Irit', 'Kecepatan',
       'Harga (Ratus Juta)']
val = [[ukuran, kenyamanan, irit, kecepatan, harga]]
dfTest = pd.DataFrame(val, columns=col)

d = Distance(df, dfTest)
result = d.getAllDistance()
print("RESULT")
val = []
for model in result:
    print("-"*17)
    print(model)
    val.append(getResult(df, result[model]))
    print("-"*17)
saveData(val)
