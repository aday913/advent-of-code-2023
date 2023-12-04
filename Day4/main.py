input_file = 'data.txt'
data = []
with open(input_file, 'r') as f:
    for i in f:
        data.append(i.strip())

# Part One
total_points = 0
for card in data:
    print(f'--------------------')

    winning_numbers = [int(i) for i in card.split(': ')[-1].split(' | ')[0].split(' ') if i != '']
    numbers_you_have = [int(i) for i in card.split(': ')[-1].split(' | ')[-1].split(' ') if i != '']
    your_winning_numbers = [int(i) for i in card.split(': ')[-1].split(' | ')[-1].split(' ') if i != '' and int(i) in winning_numbers]

    print(f'Winning numbers: {winning_numbers}')
    print(f'Numbers you have: {numbers_you_have}')
    print(f'Your winning numbers: {your_winning_numbers}')

    points = 0
    if len(your_winning_numbers) != 0:
        points = 1
        for i in range(len(your_winning_numbers)-1):
            points = points * 2
    print(f'Points for this card: {points}')
    total_points += points
print(f'--------------------')
print(f'Total points: {total_points}')
print(f'======================================')

# Part Two
card_counts = {}
for card in data:
    card_number = int(card.split(':')[0].split(' ')[-1])
    card_counts[card_number] = 1
for card in data:
    print(f'--------------------')

    card_number = int(card.split(':')[0].split(' ')[-1])
    print(f'Processing card number {card_number}')
    print(f'Card number {card_number} has {card_counts[card_number]} copies')

    winning_numbers = [int(i) for i in card.split(': ')[-1].split(' | ')[0].split(' ') if i != '']
    numbers_you_have = [int(i) for i in card.split(': ')[-1].split(' | ')[-1].split(' ') if i != '']
    your_winning_numbers = [int(i) for i in card.split(': ')[-1].split(' | ')[-1].split(' ') if i != '' and int(i) in winning_numbers]

    print(f'Winning numbers: {winning_numbers}')
    print(f'Numbers you have: {numbers_you_have}')
    print(f'Your winning numbers: {your_winning_numbers}')

    for i in range(0, len(your_winning_numbers)):
        print(f'Adding {card_counts[card_number]} copies of card {card_number + i + 1}')
        card_counts[card_number + i + 1] += card_counts[card_number]

total_points = 0
for i in card_counts.keys():
    total_points += card_counts[i]
print(f'Total number of cards: {total_points}')