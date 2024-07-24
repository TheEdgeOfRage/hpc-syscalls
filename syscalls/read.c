#include <stdio.h>
#include <stdlib.h>
#include <sys/syscall.h>
#include <sys/time.h>
#include <unistd.h>

int main (int argc, char ** argv) {
  int i, r, n;
  char c;

  n = atoi(argv[1]);
  
  struct timeval stop, start;
  gettimeofday(&start, NULL);

  FILE *f = fopen("/dev/zero", "r");
  for(i = 0 ; i < n; i++){
    syscall(SYS_read,fileno(f), &c, 1);
  }

  gettimeofday(&stop, NULL);
  printf("read %d %luus\n", n, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);
  
  fclose(f);
  
  return 0;
}