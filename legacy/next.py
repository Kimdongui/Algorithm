next_list = [1,2,3,4,5]
next_tuple = (1,2,3,4,5)
next_dict = {1:"첫번째",2:"두번째",3:"세번째",4:"네번째",5:"다섯번째"}

print(dir(list)) # list객체의 내장 메서드 아래는 그 결과
has_list_iter = ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__'
, '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', 
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__'
, '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(dir(range)) # range객체의 내장 메서드 아래는 그 결과
has_range_iter = ['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
 '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
print(dir(tuple)) # tuple객체의 내장 메서드 아래는 그 결과
has_tuple_iter = ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 
'index']
print(dir(dict)) # dictionary객체의 내장 메서드 아래는 그 결과
has_dict_iter = ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear',
  'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

if '__iter__' in has_list_iter:
    print("List has an iter")
if '__iter__' in has_range_iter:
    print("Range has an iter")
if '__iter__' in has_tuple_iter:
    print("Tuple has an iter")
if '__iter__' in has_dict_iter:
    print("Dictionary has an iter")
# 네가지 객체 모두 iter를 가지고 있음

now = iter(next_list)
print(next(now))
now = iter(next_tuple)
print(next(now))
now = iter(next_dict)
print(next(now))
now = iter(range(5))
print(next(now)) # 0
# 리스트,튜플,딕셔너리,튜플 모두 iter를 가지고 있으며 iter함수로 변환한 뒤 next함수를 통해 호출 -> 각 원소의 첫번째값(딕셔너리는 키값기준)

print(next(now)) # 1
print(next(now)) # 2
# 마지막에담긴 iter객체(Range(5))를 기준으로 다음값을 계속꺼내다가

print(next(now)) # 3
print(next(now)) # 4
print(next(now)) # 5-> 에러발생
# 더이상 꺼낼 값이 없다면 StopIteration를 발생

