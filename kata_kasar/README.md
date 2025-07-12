# 🧼 Deteksi Kata Kasar (Bahasa Indonesia)

Proyek Python ini mendeteksi kata-kata kasar dalam Bahasa Indonesia. Terdapat dua metode deteksi yang dapat digunakan:

- **🔎 Deteksi Sederhana** – cepat dan ringan tanpa AI
- **🤖 Deteksi dengan AI** – menggunakan model machine learning dari Hugging Face

---

## 📁 Struktur Folder

```
kata_kasar/
├── model/ # Folder model AI setelah inisialisasi (bisa gunakan Git LFS)
├── venv/ # Virtual environment Python
├── deteksi_sederhana.py # Deteksi kata kasar tanpa AI (regex)
├── deteksi_with_ai.py # Deteksi kata kasar menggunakan AI
├── init_model.py # Mengunduh dan menyimpan model dari Hugging Face
├── requirements.txt # Daftar dependensi
└── README.md # Dokumentasi proyek
```

---

```yaml

## 🔧 Persiapan Awal

### 1. Aktifkan Virtual Environment


# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

# 2. Install Dependensi

```bash
pip install -r requirements.txt
```

## ✅ Mode 1: Deteksi Sederhana (Tanpa AI)

Jalankan deteksi berbasis regex:

```bash
python deteksi_sederhana.py
# Atau untuk versi obfuscated
```

<!-- buat agar menjadi llist -->

Keunggulan:

- Tidak memerlukan model AI
- Cepat dan efisien
- Tidak memerlukan koneksi internet
- Cepat dan ringan
- Cocok untuk kebutuhan offline

## 🤖 Mode 2: Deteksi dengan AI

Langkah 1: Unduh Model AI
Sebelum menjalankan deteksi berbasis AI, download model dengan:

```bash
python init_model.py
# Model akan tersimpan ke folder ./model.
# Pastikan untuk menjalankan ini hanya sekali
```

Langkah 2: Jalankan Deteksi AI

```bash
python deteksi_with_ai.py
# Menggunakan model dari 🤗 Hugging Face
```

Keunggulan:

- Menggunakan model dari 🤗 Hugging Face
- Lebih fleksibel dalam mendeteksi kalimat kasar, termasuk yang tidak eksplisit

📝 Tips Tambahan
Ketik exit untuk keluar dari program saat diminta input.
