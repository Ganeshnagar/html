#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>

int main()
{
    int fd[2];
    pipe(fd);

    // Block Ctrl-C (SIGINT) and Ctrl-\ (SIGQUIT)
    signal(SIGINT, SIG_IGN);
    signal(SIGQUIT, SIG_IGN);

    if (fork() == 0)
    {
        
        close(fd[0]);          
        dup2(fd[1], 1);        
        close(fd[1]);

        execlp("ls", "ls", "-l", NULL);
    }
    else
    {
        
        close(fd[1]);          
        dup2(fd[0], 0);       
        close(fd[0]);

        execlp("wc", "wc", "-l", NULL);
    }

    return 0;
}
