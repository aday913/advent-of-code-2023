input_file = 'data.txt'
data = []
with open(input_file, 'r') as f:
    for i in f:
        data.append(i.strip())

numbers_as_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
indexes_already_taken = []
max_row_size = len(data[0])
num_rows = len(data)

def sum_surrounding_numbers(data : list, symbol_index_row : int, symbol_index_col : int):
    part_total = 0
    all_part_numbers = []

    # top left
    if (symbol_index_row-1 >= 0) and (symbol_index_col-1 >= 0) and (data[symbol_index_row-1][symbol_index_col-1] in numbers_as_strings):
        part_number = get_entire_number(data[symbol_index_row-1], (symbol_index_col-1), symbol_index_row-1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)
    # above
    if (symbol_index_row-1 >= 0) and (data[symbol_index_row-1][symbol_index_col] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row-1], (symbol_index_col), symbol_index_row-1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)    
    # top right
    if (symbol_index_row-1 >= 0) and (symbol_index_col+1 < max_row_size) and (data[symbol_index_row-1][symbol_index_col+1] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row-1], (symbol_index_col+1), symbol_index_row-1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)

    # left
    if (symbol_index_col-1 >= 0) and (data[symbol_index_row][symbol_index_col-1] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row], (symbol_index_col-1), symbol_index_row)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)
    # right
    if (symbol_index_col+1 < max_row_size) and (data[symbol_index_row][symbol_index_col+1] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row], (symbol_index_col+1), symbol_index_row)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)

    # bottom left
    if (symbol_index_row+1 < num_rows) and (symbol_index_col-1 >= 0) and (data[symbol_index_row+1][symbol_index_col-1] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row+1], (symbol_index_col-1), symbol_index_row+1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)
    # below
    if (symbol_index_row+1 < num_rows) and (data[symbol_index_row+1][symbol_index_col] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row+1], (symbol_index_col), symbol_index_row+1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)
    # bottom right
    if (symbol_index_row+1 < num_rows) and (symbol_index_col+1 < max_row_size) and (data[symbol_index_row+1][symbol_index_col+1] in numbers_as_strings):
        part_number =  get_entire_number(data[symbol_index_row+1], (symbol_index_col+1), symbol_index_row+1)
        part_total += part_number
        if part_number != 0:
            all_part_numbers.append(part_number)
    
    if len(all_part_numbers) == 2:
        gear_ratio = all_part_numbers[0] * all_part_numbers[1]
    else:
        gear_ratio = 0

    return part_total, gear_ratio

def get_entire_number(row : str, found_index : int, row_index : int):
    left_index = found_index
    right_index = found_index

    temp = found_index
    while temp >= 0:
        if row[temp] not in numbers_as_strings:
            break
        left_index = temp
        temp -= 1
    
    temp = found_index
    while temp < max_row_size:
        if row[temp] not in numbers_as_strings:
            break
        right_index = temp
        temp += 1

    acceptable_num = True
    for i in range(left_index, right_index+1):
        if [row_index, i] not in indexes_already_taken:
            indexes_already_taken.append([row_index, i])
        else:
            acceptable_num = False
    
    if acceptable_num:
        print(f'Found number: {row[left_index:right_index+1]}')
        return int(row[left_index:right_index+1])
    else:
        return 0

part_number_sum = 0
gear_ratio_sum  = 0
for row_num in range(0, len(data)):
    for col_num in range(0, max_row_size):
        if data[row_num][col_num] in numbers_as_strings or data[row_num][col_num] == '.':
            continue
        
        # Found a symbol, now we sum all the numbers around it
        print(f'Found symbol {data[row_num][col_num]} at index {row_num} {col_num}')
        local_part_sum, local_gear_ratio = sum_surrounding_numbers(data=data, symbol_index_row=row_num, symbol_index_col=col_num)

        part_number_sum += local_part_sum
        gear_ratio_sum += local_gear_ratio

print(part_number_sum)
print(gear_ratio_sum)