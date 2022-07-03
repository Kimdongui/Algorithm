#include <stdio.h>
int main(void)
{
	int i, n;
	int factorial = 1;
	printf("숫자를 입력하시오 : ");
	scanf_s("%d", &n);

	if (n == 1)
		printf("This number factorial is 0\n");
	else
	{
		for (i = 1; i <= n; i++)
		{
			printf("number list is %d\n", i);
			factorial = factorial * i;
		}
		printf("This number factorial is %d\n", factorial);

	}
	return 0;
}