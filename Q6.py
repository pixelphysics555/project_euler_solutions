x = 0
for i in range(101):
    x += i ** 2

y = 0
z = 0
for i in range(101):
    z += i
    y = z ** 2

print(y - x)
