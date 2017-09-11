stacknew = []
stackold = []


def shiftnew(stacknew, stackold):
    if len(stackold) == 0:
        while (len(stacknew) > 0):
            stackold.append(stacknew.pop())


for i in range(0, input()):
    var = map(int, raw_input().split(' '))
    if var[0] == 1:
        stacknew.append(var[1])
    if var[0] == 2:
        shiftnew(stacknew, stackold)
        stackold.pop()
    if var[0] == 3:
        shiftnew(stacknew, stackold)
        print stackold[len(stackold) - 1]
