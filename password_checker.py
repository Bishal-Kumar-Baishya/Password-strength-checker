import string
import re
import argparse

parser = argparse.ArgumentParser()

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
    
    try:
        with open(path, "r") as f:
            for line in f:
                password.append(line.strip())
        return password
    except FileNotFoundError:
        print(f"ERROR: {path} not found")
        return []

def get_feedback(password):
    feedback = []

    if len(password) < 8:
        feedback.append("Too short - use 8+ characters")
    if not any(char in string.ascii_uppercase for char in password):
        feedback.append("Missing uppercase letters")
    if not any(char in string.ascii_lowercase for char in password):
        feedback.append("Missing lowercase letters")
    if not any(char in string.digits for char in password):
        feedback.append("Missing digits")
    if not any(char in string.punctuation for char in password):
        feedback.append("Missing special characters")
    return feedback



def main():
    parser.add_argument("--password")
    args = parser.parse_args()
    
    if args.password is None:
        print("Error: please provide a password using --password")
        return
    
    cmnPassword = load_common_passwords("common_passwords.txt")
    score = check_strength(args.password, cmnPassword)

    if score == "common":
        print("Your password is very common, and is present in common password file\n")

    elif score == "repeated":
        print("Password has repeated characters - too weak")

    else:
        result = get_rating(score)
        print(f"Password is {result} and score is {score}")
        if result != "Strong":
            feedback = get_feedback(args.password)
            for msg in feedback:
                print(msg)

if __name__ == "__main__":
    main()