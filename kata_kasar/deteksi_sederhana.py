import re

# 🔒 Daftar pola regex (tidak menyimpan kata kasar secara eksplisit)
regex_patterns = [
    r"\banjing\b",
    r"\bkentut\b",
    r"\btolol\b",
    r"\bgoblok\b",
    r"\bkontol\b",
    r"\bmemek\b",
    r"\bbangsat\b",
    r"\basu\b",
    r"\bjancok\b",
    r"\bsial\b",
    r"\bbodoh\b"
]


def contains_offensive_pattern(text):
    text = text.lower()
    for pattern in regex_patterns:
        if re.search(pattern, text):
            return True
    return False


# 🔁 Program utama
print("\n🧼 Deteksi Kata Kasar (Versi Sederhana)")
print("Ketik 'exit' untuk keluar.")
print("---------------------------------------------")

while True:
    kalimat = input("Masukkan kalimat: ")

    if kalimat.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    if contains_offensive_pattern(kalimat):
        print("⚠️ Kalimat mengandung kata kasar.")
    else:
        print("✅ Kalimat aman.")
