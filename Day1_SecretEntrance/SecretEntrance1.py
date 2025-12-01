def calculate_value(file):
    safe_value = 50
    real_safe_value = 0
    for line in file:
        line=line.strip()
        print(f"Before:{safe_value}, {line}")
        val = int(line[1:])
        if "R" in line:
            safe_value += val
        else:
            safe_value -= val
        print(f"After:{safe_value}")
        safe_value %= 100
        if safe_value == 0:
            real_safe_value += 1
    return real_safe_value

if __name__ == '__main__':
    with open("input.txt") as input_file:
        print(calculate_value(input_file))