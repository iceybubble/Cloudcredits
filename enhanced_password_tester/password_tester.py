import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load common breached passwords
def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, "r") as f:
            return set(line.strip() for line in f.readlines())
    except FileNotFoundError:
        print(Fore.YELLOW + "Warning: common_passwords.txt not found. Skipping breach check.")
        return set()

def check_password_strength(password, common_passwords):
    score = 0
    recommendations = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        recommendations.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        recommendations.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        recommendations.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        recommendations.append("Add at least one number.")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        recommendations.append("Add at least one special character (!@#$%^&* etc).")

    # Breach check
    if password in common_passwords:
        recommendations.append("This password is very common or breached. Use a more unique password.")
        score = min(score, 2)

    # Strength label
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, recommendations

def print_colored_strength(strength):
    if strength == "Very Strong":
        print(Fore.GREEN + f"\nPassword Strength: {strength}")
    elif strength == "Moderate":
        print(Fore.YELLOW + f"\nPassword Strength: {strength}")
    else:
        print(Fore.RED + f"\nPassword Strength: {strength}")

def main():
    common_passwords = load_common_passwords()
    print(Fore.CYAN + "=== ENHANCED PASSWORD STRENGTH TESTER ===")
    password = input("Enter a password to test: ")

    strength, recommendations = check_password_strength(password, common_passwords)

    print_colored_strength(strength)

    if recommendations:
        print(Fore.CYAN + "\nSuggestions to improve your password:")
        for rec in recommendations:
            print(Fore.CYAN + "- " + rec)

if __name__ == "__main__":
    main()
