from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "AptaArkana/indonesian_toxic_classification"

print("⬇️ Mengunduh dan menyimpan model ke folder './model'...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

tokenizer.save_pretrained("./model")
model.save_pretrained("./model")

print("✅ Model berhasil disimpan.")
print("🔄 Silakan jalankan kembali program deteksi kata kasar.")
