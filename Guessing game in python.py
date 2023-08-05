#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def guess_number():
    # Generate a random number between 1 and 1000
    secret_number = random.randint(1, 1000)

    attempts = 0
    while True:
        #player's guess
        try:
            guess = int(input("Guess a number between 1 and 1000: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Very low. Try again.")
        else:
            print("Very high. Try again.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    guess_number()



# In[ ]:




