#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/syscall.h>
#include <sys/time.h>
#include <unistd.h>

int main (int argc, char ** argv) {
  int i, r, n;

  n = atoi(argv[1]);
  char *text = argv[2];

  FILE *f = fopen("/dev/null", "w");

  struct timeval stop, start;
  gettimeofday(&start, NULL);

  for(i = 0 ; i < n; i++){
    syscall(SYS_write,fileno(f), text, strlen(text));
  }

  gettimeofday(&stop, NULL);
  printf("write %d %luus\n", n, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);

  fclose(f);
  return 0;
}