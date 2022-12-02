import sys

current_elf = 0
global_max = 0

for line in sys.stdin.readlines():

    print("considering line ", line)
    # Strip newline
    line = line[:-1]

    if not line:
        if current_elf > global_max:
            global_max = current_elf
        current_elf = 0
    else:
        current_elf += int(line)

print("The most prepared (or greedy?) elf had ", global_max, " calories!")

