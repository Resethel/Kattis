// Using C
// https://open.kattis.com/problems/sibice

#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{

  int N, width, height, length;
  scanf("%d %d %d", &N, &width, &height);

  for ( int i = 0 ; i < N ; i++ )
  {
    scanf("%d", &length);

    if (length <= width || length <= height || length <= sqrt(width*width + height*height))
    {
      printf("DA\n");
    }
    else
    {
      printf("NE\n");
    }
  }
}
