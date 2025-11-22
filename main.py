import time
import pyperclip
import os

current_path = os.path.dirname(os.path.realpath(__file__))

# خواندن کاراکترهای مخفی از فایل
with open(os.path.join(current_path, "characters.txt"), "r", encoding="utf-8") as f:
    raw = f.read()
    # اگر کاراکترها پشت سر هم باشند → همه را جدا می‌کنیم
    # اگر خط‌به‌خط باشند → splitlines هم می‌گیرد
    hidden_chars = list(raw.replace("\n", "")) + [c for c in raw.splitlines()]

# حذف موارد خالی یا تکراری
hidden_chars = list(set([c for c in hidden_chars if c.strip() == "" or len(c) == 1]))

recent_value = ""

while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value

        cleaned = recent_value
        for hc in hidden_chars:
            cleaned = cleaned.replace(hc, "")

        pyperclip.copy(cleaned)
        print("Cleaned:", cleaned[:50])

    time.sleep(0.1)
