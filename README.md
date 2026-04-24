# Password Strength Checker
A Password strength checker is made with python

## How to run
python password_checker.py

## About the tool
- v1: This tool gets a input from user to enter a password. Based on that input password, it checks whether it contains uppercase letters, lowercase letters, digits, and symbols. It then gives a score based on the password out of 5 by specifying the password with Weak, Medium and Strong.
- v2: Added common password check against a wordlist file, and repeated character detection using regex.

## Scoring Criteria
- Length 8+ characters — +1
- Contains uppercase letter — +1
- Contains lowercase letter — +1
- Contains digit — +1
- Contains special character — +1
- Common passwords and repeated characters result in automatic weak rating

Score <= 2: Weak | Score 3-4: Medium | Score 5: Strong

## Built with
- Python 3
- string module
- re module

## Purpose
Everyday passwords are cracked using dictionary attacks, brute force attacks for very simple passwords. So this tool checks the passwords by giving score and specifying as "Weak/Medium/Strong" so that it can't easily be cracked.  