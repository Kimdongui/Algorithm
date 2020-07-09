print(callable(list))


def rucallable():
    return 666



print(callable(list))
print(callable(rucallable))
print(callable(55))

print(dir(rucallable))

#__call__ attribute가 있으면 호출이 가능하다고 판단
#없다면 호출 할 수 없음