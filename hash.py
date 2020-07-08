# hashvalue를 반환
# hashvalue는 딕셔너리 key에 사용
# 값 변경이 불가능 한 immutable 객체에 사용 가능

#mutable

hash([1,2,3]) # list

hash({'a','b'}) # set

hash({'a':1,'b':2}) #dict

#immutable

hash(500) # int 값과 해쉬 값이 같다.

hash(99999999999999999999999999999999999999)
# int 18자리를 벗어나면 값과 다른 해쉬값을 리턴 한다.

hash(3.5) # float 값과 해쉬값이 다르다.

hash(5+3j) # complex 값과 해쉬값이 다르다.

hash(1)
hash(1.0) # 1과 1.0 값이 같다

print(dir(hash))
