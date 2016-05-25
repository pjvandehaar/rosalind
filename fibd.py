#!/usr/bin/env python3

# rabbits are babies once.


def get_num_final_rabbits(num_months, lifespan):
    num_rabbits_of_age = [0] * lifespan
    num_rabbits_of_age[0] = 1
    for month in range(1, num_months):
        num_new_babies = sum(num_rabbits_of_age[1:])
        num_rabbits_of_age = [num_new_babies] + num_rabbits_of_age[:-1]
    return sum(num_rabbits_of_age)


assert get_num_final_rabbits(1, 3) == 1
assert get_num_final_rabbits(2, 3) == 1
assert get_num_final_rabbits(3, 3) == 2
assert get_num_final_rabbits(4, 3) == 2
assert get_num_final_rabbits(5, 3) == 3
assert get_num_final_rabbits(6, 3) == 4

assert get_num_final_rabbits(1, 9) == 1 # fibonacci sequence
assert get_num_final_rabbits(2, 9) == 1
assert get_num_final_rabbits(3, 9) == 2
assert get_num_final_rabbits(4, 9) == 3
assert get_num_final_rabbits(5, 9) == 5
assert get_num_final_rabbits(6, 9) == 8
assert get_num_final_rabbits(7, 9) == 13



num_months, lifespan = (int(x) for x in input().split())
print(get_num_final_rabbits(num_months, lifespan))
