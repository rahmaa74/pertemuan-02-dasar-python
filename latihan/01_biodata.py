tahun_sekarang = 2026
nama = input("nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

umur = tahun_sekarang - tahun_lahir

print()
print("KARTU BIODATA")
print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {umur} tahun")