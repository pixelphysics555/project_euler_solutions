# Pythagorean Triple where a + b + c = 1000
# a < b < c
# a ** 2 + b ** 2 = c ** 2
# Find a * b * c
import time
from numpy import sqrt, array, append

sq_list = array([i ** 2 for i in range(1000)])

try:
    start = time.time()
    for i in range(1, len(sq_list)):
        for j in range(i, len(sq_list)):
            for k in range(j, len(sq_list)):
                if sq_list[i] + sq_list[j] == sq_list[k]:
                    trip_array = sqrt(array([sq_list[i], \
                            sq_list[j], sq_list[k]]))
                    if sum(trip_array) == 1000.0:
                        print(f'Triple: {trip_array}')
                        abc = trip_array[0] * \
                                trip_array[1] * trip_array[2]
                        print(f'abc = {abc}')
                        raise StopIteration

except StopIteration:
    end = time.time()
    print(f'Took {round(end - start, 3)} seconds.')
