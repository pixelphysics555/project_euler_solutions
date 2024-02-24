multiples_of_3_or_5 = []

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples_of_3_or_5.append(i)

multiples_of_3_or_5.remove(0)
#print(multiples_of_3_or_5)

total = 0
for x in range(len(multiples_of_3_or_5)):
    total += multiples_of_3_or_5[x]

print(total)
