from random import randint

x = randint(1, 100)

if x < 30:
    print("Rainny")
elif x < 60:
    print("Cloudy")
elif x < 100:
    print("Sunny")
else:
    print("...")