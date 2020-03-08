# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest
import os
import random

import Prob2

def numcheck(num, ans, tol=0.02):
    return (ans*(1-tol) < num < ans*(1+tol))

class Test_Prob1:
    def test_pdf_present(self):
        assert any(f.endswith('.pdf') for f in os.listdir('.'))


class Test_Prob2:
    # ep = 0.001
    def report(self,args):
        return f"\nProgram fails to get the correct value with parameters of {args}."

    def test_get_word_score(self):
        args = {("",7):0,
                ("it",7):2,
                ("was",7):54,
                ("weed",6):176,
                ("scored",7):351,
                ("WaYbILl",7):735,
                ("Outgnaw",7):539,
                ("fork",7):209,
                ("FORK",4):308,
                }
        for (word,n) in args.keys():
            student = Prob2.get_word_score(word,n)
            assert student == args[(word,n)], self.report((word,n))


    def test_update_hand(self):
        hands = (
                ['a','q','l','l','m','u','i'],
                ['e','v','v','n','i','l','l'],
                ['h','e','l','l','o'],
                )
        words = ('quail', 'Evil', 'HELLO')
        sols = (
                ['l','m'],
                ['v','n','l'],
                [],
                )
        for (hand,word,sol) in zip(hands,words,sols):
            handcopy = hand.copy()
            newhand = Prob2.update_hand(hand,word)
            assert handcopy == hand, "\nThe implementation of update_hand mutated the original hand!"
            assert newhand == sol, f"\nThe correct letters are not remaining with parameters {(hand, word)}."


    def test_is_valid_word(self):
        word_list = Prob2.load_words()
        words = ('hello', 'Rapture', 'honey','EVIL', 'Even')
        hands = (
                list('hello'),
                list('raaappetu'),
                list('nhoydwee'),
                list('evvnill'),
                list('evvnill'),
                )
        sols = (True,False,True,True,False)

        for word,hand,sol in zip(words,hands,sols):
            handcopy=hand.copy()
            student = Prob2.is_valid_word(word,hand,word_list)

            assert student == sol, f'\nExpected {sol}, but got {student} for word: {word} and hand: {hand}'
            assert hand == handcopy, 'Testing {word} for a second time. At this point hand should be {handcopy} but it is {hand}.'


    def test_display_hand(self, capsys):
        hands = ( 
                list('hello'),
                list('raaappetu'),
                list('nhoydwee'),
                list('evvnill'),
                )
        sols = (
                'h e l l o',
                'r a a a p p e t u',
                'n h o y d w e e',
                'e v v n i l l',
                )
        for hand,sol in zip(hands,sols):
            Prob2.display_hand(hand)
            cap = capsys.readouterr()
            cap = cap.out.rstrip()
            assert cap == sol, 'display_hand is not outputting the proper format. Make sure you have a space between characters and nothing else is being printed.'


    def test_play_hand(self):
        word_list = Prob2.load_words()

        hands = (
                list('rraaappetu'),
                list('nhoydwee'),
                )
        inputs = (
                ['rapture','aa','!!'],
                ['honey', 'wed'],
                )
        sols = (382,433)
        for hand,input_,sol in zip(hands,inputs,sols):
            with mock.patch('builtins.input', side_effect=input_):
                student = Prob2.play_hand(hand,word_list)
                assert student == sol, f'\nAn incorrect total hand score of {student} was returned with the hand: {hand} and the guessed words: {input_}. Score should have been {sol}.'



    def test_play_game(self):
        word_list = Prob2.load_words()

        seeds = (123,456)
        inputs= (
                  ['2','car','fail','wink','he','!!'],
                  ['3','zoo','coy','!!','goal','cog','rum','up','za']
                )
        sols = (505,704)
        for seed,input_,sol in zip(seeds,inputs,sols):
            with mock.patch('builtins.input', side_effect=input_):
                random.seed(seed)
                student = Prob2.play_game(word_list)
                assert student == sol, f'Did not get final expected score of {sol} at the end of {input_[0]} rounds. Instead got {student}.'






