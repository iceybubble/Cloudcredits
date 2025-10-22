🔐 Enhanced Password Strength Tester

📁 Project Structure
```
Enhanced_Password_Tester/
│
├── password_tester.py          # Main program to test password strength
└── common_passwords.txt        # List of most common or breached passwords
```

🧠 Overview

Enhanced Password Strength Tester is a Python-based command-line tool designed to help users evaluate and improve their password security.

It checks a password against security best practices (length, complexity, and variety) and compares it with a list of commonly used or breached passwords.

It also provides color-coded feedback using the colorama library to make results easy to read.

⚙️ Features
```
✅ Checks password length, uppercase, lowercase, numbers, and special characters
✅ Detects weak or common passwords using a built-in wordlist
✅ Provides real-time, color-coded feedback (green = strong, yellow = moderate, red = weak)
✅ Gives clear recommendations to improve password strength
✅ Lightweight and easy to use — runs directly in the terminal
```

🧰 Requirements

You’ll need Python 3.7+ and the colorama library.

Install dependencies with:

```
pip install colorama
```

🚀 How to Run

1️⃣ Clone or download the project folder.
2️⃣ Make sure the file common_passwords.txt is in the same directory as password_tester.py.
3️⃣ Run the program:

```
python password_tester.py
```

💡 Example Run
```
=== ENHANCED PASSWORD STRENGTH TESTER ===
Enter a password to test: Password123!

Password Strength: Moderate

Suggestions to improve your password:
- Add at least one special character (!@#$%^&* etc).
```

```
Example 2 – Very Strong Password

Enter a password to test: My$ecureP@ssw0rd123

Password Strength: Very Strong
```

```
Example 3 – Weak Password

Enter a password to test: 123456

Password Strength: Weak

Suggestions to improve your password:
- Password should be at least 8 characters long.
- Add at least one uppercase letter.
- Add at least one lowercase letter.
- Add at least one special character (!@#$%^&* etc).
- This password is very common or breached. Use a more unique password.
```

🔍 How It Works

Loads Common Passwords:
Reads from common_passwords.txt (list of known weak/breached passwords).

Analyzes Strength:
Checks for:

Minimum 8 characters

Uppercase & lowercase letters

Digits

Special characters

Scores Password:
Each rule met increases the score. The tool labels your password as:
 Weak
 Moderate
 Very Strong

Displays Feedback:
Prints color-coded strength and helpful suggestions.

⚠️ Notes

If common_passwords.txt is missing, the program will skip the breach check and display a warning.

The tool is for educational and personal use only — do not use it to test or store real user passwords.

🧩 Technologies Used

```
Python 3

colorama — For colorized terminal output

re (Regular Expressions) — For pattern matching

File I/O — For reading common passwords list
```

📄 License

This project is open-source and released under the MIT License.
You’re free to use, modify, and distribute it with proper credit.

```
“A strong password is your first defense — make it count.”`
```