flock_size = [5, 7, 300, 90, 24, 50, 75]

print("Hello, My name is Hiep and these are my sheeps size: ")
print(flock_size)

for i in range(3):
    print("MONTH", i + 1, ":")

    for i in range(len(flock_size)):
        flock_size[i] = int(flock_size[i]) + 50
    print("One month has passed, now here is my flock: ")
    print(flock_size)

    max_size = max(flock_size)
    print("Now my biggest sheep has size", max_size, "let share it")

    flock_size[flock_size.index(max_size)] = 8
    print("After shearing, here is my flock: ")
    print(flock_size)

s = sum(flock_size)
print("My flock in size total: ", s)
money = s * 2
print("I would get to: ", s, "* 2$ =", s * 2)

    