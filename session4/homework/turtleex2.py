from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for col in colors:
    color(col)
    begin_fill()
    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
    

mainloop()