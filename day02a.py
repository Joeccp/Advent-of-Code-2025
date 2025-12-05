with open('data/day02.txt') as file:
    line: str = file.readline()

ranges: list[range] = []

for str_range in line.split(','):
    str_start, str_end = str_range.split('-')
    start: int = int(str_start)
    end: int = int(str_end) + 1  # range's end is exclusive
    ranges.append(range(start, end))

sum_: int = 0

for each_range in ranges:
    for num in each_range:
        str_num: str = str(num)
        length: int = len(str_num)
        if length % 2 == 1:
            continue
        if str_num[:int(length/2)] == str_num[int(length/2):]:
            sum_ += num

print(sum_)
