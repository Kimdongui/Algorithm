def partition(list):
    if len(list) < 2:
        return list
    middle = len(list) // 2
    left = list[:middle]
    right = list[middle:]
    left = partition(left)
    right = partition(right)
    return merge_sort(left, right)

def merge_sort(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

list = []
while(1):
    num = int(input("추가 할 숫자를 입력하세요(종료 : 0) : "))
    if num == 0:
        break
    else:
        list.append(num)

print(list)

print(partition(list))
