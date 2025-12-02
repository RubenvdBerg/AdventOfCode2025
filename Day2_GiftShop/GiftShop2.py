def parse_input():
    with open("input.txt") as file:
        return file.read()

def calculate_id_sum(data):
    id_ranges = data.split(",")
    id_sum = 0
    max_end = 0
    for id_range in id_ranges:
        begin, end = id_range.split("-")
        id_sum += check_range(begin, end)
    return id_sum

def check_range(begin, end):
    val=0
    for num in range(int(begin), int(end) + 1):
        if check_multiple(str(num)):
            val += num
    return val

def check_multiple(number):
    len_number = len(number)
    for i in [2,3,5,7]:
        if len_number%i==0:
            part=number[:len_number//i]
            complete=part*i
            if complete==number:
                return True
    return False

if __name__ == '__main__':
    print(calculate_id_sum(parse_input()))