import aocd

data = list(aocd.get_data(day=3, year=2022).splitlines())

total_priority = 0

def add_value(c):
    if c[0].isupper():
         priority = ord(c[0]) % 65 + 27
    else:
         priority = ord(c[0]) % 96
    return priority

#Part 1
for line in data:
    first, second = line[int(len(line) / 2):], line[:int(len(line) / 2)]
    c = ''.join(set(first).intersection(second))
    total_priority  += add_value(c)
print(total_priority)

#Part 2
counter = 0
total_priority_group = 0

while counter != len(data):
    line_1, line_2, line_3 = data[counter], data[counter + 1], data[counter + 2]
    c = ''.join(set(line_1).intersection(line_2).intersection(line_3))
    total_priority_group += add_value(c)
    counter += 3
print(total_priority_group)