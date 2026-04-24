import string
import re

def check_strength(password, common_password):
    score = 0
    if password in common_password:
        return "common"
    if re.search(r"(.)\1\1", password):
        return "repeated"
    if len(password) >= 8:
        score += 1
    if any(char in string.ascii_uppercase for char in password):
        score += 1
    if any(char in string.ascii_lowercase for char in password):
        score += 1
    if any(char in string.digits for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    return score


def get_rating(score):
    if score <= 2:
        return "Weak"
    elif score >= 3 and score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"
    
def load_common_passwords(path):
    password = []
    with open(path, "r") as f:
        for line in f:
            password.append(line.strip())
    return password


def main():
    password = input("Enter a password: ")
    cmnPassword = load_common_passwords("common_passwords.txt")
    score = check_strength(password, cmnPassword)
    if score == "common":
        print("Your password is very common, and is present in common password file\n")
    elif score == "repeated":
        print("Password has repeated characters - too weak")
    else:
        result = get_rating(score)
        print(f"Password is {result} and score is {score}")

if __name__ == "__main__":
    main()