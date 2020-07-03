#런타임에 생성
#Return 문이 포함되지 않음


list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]


print(list(map(lambda x,y:x==y,list1,list2)))
# lambda arg1,arg2 ... : equation about args
# map("lambda function",arg1, arg2,...)


print(list(map(lambda x,y:x+y,list1,list2)))


# iterator method가 없으면 에러
# iter 개수가 가장 작은 인자 기준으로 출력
# (Ex, len(a) == 2,len(b) == 6,len(c) == 4) -> a의 개수가 가장적으므로 만큼만 적용

print(list(map(lambda x,y:x+y,list1,list2)))

dict1 = {1,2,3,4,5}
dict2 = {1,2,3,4,5}

print(list(map(lambda x,y:x+y,list1,list2)))
print(set(map(lambda x,y:x+y,dict1,list2))) # -> dictionary type과 list type이 호환됨

#객체의 type에 관계없이 mapping가능
#iter method만 있으면 관계없이 적용되는 것으로 보임
