fr = open('input.txt', 'r')
line = fr.readline()
sum = 0
while line:
    sum += int(line)
    line = fr.readline()
print(sum)