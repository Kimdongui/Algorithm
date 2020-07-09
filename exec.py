# exec(object[,globals[,locals]]
# 문자열로 표현된 파이썬 코드를 동적 실행을 지원
# object는 문자열 또는 코드 객체여야 한다.
# 문자열로 표현된 문을 인수로 받아 파이썬 컴파일 코드로 변환
a = 5
exec('a=a+4')
a

# exec()함수는 여러 개의 문으로 사용할 수 있다.
s = '''

a=1

if a > 0:

print('Success')

'''

print(exec(s))


# main함수의 지역변수로 선언된 a가 what_is_exec 함수에서 사용된다
# exec함수는 강제로 문자열 내부의 코드를 실행시키게 된다.
# 위 코드에서 what_is_eval함수를 호출하면 현재 스택에 있는 지역변수 a를 강제로 호출하게 된다.(물론 main 함수에서 a를 선언하지 않았다면 오류발생)
# 원래 what_is_exec 함수 안에서 다른 지역의 변수 a를 호출하면 오류가 발생해야 정상이다.
# exec함수를 잘못 사용하면 원했던 변수가 아닌 다른 변수에 접근할 수도 있게 된다.
# 해당 표현식을 그대로 실행하는 것이기 때문에 Command Injection Flaws가 그대로 노출될 수 있다. 이는 시스템 명령어를 삽입할 수 있는 언어 모두가 가지고 있는 취약점이기도 하다.
# 뿐만 아니라, 이 함수는 코드의 가독성을 떨어트리고 디버깅을 어렵게 만들 수 있다.
string1 = '''
if a != 0:
    print("'a' is ",a)
else:
    print("'a' is zero.")
'''

def what_is_exec():
    print('----------------------------------')
    print('this is code in what_is_exec')

    print('do "exec(string1)" in function : ')
    exec(string1)

if '__main__':
    a=20
    print('Local variables \'a\' is defined in \'__main__\'')
    print("Do \'print(a)\' : ",a)
    print('Let\'s run the \'what_is_exec\' function')
    what_is_exec()

# eval()은 파이썬 식을 인수로 받아 파이썬 컴파일 코드로 변환하여 실행하는것
a = 5
eval('a+4')
a


