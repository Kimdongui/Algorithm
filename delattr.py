# 파이썬 내장함수 정리하기
# 파이썬은 객체 지향 언어이다.
# 특정 함수들 처럼 어떤 기능을 함수코드에 묶어 두는 것이 아니라, 그런 기능을 묶은 하나의 단일 프로그램을 객체라고 하는 코드에 넣어 
# 다른 프로그래머가 재사용할 수 있도록 하는 것
# 객체(object), 클래스(class)
# 클래스라는 붕어빵틀을 이용하여 만들어내는 인스턴스를 '객체'라고 한다.
# 객체는 실생활에 존재하는 실제적인 물건 or 개념을 뜻하며, 속성 attritute 와 행동 action 으로 구성된다.


# delattr(object,name)
# 객체에 포함되어 있는 속성을 제거해주는 내장함수 중 한 가지이다.


class sample():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Pt(self):
        z = self.x + self.y
        return z

a = sample(1,2)

print(a.Pt())

# delattr(a,'x')
# del a.x
# print(a.Pt())

# delattr(a,'y')
# print(a.Pt())

class sample2():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sum(self):
        return self.x + self.y
    def minus(self):
        return self.y - self.z 

b = sample2(10,20,30)
delattr(b,'z')
print(b.sum())
print(b.minus())

# setattr() - object의 속성(attribute) 값을 설정하는 함수

# getattr() - object의 속성(attribute) 값을 확인하는 함수

# delattr() - object의 속성(attribute)을 제거하는 함수

# hasattr() - object의 속성(attribute) 존재를 확인하는 함수