f = open("input.txt","r")
array = f.read().splitlines()
input = [[]]
c = 0
for i in range(len(array)):
    if array[i] == '':
        input.append([])
        c+=1
    else:
        input[c].append(array[i])
solution = []
for i in range(len(input)):
    number = 0
    for j in range(len(input[i])):
        number+=int(input[i][j])
    solution.append(number)
print(solution)
max,maxsnumber = 0,0
for i in range(len(solution)):
    if max < solution[i]:
        max = solution[i]
        maxsnumber = i
print(max,maxsnumber)
