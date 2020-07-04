# 내장 함수 zip
# zip은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.

A = [1,2,3,4]
B = ["a","b","c","d"]

AB = list(zip(A,B))

print(AB,end = "\n\n\n\n")

# 위와 같이 A,B 리스트에 갯수가 같다면 zip 을 이용하여 하나의 연관된 리스트로 묶을 수 있다.

dic = {}
for i in range(len(A)):
    dic[A[i]] = B[i]

print(dic,end = "\n\n\n\n")

# 딕셔너리를 zip 함수를 사용하지 않고 만들 때 위와 같이 이용한다.

ABdic = dict(zip(A,B))
print(ABdic,end = "\n\n\n\n")

# zip 함수를 이용한다면 위와 같이 간단하게 표현될 수 있다.

C = [4,5,6]
ABC = list(zip(A,B,C))
print(ABC,end = "\n\n\n\n")

# 위와 같이 문자, 숫자형 관계없이 여러개의 리스트도 묶을 수 있다.

