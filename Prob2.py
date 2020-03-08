##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import math
import random

# Variables that all functions should have
# access to (but which they will not alter)
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
LETTER_VALUES = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,  'f': 4,
        'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5,  'l': 1,
        'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
        's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4,  'x': 8,
        'y': 4, 'z': 10
        }
WORDLIST_FILENAME = "words.txt"



def load_words():
    """
    Returns a list of valid words, where all words are
    strings of lowercase characters.

    YOU DO NOT NEED TO TOUCH THIS FUNCTION!

    Outputs:
        - (list of strings): list of lowercase valid words
    """
    print('Loading valid word list from file...')
    f = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in f:
        wordlist.append(line.strip().lower())
    print('...', len(wordlist), 'words loaded.')
    return wordlist


def get_word_score(word, n):
    """
    Function which returns the overall score of the word. Assumes
    that the word is a valid word and is always a string of letters
    or an empty string. Does NOT assume that the string will only
    contain lowercase letters, so make sure that is accounted for.

    The score is the product of two components:
        * The sum of the points for the letters in the word
        * The larger of 1 or 7*(word length) - 3 * (n - word length)
    Individual letters are scored as in Scrabble.

    Inputs:
        - word (str): submitted word. Can contain uppercase characters
        - n (int): number of letters in hand that word was formed from

    Outputs:
        - (int): total score of word

    Usage:
        >>> get_word_score('weed', 6)
        176
        >>> get_word_score('fly', 7)
        81
    """
    pass # <-- delete when you add your code below




def display_hand(hand):
    """
    Prints out the individual letters in the hand in a more
    human readable format than simply printing the list.
    Individual characters should be printed out separated by
    a single space.

    Input:
        - hand (list of strings): hand of individual letters 
                to be displayed.
    Output:
        - Nothing returned
        - Prints characters to the screen directly

    Usage:
        >>> display_hand(['a','c','i','b','s'])
        a c i b s
    """
    pass # <-- delete when you add your code below




def deal_hand(n):
    """
    Function to randomly distribute letters to a hand of n
    letters. Approximately 1/3 of the letters in the hand
    are guaranteed to be vowels, and the rest consonants.

    YOU DO NOT NEED TO TOUCH THIS FUNCTION!

    Input:
        - n (int): Size of desired hand (number of letters)
    Output:
        - (list of strings): list of length n of individual
                characters.
    """
    hand = []
    num_vowels = int(math.ceil(n/3))

    for _ in range(num_vowels):
        hand.append(random.choice(VOWELS))
    for _ in range(num_vowels, n):
        hand.append(random.choice(CONSONANTS))
    random.shuffle(hand)
    return hand


def update_hand(hand, word):
    """
    Function to return a new hand, lacking any letters that
    were used up by the latest guessed word.

    Should NOT assume that the hand contains every letter in
    the word, or the same number of letters as were input for
    the word. A separate function checks for the validity of
    the word. Here simply return a new hand that is missing any
    letters that were contained within the word.

    The function SHOULD NOT MODIFY THE ORIGINAL HAND. It returns a
    NEW object which is the hand without the guessed characters.

    Inputs:
        - hand (list of strings): list of the current letters in hand
        - word (string): the guessed word
    Outputs:
        - (list of strings): a new hand which has had any letters in
                word subtracted out from it (if they were present in
                the first place)

    Usage:
        >>> update_hand(['a', 'x', 'e', 't', 'g'], 'axe')
        ['t', 'g']
        >>> update_hand(['a', 'x', 'e', 't', 'g'], 'axis')
        ['e', 't', 'g']
    """
    pass # <-- delete when you add your code below




def is_valid_word(word, hand, word_list):
    """
    Function to check if a word is both present in the valid
    word list AND if all letters necessary for the word are
    present in the hand. Should return True if both conditions
    are satisfied, False otherwise. Makes no assumptions about
    any capitalization in the submitted word.

    Inputs:
        - word (string): the guessed word
        - hand (list of str): the hand of characters
        - word_list (list of str): a list of all valid words
    Outputs:
        - (bool): True if word is in word_list and all letters in
                hand, otherwise False

    Usage:
        >>> is_valid_word('Axe', ['a', 'x', 'e', 't'], word_list)
        True
        >>> is_valid_word('axes', ['a', 'x', 'e', 't'], word_list)
        False
        >>> is_valid_word('xeT', ['a', 'x', 'e', 't'], word_list)
        False
        >>> is_valid_word('teat', ['a', 'x', 'e', 't'], word_list)
        False
    """
    pass # <-- delete when you add your code below




def play_hand(hand, word_list):
    """
    Allows a user to play a given hand, as follows:
        * The hand is displayed
        * The user can input a word
        * When any word is entered (valid OR invalid), the letters
          are used up from the hand
        * An invalid word results in no points, and a message is
          displayed to the user explaining and asking for another
          word
        * After every valid word, the score for that word is displayed
          as well as the total score for the hand. Remaining letters
          are also displayed and the user asked for another word.
        * The sum of all the word scores is displayed when the hand finishes
        * The hand finishes when there are either no more letters to guess or
          when the user inputs the string '!!' indicating they are giving up.
          Do NOT stop the hand when only a single character is left, only when
          0 letters are left or '!!' is entered.

    Inputs:
        - hand (list of str): current hand of characters
        - word_list (list of str): list of all valid words
    Outputs:
        - (int): the total score for the hand
    """
    pass # <-- delete when you add your code below




def play_game(word_list):
    """
    Allows the user to play a series of hands and outputs an overall score
    upon completion. Should
        * Ask the user to input the desired total number of hands to play
        * Accumulate an overall score over all hands to be output to the user
          upon completion

    Inputs:
        - word_list (list of str): list of all valid words
    Outputs:
        - (int) overall score summed across all desired hands
    """
    pass # <-- delete when you add your code below




# Runs the game when you launch the program
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
