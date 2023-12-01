input_data = 'data.txt'
data = []
with open(input_data, 'r') as f:
    for i in f:
        data.append(i)

# First task
acceptable_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sum_total = 0
for new in data:
    number = ''
    # Get first val
    for char in new:
        if char in acceptable_chars:
            number = number + char
            break
    # Get second val
    for i in range(0, len(new)):
        if new[-1 - i] in acceptable_chars:
            number = number + new[-1 - i]
            break
    int_number = int(number)
    sum_total += int_number
print(sum_total)

# Second task
acceptable_ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
acceptable_nums = {'zero': '0',
                   'one' : '1', 
                   'two' : '2', 
                   'three' : '3', 
                   'four' : '4', 
                   'five' : '5', 
                   'six' : '6', 
                   'seven' : '7', 
                   'eight' : '8', 
                   'nine' : '9'}
sum_total = 0
for new in data:
    number = ''
    # Get first value
    for i in range(0, len(new)):
        sub_string = new[i:]
        if sub_string[0] in acceptable_ints:
            number = number + sub_string[0]
            break
        for num in acceptable_nums.keys():
            if sub_string.find(f'{num}') == 0:
                number = number + acceptable_nums[num]
                break
        else:
            continue
        break
    # Get second value
    for i in range(0, len(new)):
        if i == 0:
            sub_string = new
        else:
            sub_string = new[:0-i]

        if sub_string[-1] in acceptable_ints:
            number = number + sub_string[-1]
            break
        for num in acceptable_nums.keys():
            if ((sub_string.rfind(f'{num}') + len(num)) == len(sub_string)) and (sub_string.rfind(f'{num}') != -1):
                number = number + acceptable_nums[num]
                break
        else:
            continue
        break
    int_number = int(number)
    sum_total += int_number
print(sum_total)
