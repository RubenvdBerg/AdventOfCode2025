def calculate_solution1(input):
    return sum(calculate_max_joltage(bank) for bank in input)

def calculate_max_joltage(bank):
    first_digit=max(int(joltage) for joltage in bank[:-1])
    second_digit=max(int(joltage) for joltage in bank[bank.find(str(first_digit))+1:])
    return int(str(first_digit) + str(second_digit))

if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_solution1(file.read().splitlines()))