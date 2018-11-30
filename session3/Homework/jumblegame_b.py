# Make color :D
# print("The game is: Guess words")
# print("-------------------------")
# print("Rule: You must guess a word which having mixed character")
# print("Don't worrry! You will be suggested by all of characters in that word")
# print("-------------------------")
# print("Let's get started !")
# print("--------------------------")

# Start coding:
from random import *

list_word = ["hello", "champion", "fighting"]

word_str = choice(list_word)
word = list(word_str)

shuffle(word, random = None)

print(*word)





