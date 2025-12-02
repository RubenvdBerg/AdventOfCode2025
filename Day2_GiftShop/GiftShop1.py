def calculate_id_sum1(input):
    ranges=input.split(',')
    val=0
    for ranger in ranges:
        begin, end = ranger.split('-')
        l_begin = len(str(begin))
        l_end = len(str(end))
        if (l_begin%2==0 and l_end%2==0) or (l_end>l_begin):
            for number in range(int(begin), int(end)+1):
                if check_double(str(number)):
                    val += number
    return val

def check_double(value):
    len_value=len(value)
    half = value[:len_value//2]
    return half + half == value



if __name__ == '__main__':
    with open("input.txt") as file:
        print(calculate_id_sum1(file.read()))