import aocd

data = aocd.get_data(day=8, year=2022).splitlines()
#f = open("day8/day8.txt", "r")
#datas = f.readlines()
#data = list()
#for datum in datas:
#    data.append(datum.replace("\n", ""))

#Parse grid
grids = list()
line_counter = 0
for line in data:
    grids.append(list())
    for number in line:
        grids[line_counter].append(int(number))
    line_counter += 1

max_lines = line_counter - 2
max_column = len(grids[0]) - 2
pointer_line = 1
pointer_column = 1
visible_trees = (line_counter * 2) + ((len(grids[0]) - 2) * 2)

highest_scenic_score = 0

def check_tree(grids, line, column):
    ret_val = 0
    left = grids[line][:column]
    right = grids[line][column+1:]
    value = grids[line][column]
    if value > max(left) or  value > max(right):
        return 1
    top_list = list()
    for i in range(0, line):
        top_list.append(grids[i][column])
    bottom_list = list()
    for i in range(line+1, len(grids)):
        bottom_list.append(grids[i][column])
    if value > max(top_list) or value > max(bottom_list):
        return 1
    return ret_val

def scenic_max(grids, line, column, current_max):
    left = list(grids[line][:column])
    right = list(grids[line][column+1:])
    value = grids[line][column]
    s_left, s_right, s_top, s_bottom = 0, 0, 0, 0

    #Left
    counter = 0
    if len(left) > 1:
        left.reverse()
        for tree in left:
            if tree >= value:
                s_left = counter + 1
                break
            counter += 1
        if counter == len(left):
            s_left = len(left)
    else:
        s_left = 1
    #Right
    counter = 0
    if len(right) > 1:
        counter = 0
        for tree in right:
            if tree >= value:
                s_right = counter + 1
                break
            counter += 1
        if counter == len(right):
            s_right = len(right)
    else:
        s_right = 1

    #Top
    counter = 0
    top_list = list()
    for i in range(0, line):
        top_list.append(grids[i][column])
    if len(top_list) > 1:
        top_list.reverse()
        for tree in top_list:
            if tree >= value:
                s_top = counter + 1
                break
            counter += 1
        if counter == len(top_list):
            s_top = len(top_list)
    else:
        s_top = 1

    #Bottom
    counter=0
    bottom_list = list()
    for i in range(line+1, len(grids)):
        bottom_list.append(grids[i][column])
    if len(bottom_list) > 1:
        for tree in bottom_list:
            if tree >= value:
                s_bottom = counter + 1
                break
            counter += 1
        if counter == len(bottom_list):
            s_bottom = len(bottom_list)
    else:
        s_bottom = 1

    scenic_score = s_left * s_right * s_top * s_bottom
    return scenic_score if scenic_score > current_max else current_max

#Count visible trees
for line in range(pointer_line,max_lines + 1):
    for column in range(pointer_column, max_column + 1):
        #visible_trees += check_tree(grids, line, column)
        highest_scenic_score = scenic_max(grids, line, column, highest_scenic_score)



#aocd.submit(visible_trees, day=8, year=2022, part="a")
aocd.submit(highest_scenic_score, day=8, year=2022, part="b")