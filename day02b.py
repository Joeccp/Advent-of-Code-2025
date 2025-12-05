with open('data/day02.txt') as file:
    line: str = file.readline()

ranges: list[range] = []

for str_range in line.split(','):
    str_start, str_end = str_range.split('-')
    start: int = int(str_start)
    end: int = int(str_end) + 1  # range's end is exclusive
    ranges.append(range(start, end))

sum_: int = 0


def isInvalid(str_number: str) -> bool:
    length: int = len(str_number)
    for sub_length in range(1, length+1):
        pattern: str = str_number[:sub_length]
        temp_str: str = pattern
        while len(temp_str) < length:
            temp_str += pattern
            if temp_str == str_number:
                return True
    return False


for each_range in ranges:
    for number in each_range:
        if isInvalid(str(number)):
            sum_ += number

print(sum_)
