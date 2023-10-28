output = " "

for i in range(0, 6):
        for j in range(i, 0, -1):
            output += ' '
        for j in range(0, 9-(2 * i)):
            output += '*'
        output += '\n'

print(output)
