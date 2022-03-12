#file for quick code tests
l1 =  ['When', 'you', 'doubt', 'your', 'power', ',', 'you', 'give', 'power', 'to', 'your', 'doubt', '.']
l2 =  ['When', 'you', 'doubt', 'your', 'powwer', ',', 'you', 'give', 'power', 'to', 'your', 'doubt', '.']

error = l2.copy()

mistake = 0

for i in range(len(l2)):
    
    if (l2[i] in l1):
        error.remove(l2[i])

    print(i, "   ", mistake, "   ", error)
res = mistake + len(error)

print(res)