#include <stdio.h>

int factorial(int);

int main() {
	int n, res;
	printf("n입력 : ");
	scanf("%d", &n);
	res = factorial(n);
	printf("%d! = %d", n, res);
}

int factorial(int n) {
	int i, res;
	res = 1;
	if (n == 0)	
		res = 1;
	else
		for (i = n; i > 1; i--)
			res *= i;
	return res;
}
