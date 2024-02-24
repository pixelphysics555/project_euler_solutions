fibonacci_numbers = [1, 2]

x = 2
while True:
    if x > 4000000: # Four million
        del fibonacci_numbers[-1]
        break
    else:
        x = fibonacci_numbers[-2] + fibonacci_numbers[-1]
        fibonacci_numbers.append(x)

print(fibonacci_numbers)

sum_of_even_terms = 0

# Only terms that are themselves even:
for i in range(len(fibonacci_numbers)):
    if fibonacci_numbers[i] % 2 == 0:
        sum_of_even_terms += fibonacci_numbers[i]

# If it wanted the even indexes:
'''
    if i % 2 == 1:
        sum_of_even_terms += fibonacci_numbers[i]
    if i % 2 == 0:
        sum_of_even_terms += 0
'''
print(sum_of_even_terms)
