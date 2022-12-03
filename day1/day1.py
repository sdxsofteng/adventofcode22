import aocd

data = aocd.get_data(day=1, year=2022)

data = data.split("\n\n")
sums = list()
for datum in data:
    sums.append(sum(map(lambda x: int(x), datum.splitlines())))
#Answer 1
print(max(sums))
#Answer 2
print(sum(map(lambda x: int(x), sorted(sums, reverse=True)[:3])))

