#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <unistd.h>

int main(int args, char **argv) {

  int i, n, pages;

  n = atoi(argv[1]);
  pages = atoi(argv[2]);
  size_t pagesize = getpagesize();
  
  struct timeval stop, start;
  gettimeofday(&start, NULL);
  
  for(i = 0 ; i < n; i++){
    char* region = mmap(
      (void*) pagesize,
      pages * pagesize,
      PROT_READ|PROT_WRITE|PROT_EXEC,
      MAP_ANON|MAP_PRIVATE,
      0,
      0
    );
    munmap(region, pages * pagesize);
  }

  gettimeofday(&stop, NULL);
  printf("mmap_munmap %d %d %luus\n", n, pages, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);

  return 0;
}