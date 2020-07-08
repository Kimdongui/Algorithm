def divide(e, f):
    breakpoint()
    return f / e

a, b = 1, 2

print("check")
print(a,b)
breakpoint()
print(divide(a, b))


# breakpoint() 대신에 import pdb; pdb.set_trace() 도 가능.
# pdb : 파이썬 디버깅 도구로 파이썬 인터프리터를 줄마다 보면서 실행할 수 있도록 도와주는 도구.
# pdb에서는 일반적인 앱 중단점 실행 화면과 비슷하게 동작합니다. 다음으로 넘어가거나 콘솔 실행, 다음 줄 이동 등등의 명령어를 사용 가능합니다.
# c - continue로 다음에 설정 된 중단점으로 바로 이동
# n - 다음 줄로 이동 함
# r - 현재 함수가 return 될 때까지 계속 실행
# l - 현재 라인을 포함하여 위 아래로 11줄의 코드를 출력함
