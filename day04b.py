from copy import deepcopy


with open('data/day04.txt') as file:
    lines: list[str] = file.readlines()
lines = list(map(str.strip, lines))
max_line_index: int = len(lines)-1
max_character_index: int = len(lines[0])-1

accessible_paper_count: int = 0


def removePaper(lines: list[str]) -> list[str]:
    global accessible_paper_count

    new_lines: list[str] = deepcopy(lines)

    for line_index, line in enumerate(lines):
        for character_index, character in enumerate(line):
            adjacent_paper_count: int = 0

            if character != '@':
                continue

            # Top left
            if line_index != 0 and character_index != 0:
                top_left: str = lines[line_index-1][character_index-1]
                if top_left == '@':
                    adjacent_paper_count += 1

            # Top
            if line_index != 0:
                top: str = lines[line_index-1][character_index]
                if top == '@':
                    adjacent_paper_count += 1

            # Top right
            if line_index != 0 and character_index != max_character_index:
                top_right: str = lines[line_index-1][character_index+1]
                if top_right == '@':
                    adjacent_paper_count += 1

            # Left
            if character_index != 0:
                left: str = line[character_index-1]
                if left == '@':
                    adjacent_paper_count += 1

            # Right
            if character_index != max_character_index:
                right: str = line[character_index+1]
                if right == '@':
                    adjacent_paper_count += 1

            # Bottom left
            if line_index != max_line_index and character_index != 0:
                bottom_left: str = lines[line_index+1][character_index-1]
                if bottom_left == '@':
                    adjacent_paper_count += 1

            # Bottom
            if line_index != max_line_index:
                bottom: str = lines[line_index+1][character_index]
                if bottom == '@':
                    adjacent_paper_count += 1

            # Bottom right
            if line_index != max_line_index and character_index != max_character_index:
                bottom_right: str = lines[line_index+1][character_index+1]
                if bottom_right == '@':
                    adjacent_paper_count += 1

            if adjacent_paper_count < 4:
                accessible_paper_count += 1
                new_lines[line_index] = new_lines[line_index][:character_index] + '.' + new_lines[line_index][character_index+1:]

    return new_lines


while True:
    old_accessible_paper_count: int = accessible_paper_count
    lines: list[str] = removePaper(lines)
    if old_accessible_paper_count == accessible_paper_count:
        print(accessible_paper_count)
        break
