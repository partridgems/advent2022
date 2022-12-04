import sys

def overlap(line):
    sections = [[int(elfnum) for elfnum in elf.split('-')] for elf in line.split(',')]
    # Get the lower starting section first
    sections.sort()
    # no overlap means first ends strictly before second starts
    return not (sections[0][1] < sections[1][0])


total_overlaps = 0

for line in sys.stdin.readlines():
    line = line[:-1]
    if overlap(line):
        print("overlaps:", line)
        total_overlaps += 1
    else:
        print("does not overlap:", line)

print(total_overlaps)

