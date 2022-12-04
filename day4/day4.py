import sys

def fully_contains(line):
    sections = [[int(elfnum) for elfnum in elf.split('-')] for elf in line.split(',')]
    # Get the lower starting section first
    sections.sort()
    return (sections[0][0] < sections[1][0] and sections[0][1] >= sections[1][1]) or sections[0][0] == sections[1][0]

total_dupes = 0

for line in sys.stdin.readlines():
    line = line[:-1]
    if fully_contains(line):
        print("fully contains:", line)
        total_dupes += 1
    else:
        print("does not contain:", line)

print(total_dupes)

