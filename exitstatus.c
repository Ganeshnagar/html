#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() 
{
    pid_t pid;
    int status;

   
    pid = fork();
    if (pid < 0)
 {
       printf ("fork failed");
        exit(1);
    }

    if (pid == 0) 
    {       
        
        printf("Child: Performing some task...\n");
        sleep(2); // Sleep for 2 seconds
        exit(42); // Exit with status 42
    } 
   else 
       { 
        
        waitpid(pid, &status, 0);// Wait for the child process to terminate

        if (WIFEXITED(status)) // Check if the child terminated normally
         {
            int exit_status = WEXITSTATUS(status);
            printf("Parent: Child terminated with exit status %d\n", exit_status);
        } 
         else 
         {
            printf("Parent: Child did not terminate normally.\n");
        }
    }

    return 0;
}