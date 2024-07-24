#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <unistd.h>

int main(int args, char **argv)
{
    // printf("%d\n", getpid());
    
    int i, n;
    n = atoi(argv[1]);

    long pagesize = sysconf(_SC_PAGESIZE);

    struct timeval stop, start;
    gettimeofday(&start, NULL);
    for(i = 0; i < n; i++){
        unsigned char *p = malloc(pagesize + 1);
        // Page fault
        p[0] = 0;
    }

    gettimeofday(&stop, NULL);
    printf("page_fault %d %luus\n", n, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);

    // ps -o min_flt,maj_flt <pid>
    // sleep da bih mogla da pokrenem ps dok se ne ubije proces
    // sleep(30);

    return 0;
}