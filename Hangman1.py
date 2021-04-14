# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:43:23 2020

@author: SAMRUDDHI
"""
import random
import string

p = int(input("Choose language of secret word : 1. English 2. German: "))
if p==1:
    WORDLIST_FILENAME = "words.txt"
else:  
    WORDLIST_FILENAME = "german_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
def is_word_guessed(secret_word, letters_guessed):
    list1 = []
    list1[:0]=secret_word
    cnt = 0

    for s in list1:
        if s in letters_guessed:
            #print(s)
            cnt+=1

    return(cnt == len(list1) )
def get_guessed_word(secret_word, letters_guessed):
    list1 = []
    str = ''
    list1[:0]=secret_word

    for s in list1:
        if s in letters_guessed:
            #print(s)
            str = str + s
        else:
            #print('Wrong guess')
            str = str + '_ '
    return(str)
def get_available_letters(letters_guessed):
    list1 = []
    list1[:0] = string.ascii_lowercase
    str = ''
    print("\nLetters not guessed: ")

    for i in list1:
        if i not in letters_guessed:
            str = str + i
    return(str)   
def hangman(secret_word):
    
    guess = 7
    letters_guessed = ['a','e','i','o','u']
    
    #intro...
    print("\nWELCOME TO HANGMAN\n")
    name = input("Please enter username: ")
    print("Hello",name,"!\n")
    print("Vowels in the word will be displayed! So do not waste guesses on vowels...\n")
    print("I am thinking of a word that is ",len(secret_word),"letters long.")
    print(" --------------- \n")
    print("Letters not guessed: " ,string.ascii_lowercase)
    str = get_guessed_word(secret_word, letters_guessed)
    print(str)
    
    for i in range (0,8):
        #str1 = get_available_letters(letters_guessed)
        letters_guessed.append(input("Enter guess: "))
        str = get_guessed_word(secret_word, letters_guessed)
        print(str)
        bool = is_word_guessed(secret_word, letters_guessed)
        if bool is True:
            print("Word is guessed, YOU WON!!! ")
            print(name, "has guessed the secret word in ",guess," guesses! ")
            break
        else:
            print("Word has not been yet guessed")
            str1 = get_available_letters(letters_guessed)
            print(str1)
        print("\nYou have ", guess," guesses left")
        n = input("Do you want to guess the word? yes/no: ")
        if n == 'yes':
            n1 = input("What is it?")
            if n1 == secret_word:
                print("YES!",name,"You have WON!!!")
                break
            else:
                print("Nope! Wrong guess...")
        guess = guess - 1
    if guess == 1:
        print("\nUhoh, Sorry ",name," you LOST :( ")
    print("The secret word is ", secret_word.upper(),"!")
        

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    #secret_word = "apple"
    hangman(secret_word)