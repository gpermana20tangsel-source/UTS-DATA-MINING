import pandas as pd
import numpy as np

df_data = {
    'Nama': ['Andi', 'Budi', 'Caca', 'Dedi', 'Euis'],
    'Departemen': ['IT', 'HR', 'IT', 'Sales', 'Sales'],
    'Gaji': [8000000, 7000000, 8500000, np.nan, 6000000],
    'Pengalaman_Tahun': [5, 3, 6, 2, 1]
}

# Membuat DataFrame
df = pd.DataFrame(df_data)

# 1. Isi nilai NaN dengan median gaji
median_gaji = df['Gaji'].median()
df['Gaji'] = df['Gaji'].fillna(median_gaji)

# 2. Membuat kolom kategori senioritas
df['Kategori_Senioritas'] = np.where(
    df['Pengalaman_Tahun'] > 4,
    'Senior',
    'Junior'
)

# 3. Rata-rata gaji per departemen
rata_gaji = df.groupby('Departemen')['Gaji'].mean()

# Output
print("DataFrame:")
print(df)

print("\nRata-rata Gaji per Departemen:")
print(rata_gaji)