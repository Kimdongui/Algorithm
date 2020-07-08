# 외부에서 접근 가능한 변수를 파이썬은 property 라고 한다.
# 파이썬은 인스턴스 외부에서 접근이 가능하다.
# 그렇다면 그 접근을 막기 위해서는 어떻게 해야할까?
# __ 를 넣으면 된다. 즉, 인스턴스 외부에서 접근하는 것을 막는 방법은 __를 넣어서 만드는 것이다.

class C(object):
    def __init__(self, v):
        self.__value = v
    def show(self):
        print(self.__value)
c1 = C(10)
# print(c1.__value) # 여기서 에러가 나온다.
c1.show()

# 밑에는 접근이 됨

# class C(object):
#     def __init__(self, v):
#         self.value = v
#     def show(self):
#         print(self.value)
# c1 = C(10)
# print(c1.value)
# c1.show()
