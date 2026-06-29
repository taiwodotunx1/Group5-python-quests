#!/usr/bin/python3

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number: "))

print("Correct!")