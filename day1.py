from data_day1 import data

data_lines = data.splitlines()
#print(data_lines)
current = 50
position = 50
max = 100
count = 0
numbers = list(range(max+1))
for code in data_lines:
    if code:
        direction_char = code[0]
        move_number = int(code[1:])
        print(direction_char, move_number)
        if direction_char=="L":
            move_number = -move_number
        position = (current + move_number) % max
        current = numbers[position]
        print(current)
        if current==0:
            count += 1
            
print(f"{count = }")
