#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <unistd.h>

#define MAX 80
#define PORT 8080
#define SA struct sockaddr

void func(int sockfd, int n, char *text)
{
    char buff[MAX];
    int i;

    struct timeval stop, start;
    gettimeofday(&start, NULL);

    for (i = 0; i < n; i++) {
        bzero(buff, sizeof(buff));

        strcpy(buff,text);
        send(sockfd, buff, sizeof(buff), 0);
    }
    strcpy(buff,"exit");
    send(sockfd, buff, sizeof(buff), 0);

    gettimeofday(&stop, NULL);
    printf("send %d %s %luus\n", n, text, (stop.tv_sec - start.tv_sec) * 1000000 + stop.tv_usec - start.tv_usec);
}

int main(int argc, char ** argv)
{
    int sockfd, connfd;
    struct sockaddr_in servaddr, cli;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(PORT);

    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) {
        printf("connection with the server failed...\n");
        exit(0);
    }
    
    int n = atoi(argv[1]);
    char *text = argv[2];
    func(sockfd, n, text);

    close(sockfd);
}
