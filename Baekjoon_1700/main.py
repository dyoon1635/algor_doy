n, k = map(int, input().split())
appliance = list(map(int, input().split()))
multitap = []

result = 0
for idx, each in enumerate(appliance):
    if each in multitap: continue
    if len(multitap) < n:
        multitap.append(each)
        continue

    priority = [0 for _ in range(n)]
    for i, tmp in enumerate(multitap):
        if tmp in appliance[idx:]: priority[i] = appliance[idx:].index(tmp)
        else: priority[i] = 101
    removed_idx = priority.index(max(priority))
    #print('removed ', multitap[removed_idx])
    del multitap[removed_idx]
    result += 1
    multitap.append(each)
print(result)