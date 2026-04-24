import string

def check_strength(password):
    score = 0
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
    if score >= 0 and score <= 2:
        return "Weak"
    elif score >= 3 and score <= 4:
        return "Medium"
    elif score == 5:
        return "Strong"

def main():
    password = input("Enter a password: ")
    score = check_strength(password)
    result = get_rating(score)
    print(f"Password is {result} and score is {score}")

if __name__ == "__main__":
    main()