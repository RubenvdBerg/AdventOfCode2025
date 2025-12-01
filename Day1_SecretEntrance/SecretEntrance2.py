def calculate_code(current_safe_value, turn_value):
    intermediate_safe_value = current_safe_value + turn_value
    code=0
    if not (0 < intermediate_safe_value < 100):
        if turn_value < 0 and intermediate_safe_value != 0 and current_safe_value !=0:
            code+=1
        code+=abs(intermediate_safe_value) // 100
    if intermediate_safe_value == 0:
        code+=1
    return code

def calculate_safe_value(current_safe_value, turn_value):
    return (current_safe_value + turn_value) % 100

def calculate_code_sum(lines):
    code = 0
    safe_value = 50
    for line in lines:
        line = line.strip()
        val = -int(line[1:]) if "L" in line else int(line[1:])
        code += calculate_code(safe_value, val)
        safe_value = calculate_safe_value(safe_value, val)
    return code

if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_code_sum(file))

