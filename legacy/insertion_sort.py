def insertion(array):
	print(array)

	for i in range(1,len(array)):
		temp = array[i]
		j = i-1
		while array[j]>temp and j>=0:
			array[j+1] = array[j]
			j-=1

		array[j+1] = temp
	print(array)
  
  
  array = [5,1,7,2,11,13]
  insertion(array)
