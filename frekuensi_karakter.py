from collections import Counter

print("📊 Program Frekuensi Karakter dari Nama")
print("Masukkan nama lengkap Bapak/Ibu Anda (contoh: Budi Santoso)")
print("Ketik 'exit' untuk keluar.")
print("-----------------------------------------")

while True:
    nama = input("Masukkan nama: ")

    if nama.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    # Hitung frekuensi karakter
    frekuensi = Counter(nama)

    print("\n📈 Frekuensi karakter yang muncul:")
    for huruf, jumlah in frekuensi.items():
        if huruf == " ":
            print(f"Spasi : {jumlah}x")
        else:
            print(f"{huruf} : {jumlah}x")
    print("-----------------------------------------")
    print("🔄 Silakan masukkan nama lain atau ketik 'exit' untuk keluar.")
