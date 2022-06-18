list = []
print(list)
list= ['h','e','l','l','o']
print(list)

print(list[0])
print(list[1])
print(list[4])
print("Последний элемент массива",list[-1])
print("длинна массива (количество элементов):", len(list))
print("Последний элемент массива",list[len(list)-1])

print("____________________")
i=0
while i<len(list):
    print(list[i])
    i += 1

print("_____________________")
list = ['a', 3, 5.7, True]
i=0
while i<len(list):
    print(list[i])
    i += 1

list[1] = 'b'
print(list[1])

list[len(list)-1] =False
print(list[len(list)-1])

list= [[2,3], 4]
print(list[0][1])
print(list[1])

print("____________________")

list= [[2,3], [4, 5, 6]]
i=0
while i< len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j+=1
    i +=1


print("____________________")

prices = [20,30,15,20,45,15]
min = prices[0]
max = prices[0]
i=1
while i <len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max =prices[1]
    i += 1
print("Масссив:", prices)
print("Минимальное значение в массиве", min)
print("Максимальное значение в массиве", max)



