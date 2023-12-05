input_file = 'data.txt'
data = {
    'seeds'                     : [],
    'seed_to_soil'              : [],
    'soil_to_fertilizer'        : [],
    'fertilizer_to_water'       : [],
    'water_to_light'            : [],
    'light_to_temperature'      : [],
    'temperature_to_humidity'   : [],
    'humidity_to_location'      : [],
}
# TODO: Add all possible seeds to the data dictionary first on a computer with more memory,
#  then brute force using the same method as part one!
with open(input_file, 'r') as f:
    key = None
    for j in f:
        i = j.strip()
        if i == '':
            key = None
        # elif 'seeds' in i:
        #     data['seeds'] = [int(num) for num in i.split(': ')[-1].split(' ')] ### PART ONE HERE
        elif 'seeds' in i:
            continue
        elif 'map' in i:
            key = i.split(' map:')[0].replace('-', '_')
        else:
            data[key].append([int(num) for num in i.split(' ')])

def get_destination_value(list_of_ranges : list, source_value : int):
    for test_ranges in list_of_ranges:
        # print(f'  Testing if {source_value} is in range {test_ranges[1]} to {test_ranges[1] + test_ranges[2]}')
        if source_value in range(test_ranges[1], test_ranges[1] + test_ranges[2]):
            diff = source_value - test_ranges[1]
            dest_value = test_ranges[0] + diff
            break
    else:
        dest_value = source_value
    # print(f'Returning value {dest_value}')
    return dest_value

### BELOW IS PART ONE STUFF

# print(data)
# all_locations = []
# for seed in data['seeds']:
#     print(f'Evaluating seed {seed}')
#     soil = get_destination_value(data['seed_to_soil'], seed)
#     fert = get_destination_value(data['soil_to_fertilizer'], soil)
#     water = get_destination_value(data['fertilizer_to_water'], fert)
#     light = get_destination_value(data['water_to_light'], water)
#     temp = get_destination_value(data['light_to_temperature'], light)
#     hum = get_destination_value(data['temperature_to_humidity'], temp)
#     location = get_destination_value(data['humidity_to_location'], hum)
#     all_locations.append(location)
#     print('========================')
    
# print(min(all_locations))

### HERE IS PART TWO STUFF
lowest_location = 10000000000000000000000000000
seed_iterator = 0
with open(input_file, 'r') as f:
    for i in f:
        j = i.strip()
        if 'seeds' in j:
            all_values = [int(num) for num in i.split('seeds: ')[-1].split(' ')]
            for k in range(1, len(all_values) + 1):
                if k % 2 != 1:
                    continue
                start_value = all_values[k-1]
                range_size = all_values[k]
                for val in range(start_value, start_value + range_size):
                    print(f'Seed: {(seed_iterator + 1):,}')
                    soil = get_destination_value(data['seed_to_soil'], val)
                    fert = get_destination_value(data['soil_to_fertilizer'], soil)
                    water = get_destination_value(data['fertilizer_to_water'], fert)
                    light = get_destination_value(data['water_to_light'], water)
                    temp = get_destination_value(data['light_to_temperature'], light)
                    hum = get_destination_value(data['temperature_to_humidity'], temp)
                    location = get_destination_value(data['humidity_to_location'], hum)
                    if location < lowest_location:
                        print(f'New lowest: {location} from range {start_value} to {start_value + range_size}')
                        lowest_location = location
                    seed_iterator += 1
print(lowest_location)
