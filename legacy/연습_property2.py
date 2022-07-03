# class Test:
    
#     def __init__(self):
#         self.color = "red"

#     def set_color(self,clr):
#         self.color = clr

#     def get_color(self):
#         return self.color

# if __name__ == '__main__':  # <이거는 왜 쓰는지 모르겟음>

#     t = Test()
#     t.set_color("blue")

#     print(t.get_color())

# 위에꺼랑 밑에꺼랑 같은 것임.

class Test:
    
    def __init__(self):
        self.__color = "red"

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self,clr):
        self.__color = clr

t = Test()
t.color = "blue"

print(t.color)


# 1. 변수를 변경 할 때 어떠한 제한을 두고 싶어서
# 2. get,set 함수를 만들지 않고 더 간단하게 접근하게 하기 위해서
# 3. 하위호환성에 도움이 됨.


# 출처: https://hamait.tistory.com/827 [HAMA 블로그]
