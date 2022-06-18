mydict = dict()
print(mydict)
mydict = {'Name': 'John', 'Age' : 27}
print(mydict)

mydict = dict(Name = 'John', Age = 35, isMale = True)
print(mydict)

print(mydict["Age"])

print("______________")

for key in mydict:
    print('key','=',mydict[key])

mytiple = ('Name', 'Age', 'isMale')
for key in mytiple:
    print(key, '=', mytiple[key])

print("___________________")


#mydict = [i * 2 , i for i in range(1, 10)]
print(mydict)
mydict = (str(i*2) , i for i in range(1, 10))
print(mydict)