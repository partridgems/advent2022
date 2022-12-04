import sys

values = {'A':1, 'B':2, 'C':3, 'X':1, 'Y':2, 'Z':3}

def compute_score(line):
    split = line.split(' ')
    (them, us) = (split[0], split[1])
    if not them in values or not us in values:
        print(line, ' is not found in values!')
        sys.exit()
    score = values[us]
    if values[them] == values[us]:
        score += 3
    elif (values[them]) % 3 == values[us] - 1:
        score += 6
    
    return score

cases = 0
total = 0
scores = {}

for line in sys.stdin.readlines():
    line = line[:-1]
    score = compute_score(line)
    print("score for ", line, " is ", score)
    total += score
    cases += 1
    if score in scores:
        scores[score] += 1
    else:
        scores[score] = 1

print(total, ' from ', cases, ' cases.')
print(scores)
