from collections import Counter

import aocd

data = aocd.get_data(day=6, year=2022)

answer = -1

for i in range (0, len(data) - 14):
    counter = Counter(data[i:i+14])
    if len(counter) == 14:
        answer = i + 14
        break



#aocd.submit(answer, day=6, year=2022, part="a")
aocd.submit(answer, day=6, year=2022, part="b")