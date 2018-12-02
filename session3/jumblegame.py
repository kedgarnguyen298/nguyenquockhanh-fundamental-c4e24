from random import randint

word = "hexagon"
characters = list(word)

for _ in range(len(characters)):
    n = randint(0, len(characters) - 1)
    ch = characters[n]
    print(ch, end = " ")    
    characters.pop(n)
    
# select character randomly
# print selected character
# remove selected character
        
