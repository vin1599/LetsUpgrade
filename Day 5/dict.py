dict1 = {}
x = int(input("enter the number: "))
for i in range(1, x+1):
    dict2 = {i:i*i}
    dict1.update(dict2)
print(dict1)
