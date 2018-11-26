a = int(input("a = ? "))
b = int(input("b = ? "))
c = int(input("c = ? "))

n = b**2 - 4*a*c

if n < 0:
    print("No solutions ")
elif n == 0:
    print("Only 1 solution: ", "x = ", -b/(2*a))
else:
    
    delta_2 = n**0.5
    x1 = (-b + delta_2) / (a*2)
    x2 = (-b - delta_2) / (a*2)
    print("2 solutions: ", x1, x2)
    