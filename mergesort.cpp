#include <stdio.h>
void mergeSort(int data[], int p, int r);
void merge(int data[], int p, int q, int r);
#define size 8

int main() 
{
	int data[size], i,a;
	for (i = 0; i < size; i++)
	{
		printf("The number is : ");
		scanf_s("%d", &data[i]);
	}
	for (i = 0; i < 8; i++) 
		printf("%d ", data[i]);
	
	mergeSort(data, 0, 7);
	for (i = 0; i < 8; i++) 
		printf("%d ", data[i]);
	
	scanf_s("%d", &a);
	return 0;
}
void mergeSort(int data[], int p, int r) {
	int q;
	if (p < r) {
		q = (p + r) / 2;
		mergeSort(data, p, q);
		mergeSort(data, q + 1, r);
		merge(data, p, q, r);
	}
}
void merge(int data[], int p, int q, int r) {
	int i = p, j = q + 1, k = p;
	int tmp[size]; // »õ ¹è¿­
	while (i <= q && j <= r) 
	{
		if (data[i] <= data[j]) 
			tmp[k++] = data[i++];
		else tmp[k++] = data[j++];
	}
	while (i <= q) tmp[k++] = data[i++];
	while (j <= r) tmp[k++] = data[j++];
	for (int a = p; a <= r; a++) data[a] = tmp[a];
}
