import random
from words import words
import string

def get_valid_word(words):
    word=random.choice(words)
    while "-" in word or " " in word:
        word=random.choice(words)
    return word.upper()
    
def hangman():
    random_word=get_valid_word(words)
    word_length=len(random_word)
    alphabets=string.ascii_uppercase # using imported strings
    current_word=["-"]*word_length
    characters_found=0
    lives=6
    used_letters=""
    print("\n Guess The Word And Win The Game")
    while lives>0 and characters_found<word_length:
        print(f"\nYou have {lives} lives and you have used these letters: {used_letters}")
        print("Current Word :" , " ".join(current_word))
        user_input=input("Guess A Letter: ").upper()
        if user_input in alphabets:
            if user_input in used_letters:
                print("\nYou have already tried this one, Try Something else!")
            elif user_input in random_word:
                for i in range(word_length):
                    if random_word[i]==user_input:
                        current_word[i]=user_input
                        characters_found+=1
                used_letters+=user_input+" "
            else:
                lives-=1
                used_letters+=user_input+" "
                print(f"your letter, {user_input} is not in the Word")
        else:
            print("please Provide a valid Alphabet !! ")
    if characters_found==word_length:
        return f"\nYou have guessed  '{random_word}' correctly\n"
    return f"\nYou Lose, The correct Word was {random_word}\n"
print(hangman())