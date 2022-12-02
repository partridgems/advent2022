import sys

current_elf = 0

# This wants a size-3 min heap. But 3 is small.
top3 = []

for line in sys.stdin.readlines():

    # Strip newline
    line = line[:-1]

    if not line:
        # Finished this elf. Add to the "heap"
        if len(top3) < 3:
            top3.append(current_elf)
        elif current_elf > top3[0]:
            top3[0] = current_elf
            top3.sort()
        current_elf = 0
    else:
        current_elf += int(line)

print("The most prepared (or greedy?) 3 elves had ", sum(top3), " (", top3,") calories!")

