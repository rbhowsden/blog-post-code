num_houses = 20

distances = []

for x in range(num_houses):
    for y in range(num_houses):
        if x != y:
            distances.append(abs(x-y))

average_dist = sum(distances)/len(distances)

import random

num_houses = 10000
sims = 100000
total_dist = 0

for x in range(sims):
    you = random.randint(1, num_houses)
    friend = random.randint(1, num_houses)
    total_dist += abs(you-friend)

print(total_dist/sims)