# Clipboard Hidden Character Cleaner

A lightweight Python tool that monitors your clipboard in real-time and
automatically removes hidden Unicode characters.\
This is extremely useful when copying text containing invisible
characters such as: - Zero Width Non-Joiner (`U+200C`) - Zero Width
Joiner (`U+200D`) - Zero Width No-Break Space (`U+FEFF`) - Any other
characters you define in `characters.txt`

------------------------------------------------------------------------

## 🚀 Features

-   Real-time clipboard monitoring\
-   Automatically removes hidden / invisible Unicode characters\
-   Cleans text and replaces the clipboard instantly\
-   Customizable character list\
-   Simple, fast, cross-platform\
-   Only one small dependency (`pyperclip`)

------------------------------------------------------------------------

## 📦 Installation

Clone the repository and install requirements:

``` bash
git clone https://github.com/your-username/clipboard-cleaner.git
cd clipboard-cleaner
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Running the Script

``` bash
python main.py
```

After running, the script will continuously watch your clipboard.\
Whenever you copy any text, it will:

1.  Detect if hidden characters exist\
2.  Remove all characters listed in `characters.txt`\
3.  Replace your clipboard content with the cleaned version

------------------------------------------------------------------------

## 📝 Customizing Hidden Characters

All characters you want to remove should be placed inside:

    characters.txt

You may add them:

-   Line-by-line\
-   Or next to each other without line breaks

Both formats are supported.

### Example `characters.txt`:

Invisible characters (actual characters, not escaped):

    ‌
    ‍
    ﻿

------------------------------------------------------------------------

## 📂 Project Structure

    clipboard-cleaner/
    │
    ├─ main.py
    ├─ characters.txt
    ├─ requirements.txt
    ├─ .gitignore
    └─ README.md

------------------------------------------------------------------------

## 📘 Requirements

    pyperclip

------------------------------------------------------------------------

## ❗ Notes

-   The script runs in an infinite loop by design\
-   Uses a small delay (`0.1s`) to reduce CPU usage\
-   Works on Windows, Linux, and macOS\
-   If running on Linux, you may need `xclip` or `xsel` installed

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------

## ✨ Author

Your Name\
GitHub: https://github.com/your-username
