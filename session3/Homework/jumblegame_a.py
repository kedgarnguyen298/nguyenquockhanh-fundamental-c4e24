from random import shuffle

word_str = "huybeo"
word = list(word_str)

shuffle(word, random = None )

print(*word)

while True:
    ans = input("What is our lecture's name?: ")
    dapan = "huybeo"

    if ans == dapan:
        print("Hura")
        break
    else: 
        print("Try again :(")

