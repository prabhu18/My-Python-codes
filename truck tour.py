class node:
    def __init__(self, fuel, next_distance):
        self.fuel = fuel
        self.next_distance = next_distance


pumps = []


def process_pump(pumps, pos):
    count = 1
    length = len(pumps)
    carry = pumps[pos].fuel - pumps[pos].next_distance
    while count != length:
        if pos == length - 1:
            pos = 0
        else:
            pos = pos + 1
        if carry + pumps[pos].fuel > pumps[pos].next_distance:
            count = count + 1
            carry = carry + pumps[pos].fuel - pumps[pos].next_distance
        else:
            return False

    return True


for i in range(input()):
    var = map(int, raw_input().split())
    fuel = var[0]
    next_distance = var[1]
    pumps.append(node(fuel, next_distance))

flag = False
for i in range(0, len(pumps)):
    if pumps[i].fuel - pumps[i].next_distance < 0:
        pass
    else:
        possible = process_pump(pumps, i)

        if possible is True:
            break

print i



