// Using C
// https://open.kattis.com/problems/speedlimit

#include <stdio.h>

int main(int argc, char *argv[])
{
  while (1)
  {
    int pairs;
    scanf("%d", &pairs);

    if (pairs < 0)
      break;

    long int result = 0;
    int prevHour = 0;
    for (int i = 0; i < pairs; i++)
    {
      int speed, hour;
      scanf("%d %d", &speed, &hour);
      result += (hour - prevHour) * speed;
      prevHour = hour;
    }
    printf("%ld miles\n", result);

    }

  return 0;
}
