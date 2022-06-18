list = [1, 5, -1, 4,-2.5, "s"]
for n in list:
    print(n)

print("---------------------")

str = "Pyton"
print(str[0])

for a in str:
    print(a)

for m in str:
    if m =="Y":
        break
else:
    print("Символа Y  в строке", str, "нет")

print("--- Генераторы списков ---")

array = range(2,15)
print(array[2])

for n in array:
    print(n)

print("-------------------------")

array = [i for i in range(1,10)]
print(array)
array = [i*2 for i in range(1,10)]
print(array)
array = [i for i in range(1,10) if i%2 ==0]
print(array)


array = [1,2,3,4,5,6,7,8]
i=0
n=0
while n<8:
    i += 2
    array[n] = 1
    n+=1

print(array)