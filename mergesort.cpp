#include <stdio.h>
void mergeSort(int data[], int left, int right);
void merge(int data[], int left, int mid, int right);
#define size 8

int main()
{
	int data[size], i, a;
	for (i = 0; i < size; i++)
	{
		printf("The number is : ");
		scanf_s("%d", &data[i]);
	}
	for (i = 0; i < 8; i++)
		printf("%d ", data[i]);
	printf("\n");
	mergeSort(data, 0, 7);
	for (i = 0; i < 8; i++)
		printf("%d ", data[i]);

	scanf_s("%d", &a);
	return 0;
}
void mergeSort(int data[], int left, int right) 
{
	int mid;
	if (left < right) 
	{
		mid = (left + right) / 2;
		mergeSort(data, left, mid);
		mergeSort(data, mid + 1, right);
		merge(data, left, mid, right);
	}
}
void merge(int data[], int left, int mid, int right) 
{
	int i = left, j = mid + 1, k = left;
	int tmp[size];
	while (i <= mid && j <= right)
	{
		if (data[i] <= data[j])
			tmp[k++] = data[i++];
		else tmp[k++] = data[j++];
	}
	while (i <= mid) 
		tmp[k++] = data[i++];
	while (j <= right) 
		tmp[k++] = data[j++];
	for (int a = left; a <= right; a++) 
		data[a] = tmp[a];
}