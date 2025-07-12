import re

try:
    import keyboard  # untuk deteksi ESC di laptop
    ESC_SUPPORT = True
except ImportError:
    ESC_SUPPORT = False


def is_valid_password(password):
    if len(password) < 10:
        print("❌ Password minimal harus 10 karakter.")
        return False

    if re.search(r"[\'\"\(\)]", password):
        print("❌ Password tidak boleh mengandung simbol: ' \" ( )")
        return False

    if not re.search(r"[A-Z]", password):
        print("❌ Password harus mengandung huruf besar.")
        return False

    if not re.search(r"[a-z]", password):
        print("❌ Password harus mengandung huruf kecil.")
        return False

    if not re.search(r"[^A-Za-z0-9]", password):
        print("❌ Password harus mengandung setidaknya satu karakter spesial (selain huruf/angka).")
        return False

    print("✅ Password valid.")
    return True


print("🔐 Validasi Password (Ketik 'exit' untuk keluar jika tidak bisa tekan ESC)")
print("------------------------------------------------------")

while True:
    if ESC_SUPPORT and keyboard.is_pressed('esc'):
        print("\n🚪 ESC ditekan. Program keluar.")
        break

    password = input("Masukkan password: ")

    if password.lower() == "exit":
        print("🚪 'exit' diketik. Program keluar.")
        break

    is_valid_password(password)
