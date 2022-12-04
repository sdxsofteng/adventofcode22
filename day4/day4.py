import aocd

data = aocd.get_data(day=4, year=2022).splitlines()

total_contained = 0

for line in data:
    new_line = list()
    split = line.split(',')
    for datum in split:
        new_line.append(datum.split('-'))
    min_first, max_first, min_second, max_second = int(new_line[0][0]), int(new_line[0][1]), int(new_line[1][0]), int(new_line[1][1])
    if (min_first <= min_second and max_first >= max_second) or (min_second <= min_first and max_second >= max_first) or ((max_first >= min_second and max_first <= max_second) or ( max_second >= min_first and max_second <= max_first)):
        total_contained += 1



#aocd.submit(total_contained, day=4, year=2022, part="a")
aocd.submit(total_contained, day=4, year=2022, part="b")