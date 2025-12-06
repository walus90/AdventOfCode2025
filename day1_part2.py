from data_day1 import data, test_data

data_lines = data.splitlines()
#data_lines = test_data.splitlines()
#print(data_lines)
current_number = 50
position = 50
max = 100
count = 0
numbers = list(range(max+1))
for code in data_lines:
    if code:
        direction_char = code[0]
        move_number = int(code[1:])
        print(direction_char, move_number)
        zero_crossings = abs(move_number) // max
        count += zero_crossings
        move_number = -(move_number%max) if direction_char=="L" else move_number%max
        next_position = current_number + move_number
        if current_number !=0 and (next_position<0 or next_position>max):
            count += 1
        position = (next_position) % max
        current_number = numbers[position]
        print(f"{current_number=}")
        if current_number==0:
            count += 1
        print(f"{count=}")
            
print(f"{count = }")
