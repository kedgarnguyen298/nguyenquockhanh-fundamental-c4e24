from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

i = 3
while i < 8:
    for col in colors:
        color(col)
        for j in range(i):
            forward(100)
            left(360 / i)
        i += 1
    
mainloop()
