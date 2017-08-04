T = int(raw_input())
for i in range(T):
    N = int(raw_input())
    check_ins = map(int,raw_input().split())
    check_outs = map(int,raw_input().split())
    for j in range(N):
        check_outs[j] += check_ins[j]
    check_outs = sorted(check_outs)
    check_ins = sorted(check_ins)
    occupy = 0
    max_occupy = 0
    i = 0
    j = 0
    while i < len(check_ins):
        if check_ins[i] == check_outs[j]:
            i += 1
            j += 1
        elif check_ins[i] < check_outs[j]:
            occupy += 1
            i += 1
            max_occupy = (max_occupy, occupy)[occupy > max_occupy]
        elif check_outs[j] < check_ins[i]:
            occupy -= 1
            j += 1
    print max_occupy