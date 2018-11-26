#Khánh

from turtle import *
import math 

#Thân nhà

color("black")

fillcolor("yellow")
begin_fill()

for i in range(4):
    right(90)
    forward(200)

end_fill()

#mái nhà
fillcolor("red")
begin_fill()

left(150)
forward(100 / ((1/2)*(3**(1/2))))
left(60)
forward(100 / ((1/2)*(3**(1/2))))

end_fill()



mainloop()