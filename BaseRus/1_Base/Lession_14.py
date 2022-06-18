def printpyton():
    print("Pyton")

def sum(x,y):
    return x+y

def sub(x,y):
    return x-y

def bigsum(*numbers):
    s=0
    for n in numbers:
        s += n
    return s

def printdict(**dict):
    for key in  dict:
        print(key, '=', dict[key])

def summaprint(x, y, r=False):
    s = sum(x, y)
    if  r:
        return s
    else:
        print(s)

def getmax(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max

printpyton()
s = sum(5,8)
print(s)
print(sub(10, 15))

summaprint(15,7)
print(summaprint(10,20, True))

print(sub(y=10,x=15))

print(bigsum(2,5,7,8,6,12))

printdict(name = 'Alex', age = 15)

print('Ананимные функции')
lamdafunct = lambda x, y: print(x+y)
lamdafunct(5,7)

result = (lambda x, y: x+y)(1,3)
print(result)

print('----------------')

print(getmax([1,5,9,7,14,35,2]))
print(getmax([-7, -5, 4, 3, 6]))
