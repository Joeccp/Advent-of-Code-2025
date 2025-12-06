def findJoltage(line: str) -> int:
    prefix: int = int(line[0])
    prefix_index: int = 0
    for index, number in enumerate(map(int, line[1:-1])):
        if number > prefix:
            prefix = number
            prefix_index = index + 1
    postfix: int = int(max(line[prefix_index+1:], key=int))
    joltage: int = prefix*10 + postfix
    return joltage


with open('data/day03.txt') as file:
    joltage_sum: int = 0
    while line := file.readline().strip():
        joltage_sum += findJoltage(line)

print(joltage_sum)
