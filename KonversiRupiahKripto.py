import csv
#Nama : Renata Aura Syrga
#NIM : 24416255201264
#IF24C
# Struktur Data
kurs_kripto = {}  # HashMap
riwayat_konversi = []  # Stack

# Load data dari kurs_kripto.csv
def load_kurs():
    global kurs_kripto
    kurs_kripto.clear()
    try:
        with open("kurs_kripto.csv", mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                kode = row['kode']
                kurs_kripto[kode] = {
                    "nama": row['nama_koin'],
                    "nilai": float(row['nilai_per_rupiah'])
                }
    except FileNotFoundError:
        print("File kurs_kripto.csv tidak ditemukan. Membuat file baru...")
        with open("kurs_kripto.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["kode", "nama_koin", "nilai_per_rupiah"])

# Simpan kurs ke kurs_kripto.csv
def simpan_kurs():
    with open("kurs_kripto.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["kode", "nama_koin", "nilai_per_rupiah"])
        for kode, data in kurs_kripto.items():
            writer.writerow([kode, data["nama"], data["nilai"]])

# Tampilkan kurs saat ini
def tampilkan_kurs():
    print("\n--- Daftar Kurs Kripto ---")
    for kode, data in kurs_kripto.items():
        print(f"{kode} ({data['nama']}) = Rp {data['nilai']:.2f}")

# Tambah atau update kurs
def tambah_kurs():
    kode = input("Masukkan kode kripto (contoh: BTC): ").upper()
    nama = input("Masukkan nama koin: ")
    try:
        nilai = float(input("Masukkan nilai per Rupiah: "))
        kurs_kripto[kode] = {"nama": nama, "nilai": nilai}
        simpan_kurs()
        print(f"{kode} berhasil ditambahkan/diperbarui.")
    except ValueError:
        print("Input nilai tidak valid.")

# Konversi Rupiah ke kripto
def konversi():
    try:
        rupiah = float(input("Masukkan jumlah Rupiah: "))
        kode = input("Masukkan kode kripto (contoh: BTC): ").upper()
        if kode in kurs_kripto:
            nilai = kurs_kripto[kode]["nilai"]
            hasil = rupiah / nilai
            print(f"Hasil: Rp{rupiah:.2f} = {hasil:.8f} {kode}")
            riwayat_konversi.append(f"{rupiah} => {hasil:.8f} {kode}")
        else:
            print("Kode kripto tidak ditemukan.")
    except ValueError:
        print("Input tidak valid.")

# Lihat riwayat konversi
def lihat_riwayat():
    print("\n--- Riwayat Konversi ---")
    if not riwayat_konversi:
        print("Belum ada riwayat.")
    else:
        for item in reversed(riwayat_konversi):
            print(item)

# Menu Utama
def menu():
    load_kurs()
    while True:
        print("\n=== APLIKASI KONVERSI KRIPTO ===")
        print("1. Lihat Kurs Kripto")
        print("2. Konversi Rupiah ke Kripto")
        print("3. Tambah/Update Kurs")
        print("4. Lihat Riwayat Konversi")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kurs()
        elif pilihan == "2":
            konversi()
        elif pilihan == "3":
            tambah_kurs()
        elif pilihan == "4":
            lihat_riwayat()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
menu()
