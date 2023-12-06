import os
import datetime

"""
Looks like the idea here is to make use of ranges starting with zeroes in the maps.
I guess we should move backwards from minimum range of humidity-to-location map 
[0, 1766978803, 483883727] to temperature-to-humidity map etc.

"""


def main():

    cur_path = os.path.dirname(os.path.abspath(__file__))
    input_file = open(cur_path + "\\05_input.txt", "r")
    lines = input_file.readlines()
    input_file.close()

    LINES_LEN = len(lines)

    # Create seeds list
    seeds_orig = list(map(int, lines[0].replace("seeds: ", "", 1).split()))
    seeds_orig_index = 0
    seeds_pairs = []
    while seeds_orig_index < len(seeds_orig):
        seeds_start_index = seeds_orig[seeds_orig_index]
        seeds_rng_len = seeds_orig[seeds_orig_index + 1]
        seeds_pairs.append([seeds_start_index, seeds_rng_len])
        seeds_pairs.sort(key=lambda x: x[0])  # min: [342640189, 97088268]
        seeds_orig_index += 2

    line_index = 2
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    while line_index < LINES_LEN:
        line = lines[line_index]

        if line.startswith("seed-to-soil map:"):
            line_index = create_map(lines, seed_to_soil_map, line_index)
            seed_to_soil_map_short = [seed_to_soil_map[0]]

        elif line.startswith("soil-to-fertilizer"):
            line_index = create_map(lines, soil_to_fertilizer_map, line_index)
            soil_to_fertilizer_map_short = [soil_to_fertilizer_map[0]]

        elif line.startswith("fertilizer-to-water"):
            line_index = create_map(lines, fertilizer_to_water_map, line_index)
            fertilizer_to_water_map_short = [fertilizer_to_water_map[0]]

        elif line.startswith("water-to-light"):
            line_index = create_map(lines, water_to_light_map, line_index)
            water_to_light_map_short = [water_to_light_map[0]]

        elif line.startswith("light-to-temperature"):
            line_index = create_map(
                lines, light_to_temperature_map, line_index)
            light_to_temperature_map_short = [light_to_temperature_map[0]]

        elif line.startswith("temperature-to-humidity"):
            line_index = create_map(
                lines, temperature_to_humidity_map, line_index)
            temperature_to_humidity_map_short = [
                temperature_to_humidity_map[0]]

        elif line.startswith("humidity-to-location"):
            line_index = create_map(
                lines, humidity_to_location_map, line_index)
            humidity_to_location_map_short = [humidity_to_location_map[0]]

    # find max location
    max_location_start = max(humidity_to_location_map, key=lambda x: x[0])[0]
    max_location = None
    for sublist in humidity_to_location_map:
        if sublist[0] == max_location_start:
            max_location = max_location_start + sublist[2]
            break
    print("Current time:", time_start)
    print("max_location =", max_location)

    seeds_pairs_short = []
    for seeds_pair in seeds_pairs:
        if seeds_pair[0] in range(seed_to_soil_map_short[0][1], seed_to_soil_map_short[0][1] + seed_to_soil_map_short[0][2]):
            seeds_pairs_short.append([seed_to_soil_map_short[0][1], 1])
            break
        if seeds_pair[0] + seeds_pair[1] in range(seed_to_soil_map_short[0][1], seed_to_soil_map_short[0][1] + seed_to_soil_map_short[0][2]):
            seeds_pairs_short.append([seed_to_soil_map_short[0][1], 1])
            break
    
    # if seeds_pairs_short[0][1] < seed_to_soil_map_short[0][1]:
    #     seeds_pairs_short[0][1] = seed_to_soil_map_short[0][1]
    
    # if seeds_pairs_short[0][1] + seeds_pairs_short[0][2] > seed_to_soil_map_short[0][1] + seed_to_soil_map_short[0][2]:
    #     seeds_pairs_short[0][1] = seed_to_soil_map_short[0][1]


    min_location = max_location
    for seed_pair in seeds_pairs_short:
        print("Seed pair: ", seed_pair)
        print("Current time:", time_start)

        for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
            soil = get_cor_type_number(seed_to_soil_map_short, seed)
            fertilizer = get_cor_type_number(
                soil_to_fertilizer_map, soil)
            water = get_cor_type_number(
                fertilizer_to_water_map, fertilizer)
            light = get_cor_type_number(water_to_light_map, water)
            temperature = get_cor_type_number(
                light_to_temperature_map, light)
            humidity = get_cor_type_number(
                temperature_to_humidity_map, temperature)
            location = get_cor_type_number(
                humidity_to_location_map, humidity)

            if location < min_location:
                min_location = location

    print("Closest location:", min_location)


def get_cor_type_number(map_list: list, src_num: int):
    trg_num = src_num

    for row in map_list:
        trg_start = row[0]
        src_start = row[1]
        rng_len = row[2]

        if src_num in range(src_start, src_start + rng_len):
            shift = src_num - src_start
            trg_num = trg_start + shift
            break

    return trg_num


def create_map(lines: list, map_list: list, line_index: int):
    lines_len = len(lines)
    line_index += 1
    while line_index < lines_len and lines[line_index] != "\n":
        map_list.append(list(map(int, lines[line_index].split())))
        line_index += 1
    line_index += 1

    # Sort by source
    map_list.sort(key=lambda x: x[0])
    map_list = [map_list[0]]

    return line_index


if __name__ == "__main__":
    time_start = datetime.datetime.now()
    print("Start:", time_start)

    main()

    time_end = datetime.datetime.now()
    print("End:", time_end)
    print("Duration:", time_end - time_start)
