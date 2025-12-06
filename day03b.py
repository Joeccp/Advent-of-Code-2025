def findMaxDigit(line: str) -> tuple[int, str]:
    max_digit: str = max(line, key=int)
    return line.find(max_digit), max_digit


def findJoltage(line: str, n: int = 12) -> str:
    if n == 1:
        return findMaxDigit(line)[1]
    prefix_index, prefix = findMaxDigit(line[:-n+1])
    postfix: str = findJoltage(line[prefix_index+1:], n-1)
    return prefix + postfix


with open('data/day03.txt') as file:
    joltage_sum: int = 0
    while line := file.readline().strip():
        joltage_sum += int(findJoltage(line))

print(joltage_sum)
