import sys

def get_priority(item):
    val = ord(item)
    if item > 'Z':
        pri = val - ord('a') + 1
        print("Priority of ", item, " is ", pri)
        return pri
    else:
        pri = val - ord('A') + 27
        print("Priority of ", item, " is ", pri)
        return pri

def get_intersect(first, second):
    if len(first) != len(second):
        print("ERROR, inputs have different lengths: ", first, " ", second)
        sys.exit()
    chars = {}
    for char in first:
        chars[char] = 1
    for char in second:
        if char in chars:
            return char
    print("ERROR, inputs do not intersect: ", first, " ", second)
    sys.exit()

total = 0

for line in sys.stdin.readlines():
    line = line[:-1]
    
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]

    total += get_priority(get_intersect(first, second))

print("Total: ", total) 
