# Jalankan file init model terlebih dahulu sebelum menjalankan file ini.
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import re

# 🔽 Load model dari folder lokal
tokenizer = AutoTokenizer.from_pretrained("./model")
model = AutoModelForSequenceClassification.from_pretrained("./model")

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

# 💬 Daftar pola regex kata kasar (tanpa eksplisit menuliskan)
obfuscated_patterns = [
    r"\ba.{1,2}j.{1,2}g\b",     # anjing
    r"\bk.{1,3}t.{1,3}l\b",     # kontol
    r"\bm.{1,2}m.{1,2}k\b",     # memek
    r"\bb.{1,3}g.{1,3}t\b",     # bangsat
    r"\bt.{1,3}l.{1,3}l\b",     # tolol
    r"\bg.{1,3}b.{1,3}k\b",     # goblok
    r"\ba.{1,2}s.{1,2}u\b",     # asu
    r"\bj.{1,2}n.{1,2}k\b",     # jancok
    r"\bsial\b",                # sial
    r"\bbodoh\b",               # bodoh
]
extra_offensive_patterns = [
    r"bapak kau",
    r"kau.*?(cacat|jelek|buntung|mati)",
    r"(cacat|jelek|buntung).*?kau",
]


def contains_offensive_pattern(text):
    text = text.lower()
    for pattern in obfuscated_patterns + extra_offensive_patterns:
        if re.search(pattern, text):
            return True
    return False


# 🧠 Program utama
print("\n🧠 Deteksi Kalimat Kasar (AI Lokal + Words Bad Manually)")
print("Ketik 'exit' untuk keluar.")
print("---------------------------------------------")

while True:
    kalimat = input("Masukkan kalimat: ")

    if kalimat.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    # AI classifier (toxic or not)
    result = classifier(kalimat)[0]
    label = result["label"]
    score = result["score"]

    # Regex pattern match
    is_obfuscated = contains_offensive_pattern(kalimat)

    if (label in ["Konten_kasar", "toxic"] and score >= 0.7) or is_obfuscated:
        print(
            f"⚠️ Kalimat mengandung kata kasar. (AI: {label} | Skor: {score:.2f})")
    else:
        print(f"✅ Kalimat aman. (AI: {label} | Skor: {score:.2f})")
