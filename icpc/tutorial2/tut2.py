from sys import stdin

for line in stdin:
    data = list(map(int, line.split(' ')))
    diff = data[0] - data[1]
    print(abs(diff))

