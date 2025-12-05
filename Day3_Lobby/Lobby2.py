def calculate_solution(input):
    return sum(calculate_max_joltage(bank) for bank in input)

def calculate_max_joltage(bank):
    int_bank=[int(joltage) for joltage in bank]
    max_length=12
    search_length = len(int_bank) - max_length + 1
    max_joltage = ""
    for i in range(max_length):
        search_list=int_bank[:search_length]
        digit=max(search_list)
        max_joltage+=str(digit)

        start_index=int_bank.index(digit)+1
        int_bank=int_bank[start_index:]
        search_length-=search_list.index(digit)
    return int(max_joltage)

if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_solution(file.read().splitlines()))