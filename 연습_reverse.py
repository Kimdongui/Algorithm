a = [1,2,3,4,5]
b = [2,3,4,5,6]

print("a =",a[::-1])    # Okay.

b.reverse   # 안됨
print("b =",b)

bb = b.reverse  # 이 것도 안됨
print("bb =",bb)

list(reversed(b))   #이 것도 안됨
print("b =",b)

bbb = list(reversed(b))     # Okay.
print("bbb=",bbb)