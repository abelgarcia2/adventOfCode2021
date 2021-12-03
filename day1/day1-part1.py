f = open('day1/input.txt', 'r')

strList = f.readlines()
numList = list(map(int, strList))

cont = 0
aux = numList[0]

for i in numList:
    if (i > aux):
        cont += 1
    aux = i

print(cont)
