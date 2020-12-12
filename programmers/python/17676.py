def convert(arr1,k):
    get= []
    for i in range(len(arr1)):
        m = bin(arr1[i])[2:]
        n = '0'*(k - len(m))+ m
        arr1_1 =''
        for j in n:
            if j=='1':
                arr1_1 += '#'
            else:
                arr1_1 += ' '
        get.append(arr1_1)
    return get

def plus(arr1, arr2):
    get = []
    for i in range(len(arr1)):
        key = arr1[i]
        key2 = arr2[i]
        value =''
        for j in range(len(key)):
            if key[j]==' ' and  key2[j]==' ':
                value += ' '
            else:
                value += '#'
        get.append(value)
    return get

def solve(n,arr1,arr2):
    get=[]
    arr1 = convert(arr1,n)
    arr2 = convert(arr2,n)
    get = plus(arr1,arr2)
    return get