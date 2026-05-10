inventory = {
    "laptop": {"stok": 10, "harga": 15000000},
    "mouse": {"stok": 50, "harga": 250000},
    "monitor": {"stok": 20, "harga": 3000000}
}
# jawaban 
# 1. Tambah produk baru
inventory["keyboard"] = {"stok": 30, "harga": 500000}

# 2. Update harga laptop
inventory["laptop"].update({"harga": 14500000})

# 3. Hitung total aset gudang
total_aset = 0

for barang in inventory.values():
    total_aset += barang["stok"] * barang["harga"]

# Output
print("Data Inventory:")
print(inventory)

print("\nTotal nilai aset gudang:")
print(total_aset)