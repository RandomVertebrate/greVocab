DicFile = open('grewords.txt', 'r')
lines = DicFile.readlines()
DicFile.close()
lines.sort()
SortedFile = open('grewords.txt', 'w')
for line in lines:
    SortedFile.write(line)
SortedFile.close()
