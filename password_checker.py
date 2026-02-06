import re

def check_length(password):
    return len(password) >= 8

def check_uppercase(password):
    return bool(re.search(r"[A-Z]", password))

def check_lowercase(password):
    return bool(re.search(r"[a-z]", password))

def check_digit(password):
    return bool(re.search(r"[0-9]", password))

def check_special_char(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

def calculate_strength(password):
    score = 0

    if check_length(password):
        score += 1
    if check_uppercase(password):
        score += 1
    if check_lowercase(password):
        score += 1
    if check_digit(password):
        score += 1
    if check_special_char(password):
        score += 1

    return score

def strength_feedback(score):
    if score <= 2:
        return "Heikko ❌"
    elif score == 3:
        return "Kohtalainen ⚠️"
    elif score == 4:
        return "Hyvä ✅"
    else:
        return "Erittäin vahva 🔐🔥"

def detailed_feedback(password):
    print("\nTarkistuksen tulokset:")
    print("- Pituus (väh. 8):", "OK" if check_length(password) else "PUUTTUU")
    print("- Iso kirjain:", "OK" if check_uppercase(password) else "PUUTTUU")
    print("- Pieni kirjain:", "OK" if check_lowercase(password) else "PUUTTUU")
    print("- Numero:", "OK" if check_digit(password) else "PUUTTUU")
    print("- Erikoismerkki:", "OK" if check_special_char(password) else "PUUTTUU")

def main():
    print("🔐 Password Strength Checker 🔐")
    password = input("Syötä salasana: ")

    score = calculate_strength(password)
    feedback = strength_feedback(score)

    print("\nSalasanan vahvuus:", feedback)
    detailed_feedback(password)
    print(f"\nPisteet: {score}/5")

if __name__ == "__main__":
    main()
