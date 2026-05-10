import numpy as np

scores = np.array([
    [80, 85, 90],
    [70, 60, 75],
    [95, 90, 100],
    [40, 50, 45]
])

# 1. Rata-rata setiap mahasiswa
rata_rata = np.mean(scores, axis=1)

# 2. Nilai tertinggi
nilai_tertinggi = np.max(scores)

# 3. Status lulus atau gagal
status = np.where(rata_rata >= 70, "Lulus", "Gagal")

# Output
print("Rata-rata mahasiswa:")
print(rata_rata)

print("\nNilai tertinggi:")
print(nilai_tertinggi)

print("\nStatus mahasiswa:")
print(status)