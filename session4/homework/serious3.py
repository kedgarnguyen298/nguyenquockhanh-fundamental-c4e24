from random import randint

words = ["champion", "hexagon", "meticulous"]

# pick random:
n = randint(0,len(words) - 1)
word = words[n]
chs = list(word)

# shuffle random:
for _ in range(len(chs)):
    m = randint(0, len(chs) - 1)
    ch = chs[m]
    print(ch, end = " ")
    chs.pop(m)
print("")

#user guess:
while True:
    ans = input()
    if ans == word:
        print("Hura")
        break
    else:
        print("Try again")


