# sistem_rekomendasi.py

data_buku = {
    "AI for Beginners": {"AI", "ML", "Beginner"},
    "Deep Learning with Python": {"AI", "Deep Learning"},
    "Data Science Essentials": {"Data", "ML"},
    "AI and Ethics": {"AI", "Philosophy"},
}


def cari_semua_kemungkinan(input_judul):
    input_judul = input_judul.lower()
    return [judul for judul in data_buku if input_judul in judul.lower()]


def rekomendasi_buku(judul_input, jumlah_rekomendasi=3):
    if judul_input not in data_buku:
        print("📕 Judul buku tidak ditemukan.")
        return

    genre_input = data_buku[judul_input]
    hasil_kemiripan = []

    for judul, genre in data_buku.items():
        if judul == judul_input:
            continue
        similarity_score = len(genre_input & genre)
        hasil_kemiripan.append((judul, similarity_score))

    hasil_kemiripan.sort(key=lambda x: x[1], reverse=True)
    rekomendasi = hasil_kemiripan[:jumlah_rekomendasi]

    print(f"\n📚 Rekomendasi buku mirip dengan: {judul_input}")
    for idx, (judul, skor) in enumerate(rekomendasi, 1):
        print(f"{idx}. {judul} (Kemiripan: {skor})")
    print("--------------------------------------------")


# 🔁 Program utama
print("📖 Sistem Rekomendasi Buku Berdasarkan Genre")
print("Ketik 'exit' untuk keluar.")
print("--------------------------------------------")

while True:
    user_input = input("Masukkan judul buku: ")
    if user_input.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    cocok = cari_semua_kemungkinan(user_input)
    if len(cocok) == 0:
        print("📕 Tidak ada judul yang cocok ditemukan.")
    elif len(cocok) == 1:
        print(f"\n🔎 Mungkin maksud Anda: {cocok[0]}")
        rekomendasi_buku(cocok[0])
    else:
        print("\n🔎 Ditemukan beberapa judul yang cocok:")
        for i, judul in enumerate(cocok, 1):
            print(f"{i}. {judul}")

        try:
            pilihan = int(input("Pilih nomor buku yang dimaksud: "))
            if 1 <= pilihan <= len(cocok):
                rekomendasi_buku(cocok[pilihan - 1])
            else:
                print("❌ Pilihan tidak valid.")
        except ValueError:
            print("❌ Masukkan angka yang valid.")
