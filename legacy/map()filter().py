# map(함수명, 리스트명) 함수는 리스트값 하나하나를 함수명에 대입
before = ['2019', '12', '31']
after = list(map(int, before))
after
# [2019, 12, 31]
# int('2019'), int('12'), int('31')

def power(item):
    return item * item
def under_3(item):
    return item<3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("map()함수 결과")
print("map(power, list_input_a):", output_a)
# <map object>, 제네레이터
print("map(power, list_input_a):", list(output_a))

# filter(함수명, 리스트명)리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트를 구성해주는 함수
output_b = filter(under_3, list_input_a)
print("filter()함수 결과")
print("filter(under_3, output_b):", output_b)
# <filter object>, 제네레이터
print("filter(under_3, output_b):", list(output_b))