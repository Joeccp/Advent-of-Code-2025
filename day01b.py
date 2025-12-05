pointer: int = 50
zero_counter: int = 0

with open('data/day01.txt') as file:
    while line := file.readline().strip():
        direction: str = line[0]  # 'L' or 'R'
        n_turns: int = int(line[1:])

        if direction == 'R':
            for _ in range(n_turns):
                pointer += 1
                if pointer == 100:
                    pointer = 0
                    zero_counter += 1
        else:
            for _ in range(n_turns):
                pointer -= 1
                if pointer == 0:
                    zero_counter += 1
                elif pointer == -1:
                    pointer = 99

print(zero_counter)
