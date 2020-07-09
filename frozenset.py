li = frozenset([1,2,3,4])
tp = frozenset((1,2,3,4))
st = frozenset({1,2,3,4})
di = frozenset({1:"일",2:"이",3:"삼",4:"사"})


print(type(frozenset))

print(li)
print(tp)
print(st)
print(di)

#insert/delete가 불가능
#Load/Search만 가능