def is_palindrome(text):
    # Hilangkan spasi dan ubah ke huruf kecil
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]


print("🔁 Pengecek Palindrom")
print("Ketik 'exit' untuk keluar.")
print("---------------------------")

while True:
    user_input = input("Masukkan kata atau kalimat: ")

    if user_input.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    if is_palindrome(user_input):
        print("✅ Ini adalah palindrom!")
    else:
        print("❌ Bukan palindrom.")
