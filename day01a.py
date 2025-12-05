pointer: int = 50
zero_counter: int = 0

with open('data/day01.txt') as file:
    while line := file.readline().strip():
        direction: str = line[0]  # 'L' or 'R'
        n_turns: int = int(line[1:])

        if direction == 'R':
            pointer += n_turns
            pointer %= 100
        else:
            pointer -= n_turns
            pointer %= 100

        if pointer == 0:
            zero_counter += 1

print(zero_counter)
