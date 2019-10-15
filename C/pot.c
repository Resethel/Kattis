// Using C
// https://open.kattis.com/problems/pot

#include <stdio.h>
#include <math.h>

int main()
{
    int N, number;
    long int result = 0;

    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
      scanf("%d", &number);
      result += pow(number/10, number % 10);
    }

    printf("%ld", &result);
}
