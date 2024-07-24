#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>

#define MAX 80
#define PORT 8080
#define SA struct sockaddr

void func(int sockfd)
{
    char buff[MAX];
    int n;

    struct timeval stop, start;
    gettimeofday(&start, NULL);
    while (1) {
        bzero(buff, MAX);

        recv(sockfd, buff, sizeof(buff), 0);
        // puts(buff);
        if (strncmp("exit", buff, 4) == 0) {
            break;
        }
    }
    gettimeofday(&stop, NULL);
    printf("recv %luus\n", (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);
}

int main()
{
    int sockfd, connfd, len;
    struct sockaddr_in servaddr, cli;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) {
        printf("socket bind failed...\n");
        exit(0);
    }
    
    if ((listen(sockfd, 5)) != 0) {
        printf("Listen failed...\n");
        exit(0);
    }
    len = sizeof(cli);

    connfd = accept(sockfd, (SA*)&cli, &len);
    if (connfd < 0) {
        printf("server acccept failed...\n");
        exit(0);
    }

    func(connfd);
    close(sockfd);
}
