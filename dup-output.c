#include<stdio.h>
#include<fcntl.h>
#include<unistd.h>
int main()
{
    int fd;
    fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if(dup2(fd,STDOUT_FILENO)<0){
        printf("\n Erros in dup 2.");
        close(fd);
        exit(1);
    }
    close(fd);
    printf("This output is redirected to output.txt.");
    return 0;
}