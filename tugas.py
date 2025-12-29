import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

print("Gaji sebelum kenaikan 5%")
print(df)
print("")

# Kenaikan 5%
increase_5_percent = lambda gaji: gaji * 1.05

for i in range(len(df)):
    df.at[i, 'Gaji'] = increase_5_percent(df.at[i, 'Gaji'])

print("Gaji sesudah kenaikan 5%")
print(df)
print("")

# Kenaikan tambahan 2% untuk yang usia diatas 30 tahun
increase_2_percent = lambda gaji: gaji * 1.02

for i in range(len(df)):
    if df.at[i, 'Usia'] > 30:
        df.at[i, 'Gaji'] = increase_2_percent(df.at[i, 'Gaji'])

print("Gaji tambahan untuk usia diatas 30 tahun")
print(df)
print("Perubahan gaji hanya terjadi pada Jane, karena umurnya diatas 30 tahun. Sedangkan Bob umurnya pas di 30 tahun")