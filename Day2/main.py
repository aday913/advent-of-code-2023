input_file = 'data.txt'
data = []
with open(input_file, 'r') as f:
    for i in f:
        data.append(i.strip())

# example of a single line: "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

# PART ONE
allowed = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}
sum_total = 0
for game in data:
    id, all_pulls = game.split(': ')
    id = int(id.split(' ')[-1])

    too_many = False
    for draw in all_pulls.split('; '):
        # print(draw)
        for pull in draw.split(', '):
            amount, color = pull.split(' ')
            # print(f'{amount}, {color}')
            if  int(amount) > allowed[color]:
                too_many = True
                break
        else:
            continue
        break

    if not too_many:
        sum_total += int(id)
print(sum_total)

# PART TWO
sum_total = 0
for game in data:
    minimums = {
        'red' : 0,
        'green' : 0,
        'blue' : 0
    }
    id, all_pulls = game.split(': ')

    for draw in all_pulls.split('; '):
        # print(draw)
        for pull in draw.split(', '):
            amount, color = pull.split(' ')
            # print(f'{amount}, {color}')
            if int(amount) > minimums[color]:
                minimums[color] = int(amount)
    power = minimums['blue'] * minimums['green'] * minimums['red']
    sum_total += power
print(sum_total)