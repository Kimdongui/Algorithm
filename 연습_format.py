# 파이썬 포맷팅에는 두 가지 방법이 있다
# %연산자 와 format함수

print("integer: %d, string: %s, float: %f" % (100,"str",1.1))
# integer: 100, string: str, float: 1.1
print("Hi I am unlucky %s." % "dia")
# Hi I am unlucky dia.

# %연산자와 포맷 알파벳 사이에 숫자를 넣을 수도 있다.
# 숫자만큼 공간 확보 가능.

print("Hi I am unlucky %3s." % "dia")
print("Hi I am unlucky %5s." % "dia")
print("Hi I am unlucky %10s." % "dia")
print("Hi I am unlucky %13s." % "dia")

# Hi I am unlucky dia.
# Hi I am unlucky dia.
# Hi I am unlucky   dia.
# Hi I am unlucky        dia.
# Hi I am unlucky           dia.

# format 포맷팅은 {}괄호를 넣어서 사용한다.
# %와 동일한 기능을 지원하며, 변수의 타입과 ★상관없이★ 괄호와 숫자만 이용하면 된다.

print("integer: {}, string: {}, float: {}".format(100,"str",1.1))
# integer: 100, string: str, float: 1.1

# 보통 문자열 포맷팅에 성능은 "%포맷팅" > "format포맷팅"이다.
# %: 0.115
# format: 0.204
# 빠른 속도와 전달되는 인자의 타입을 정확히 알고 있다면 %포맷팅을 이용하면 좋고,
# 포맷 스트링을 사용하기 귀찮고 가독성이 좋은 코드를 쓰고 싶으면 format함수를 이용하면 좋다.

# 참고로 파이썬3.6 부터 f-string이라는 새로운 포맷팅 문법이 추가됐다.