import re
def password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special characters
    if re.search(r"[@$!%*?&#^()-_=+]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength
    if score == 5:
        strength = "Strong "
    elif score >= 3:
        strength = "Medium "
    else:
        strength = "Weak "

    return strength, feedback

password = input("Enter your password: ")
strength, tips = password_strength(password)
print(f"Password Strength: {strength}")
if tips:
    print("Suggestions:")
    for t in tips:
        print(f"- {t}")