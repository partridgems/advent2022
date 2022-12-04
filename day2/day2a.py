import sys

values = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}

def compute_score(line):
    split = line.split(' ')
    (them, outcome) = (split[0], split[1])
    # score = values[us]
    score = values[outcome] * 3
    score += (values[them] + values[outcome] - 1) % 3 + 1
    
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
