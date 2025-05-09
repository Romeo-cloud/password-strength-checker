def password_checker(pwd):
    score = 0

    if len(pwd) >= 8:
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?/~" for c in pwd):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Moderate"
    else:
        return "Strong"

# usage
user_input = input("Enter a password: ")
print("Strength:", password_checker(user_input))
