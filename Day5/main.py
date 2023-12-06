# Data parsing:
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
with open(input_file, 'r') as f:
    key = None
    for j in f:
        i = j.strip()
        if i == '':
            key = None
        elif 'seeds' in i:
            data['seeds'] = [int(num) for num in i.split(': ')[-1].split(' ')] 
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
all_locations = []
for seed in data['seeds']:
    # print(f'Evaluating seed {seed}')
    soil = get_destination_value(data['seed_to_soil'], seed)
    fert = get_destination_value(data['soil_to_fertilizer'], soil)
    water = get_destination_value(data['fertilizer_to_water'], fert)
    light = get_destination_value(data['water_to_light'], water)
    temp = get_destination_value(data['light_to_temperature'], light)
    hum = get_destination_value(data['temperature_to_humidity'], temp)
    location = get_destination_value(data['humidity_to_location'], hum)
    all_locations.append(location)
    # print('========================')
    
print(min(all_locations))

### HERE IS PART TWO STUFF

### Brute force that takes way too long to complete:
# lowest_location = 10000000000000000000000000000
# seed_iterator = 0
# with open(input_file, 'r') as f:
#     for i in f:
#         j = i.strip()
#         if 'seeds' in j:
#             all_values = [int(num) for num in i.split('seeds: ')[-1].split(' ')]
#             for k in range(1, len(all_values) + 1):
#                 if k % 2 != 1:
#                     continue
#                 start_value = all_values[k-1]
#                 range_size = all_values[k]
#                 for val in range(start_value, start_value + range_size):
#                     print(f'Seed: {(seed_iterator + 1):,}')
#                     soil = get_destination_value(data['seed_to_soil'], val)
#                     fert = get_destination_value(data['soil_to_fertilizer'], soil)
#                     water = get_destination_value(data['fertilizer_to_water'], fert)
#                     light = get_destination_value(data['water_to_light'], water)
#                     temp = get_destination_value(data['light_to_temperature'], light)
#                     hum = get_destination_value(data['temperature_to_humidity'], temp)
#                     location = get_destination_value(data['humidity_to_location'], hum)
#                     if location < lowest_location:
#                         print(f'New lowest: {location} from range {start_value} to {start_value + range_size}')
#                         lowest_location = location
#                     seed_iterator += 1
# print(lowest_location)

### Using backtracking to find the seeds that produce the smallest locations
# Idea: take the smallest possible location range and backtrack up to find what seed values
#  cause those locations to be true, then see if any of the input seed ranges have those values.
#  Repeat with the next smallest location range until you get values that are possible as input seeds

def get_source_range(list_of_destination_ranges : list, source_to_dest_map : list):
    '''Given the destination range, will look for the range cutoffs of the source values that fall in this destination range
    '''
    pass


data['humidity_to_location'].sort()
for humidity_to_location_range in data['humidity_to_location']:
    location_range = [[ humidity_to_location_range[0], humidity_to_location_range[0] + humidity_to_location_range[-1] ]]
    humidity_ranges = get_source_range(location_range, data['humidity_to_location'])
    temp_ranges     = get_source_range(humidity_ranges, data['temperature_to_humidity'])
    light_ranges    = get_source_range(temp_ranges, data['light_to_temperature'])
    water_ranges    = get_source_range(light_ranges, data['water_to_light'])
    fert_ranges     = get_source_range(water_ranges, data['fertilizer_to_water'])
    soil_ranges     = get_source_range(fert_ranges, data['soil_to_fertilizer'])
    seed_ranges     = get_source_range(soil_ranges, data['seed_to_soil'])

    # Now we check if any of the seed ranges fall in any of the ranges provided at the top of the data:

    pass
else:
    # if the location ranges provided don't work, we have to do manual checks with 1:1 mappings
    pass