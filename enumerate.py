l = [1, 5, 7, 33, 39, 52]
t = (1, 5, 7, 33, 39, 52)

print(list(enumerate(l)))
print(tuple(enumerate(l)))
print(list(enumerate(t)))
print(tuple(enumerate(t)))

for i in enumerate(t):
    print(i)

for i, v in enumerate(t):
    print("index : {}, value: {}".format(i,v))

# 객체를 열거하여 돌려준다. 순서를 넣어서 돌려준다.
