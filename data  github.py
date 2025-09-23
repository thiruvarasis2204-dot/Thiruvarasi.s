import re

password = input("Enter password: ").strip()
score = 0

if len(password) >= 8:
    score += 5
else:
    print("Too short (< 8 chars)")

if re.search(r"[A-Z]", password):
    score += 6
else:
    print("Missing uppercase")

if re.search(r"[a-z]", password):
    score += 6
else:
    print("Missing lowercase")

if re.search(r"\d", password):
    score += 2
else:
    print("Missing digit")

if re.search(r"\W", password):
    score += 2
else:
    print("Missing special character")

print("Final score:", score)

if score >= 15:
    strength = "Strong"
elif score >= 10:
    strength = "Medium"
else:
    strength = "Weak"

print("Strength:", strength)
