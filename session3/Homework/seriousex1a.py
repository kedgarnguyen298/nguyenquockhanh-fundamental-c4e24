odd = range(1,16,2)

print("15 first odd positive numbers:", *odd)
print("------------------------------------")

for i in odd:
    print("Square of ", i, ": ", i ** 2)

print("------------------------------------")
print("End")