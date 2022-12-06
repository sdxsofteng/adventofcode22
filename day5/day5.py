import aocd

data = list(aocd.get_data(day=5, year=2022).splitlines())

stacks = []

pointer = 0
index = 1
stacks_lines = []

while True:
    stacks_lines.append(data[pointer])
    pointer += 1
    if data[pointer][index].isnumeric():
        stacks_lines.append(data[pointer])
        pointer += 1
        break
move_pointer = pointer + 1

stacks_lines.reverse()
current_stack = 0

while index < len(stacks_lines[0]):
    stacks.append([])
    for line in stacks_lines:
        if line[index].isalnum():
            stacks[current_stack].append(line[index])
    index += 4
    current_stack += 1

while move_pointer <= len(data) - 1:
    line = data[move_pointer].split(" ")
    qty, orig, dest = int(line[1]), int(line[3]), int(line[5])
    if qty == 1:
        for i in range(qty):
            stacks[dest - 1].append(stacks[orig - 1].pop())
    else:
        moved = list()
        for i in range(qty):
            moved.append(stacks[orig - 1].pop())
        moved.reverse()
        for i in range(qty):
            stacks[dest - 1].append(moved[i])
    move_pointer += 1

answer = ""
for line in stacks:
    answer += line.pop()

#aocd.submit(answer, day=5, year=2022, part="a")
aocd.submit(answer, day=5, year=2022, part="b")