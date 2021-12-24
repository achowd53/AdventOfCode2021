lines = open("day24.txt").readlines()
a, b, c = [], [], []
for i, line in enumerate(lines):
    if i % 18 == 4:
        a.append(int(line.split()[-1]))
    elif i % 18 == 5:
        b.append(int(line.split()[-1]))
    elif i % 18 == 15:
    	c.append(int(line.split()[-1]))
constraints = {i:tuple() for i in range(14)}
stack = []
for i in range(len(a)):
    if a[i] == 1:
        stack.append((i,c[i]))
    else:
        constraints[stack[-1][0]] = [i, -b[i]-stack[-1][1]]
        constraints[i] = [stack[-1][0], b[i]+stack[-1][1]]
        stack.pop()
def solve(part1): # 1 for part1, -1 for part2
	model = {i:constraints[i] for i in range(14)}
	best_value = 9 if part1==1 else 1
	for idx in model:
		if isinstance(model[idx], list):
			values = (best_value-part1*abs(model[idx][1]), best_value)[::part1]
			model[model[idx][0]] = values[model[idx][1] < 0]
			model[idx] = values[model[idx][1] > 0]
	print(''.join(str(x) for x in model.values()))
solve(1) # Maximize model number
solve(-1) # Minimize model number