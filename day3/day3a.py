import sys

def get_priority(item):
    val = ord(item)
    if item > 'Z':
        pri = val - ord('a') + 1
        return pri
    else:
        pri = val - ord('A') + 27
        return pri

def get_intersect(first, second, third):
    chars = {}
    for char in first:
        chars[char] = 1
    for char in second:
        if char in chars:
            chars[char] = 2
    for char in third:
        if char in chars and chars[char] == 2:
            return char
    print("ERROR, inputs do not intersect:", first, second, third, "\n", chars)
    sys.exit()

total = 0
group = []
for line in sys.stdin.readlines():
    line = line[:-1]
    group.append(line)
    if len(group) == 3:
        total += get_priority(get_intersect(group[0], group[1], group[2]))
        group = []

print("Total: ", total) 
