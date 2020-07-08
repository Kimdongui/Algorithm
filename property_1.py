class Cal(object):
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
c1 = Cal(10,10)
print(c1.add())
print(c1.subtract())
c1.setV1('one')
c1.v2 = 30
print(c1.add())
print(c1.subtract())

# 파이썬은 c1.v2 = 30 과 같은 직접접근을 허용하나, 좋은 방법은 아니다.
# 메소드를 만들어서 사용하는 것을 권장한다.
# 이유는 직접접근 시에 어떤 문제로 에러가 날 수도 있기 때문이다.
# 그래서 메소드를 만들 때 기능을 추가하여(ex.정수가 아니면 거른다)
# 좀 더 고차원적인 처리를 통해 에러가 발생하지 않도록 한다.
