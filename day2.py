from day2_data import data

data_ranges = [d for d in data.split(",")]
ranges_tuples = []
for data_range in data_ranges:
    split = data_range.split("-")
    ranges_tuples.append((int(split[0]), int(split[1])))
#print(ranges_tuples)

def sum_invalid_id(start, end):
    invalid_sum = 0
    print(f"{start = } {end = }")
    for number in range(start, end+1):
        str_number = str(number)
        if len(str_number) % 2 == 0:
           half_number_index = len(str_number) // 2
           if str_number[:half_number_index] ==  str_number[half_number_index:]:
               print(f"{str_number[:half_number_index] = } {str_number[half_number_index:] = }")
               invalid_sum += int(str_number)
    print(f"{start = } {end = } {invalid_sum = }")
    return invalid_sum

total_sum = 0
for start, end in ranges_tuples:
    total_sum += sum_invalid_id(start, end)

print(total_sum)

