#include <stdio.h>
#include <stdlib.h>
#include <sys/syscall.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h> 

int main (int argc, char ** argv)
{
  int i, n;
  n = atoi(argv[1]);

  struct timeval stop, start;
  gettimeofday(&start, NULL);
  
  // 2^n procesa
  for(i = 0; i < n; i++){
    syscall(SYS_fork);
  }
  gettimeofday(&stop, NULL);

  printf("fork %d %luus\n", n, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);
  return 0;
}