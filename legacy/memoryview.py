# 외부의 자료를 읽어들일 때 메모리에 복사 저장하는 것이 아닌
# 중간 단계인 버퍼에 저장 한다.
# 형식은 bytes, bytearray 형식만 지원한다.
# 많은 자원을 소모하는 데이터 복사에 비해
# 속도가 빠르다.

a = 'A'.encode() * 1000
b = bytearray(a)
# b = bytes(a)
buff_b = memoryview(b)

buff_b[999] = 66

print(b)


v = memoryview(b'abcdefg')
print(v.readonly)
# 메모리가 읽기 전용인지 여부의 불리안

print(b.nbytes)
# 총 바이트 수, = len(memoryview.tobytes())

print(v.format)
# format이 struct 모듈의 네이티브 형식 지정자인 경우
# 올바른 형으로 하나의 요소를 돌려준다.

print(v.obj)
# 메모리 뷰의 원본 객체
# 원본 객체 obj는 버퍼 프로토콜을 지원하는 자료형이어야 한다.

print(v.tobytes())
# 메모리 버퍼의 데이터를 바이트 문자열로 반환한다. = bytes()

print(v.tolist())
# 메모리 버퍼의 데이터를 리스트로 반환한다. = list()
