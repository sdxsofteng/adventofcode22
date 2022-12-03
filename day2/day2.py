import aocd

data = list(map(lambda x: x.replace(" ", ""), aocd.get_data(day=2, year=2022).splitlines()))

total_points = 0
game_result = {
    'A': {
        'X': 3,
        'Y': 6,
        'Z': 0,
    },
    'B': {
        'X': 0,
        'Y': 3,
        'Z': 6,
    },
    'C': {
        'X': 6,
        'Y': 0,
        'Z': 3,
    }
}
#Answer 1
for line in data:
    total_points += ord(line[1]) % 87
    total_points += game_result[line[0]][line[1]]
print(total_points)

total_points_2 = 0

#Mapping the computer choices to the player choices
game_choices = {
    'X': {
        'A': 3,
        'B': 1,
        'C': 2,
    },
    'Y': {
        'A': 1,
        'B': 2,
        'C': 3,
    },
    'Z': {
        'A': 2,
        'B': 3,
        'C': 1,
    }
}

#Answer 2
for line in data:
    total_points_2 += (ord(line[1]) % 88) * 3
    total_points_2 += game_choices[line[1]][line[0]]
print(total_points_2)
