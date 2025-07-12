def classify_emotion(sentence):
    sentence = sentence.lower()

    positive_keywords = ["senang", "gembira", "bahagia"]
    angry_keywords = ["marah", "kesal", "jengkel"]
    sad_keywords = ["sedih", "kecewa", "menangis"]

    if any(word in sentence for word in positive_keywords):
        return "Positive"
    elif any(word in sentence for word in angry_keywords):
        return "Angry"
    elif any(word in sentence for word in sad_keywords):
        return "Sad"
    else:
        return "Neutral"


print("💬 Klasifikasi Emosi Berdasarkan Kalimat")
print("Ketik 'exit' untuk keluar.")
print("---------------------------------------")

while True:
    sentence = input("Masukkan kalimat: ")
    if sentence.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    emotion = classify_emotion(sentence)
    print(f"🔍 Emosi terdeteksi: {emotion}")
