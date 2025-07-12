def int_to_roman(number):
    if not (0 < number < 4000):
        return "❌ Hanya mendukung angka 1 hingga 3999."

    angka_romawi = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    hasil = ''
    for nilai in angka_romawi:
        while number >= nilai:
            hasil += angka_romawi[nilai]
            number -= nilai

    return hasil


# 🔁 Program utama
print("🔢 Konversi Bilangan Bulat ke Romawi (1-3999)")
print("Ketik 'exit' untuk keluar.")
print("-----------------------------------------")

while True:
    user_input = input("Masukkan bilangan bulat: ")

    if user_input.lower() == "exit":
        print("🚪 Keluar dari program.")
        break

    if not user_input.isdigit():
        print("❌ Input harus berupa angka bulat.")
        continue

    angka = int(user_input)
    romawi = int_to_roman(angka)
    print(f"➡️ Romawi dari {angka} adalah: {romawi}")
