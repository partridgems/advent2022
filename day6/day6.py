import sys

MARKER_LENGTH = 14

def unique(buffer):
    if len(buffer) != MARKER_LENGTH:
        print("ERROR, checking incomplete buffer:", buff)
        sys.exit()
    my_set = set()
    for x in buff:
        if x in my_set:
            return False
        else:
            my_set.add(x)
    print("Buffer is unique:", buffer)
    return True

signal = sys.stdin.readlines()[0]

buff = []
for i in range(len(signal)):
    if i < MARKER_LENGTH - 1:
        buff.append(signal[i])
    else:
        buff.append(signal[i])
        if unique(buff):
            print("Found start at", i + 1, "\nBuffer:", buff)
            sys.exit()
        else:
            buff = buff[1:]

print("ERROR: Did not find start token.")
