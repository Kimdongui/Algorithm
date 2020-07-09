# open 함수
# 파일 읽기, 쓰기
# 읽기 모드 : r , 쓰기 모드 : w , 추가모드 : a
# 쓰기모드 : 기존 파일 삭제(기존 파일을 덮어버림)
# 추가모드 : 파일 생성 또는 추가
#  .. : 상대경로     . : 절대 경로

# 파일 읽기(파일이 존재하지 않을 경우 filenotfounderror)
# f = open('./resource/review.txt','r')
# content = f.read() # 파일 전체를 문자열로 돌려줌
# print(content)
# print(dir(f))
# f. close   ## 오류가 발생

# f = open('./resource/review.txt','w')
# print(dir(f))
# f.close

# close문을 생략해도 되는 with
# with open('./resource/review1.txt','r') as f:
#     c = f.read()
#     print(c)
#     print(list(c))

# read, strip, replace, readline 등 읽어올 수 있는 방법 다양


# with open('./resource/review1.txt','r') as f:
#     content = f.read()
#     print(">", content)
#     content = f.read()
#     print(">", content) # 한 번 끝까지 읽으면 컴퓨터 상 커서가 가장 아래에 있기 때문에 두번 읽지 않음


# # 한 문장 단위로 추출
# with open('./resource/review1.txt','r') as f:
#     line = f.readline()
#     while line:
#         print(line, end= '////')
#         line = f.readline()


# with open('./resource/review1.txt','r') as f:
#     contents = f.readlines() # readlines()로 파일을 읽으면 한 줄, 한 줄이 각각 리스트의 원소
#     print(contents)
#     for c in contents:
#         print(c,end = ' **** ')


# # 파일 쓰기
# with open('./resource/text1.txt','w') as f:
#     f.write('niceman\n')


# with open('./resource/text1.txt','a') as f:
#     f.write('goodman')
    
# # writelines : 리스트 -> 파일로 저장하는 형태
# with open('./resource/text2.txt','w') as f:
#     list = ['kim','park\n','cho']
#     f.writelines(list)


# with open('./resource/text4.txt','w') as f:
#     print('Test Contests1!',file=f)
#     print('Test Contests2!',file=f)

