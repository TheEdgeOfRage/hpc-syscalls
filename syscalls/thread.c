#include <pthread.h>
#include <stdio.h> 
#include <stdlib.h> 
#include <sys/time.h>
#include <unistd.h>

void *threadFun(void *vargp) { 
  return NULL;
}

int main(int argc, char ** argv) {
  pthread_t thread_id;
  int i, n;
  n = atoi(argv[1]);

  struct timeval stop, start;
  gettimeofday(&start, NULL);

  for(i = 0; i < n; i++) {
    pthread_create(&thread_id, NULL, threadFun, NULL);
    pthread_join(thread_id, NULL);
  }

  gettimeofday(&stop, NULL);
  printf("thread %d %luus\n", n, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);

  return(0);
}
