#include<stdio.h>
#include<sys/stat.h>
#include<sys/types.h>
#include<unistd.h>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        printf("\n Invalid no of arguments");
        return 1;

    }
    struct stat st;
    if(stat(argv[1],&st)==-1)
    {
        printf("\n Error in stat");
        return 1;
    }

    if(S_ISDIR(st.st_mode))
    printf("\n Directory.\n");
    else if(S_ISCHR(st.st_mode))
    printf("\n Character device.\n");
    else if(S_ISBLK(st.st_mode))
    printf("\nBlock device.\n");
    else if(S_ISFIFO(st.st_mode))
    printf("\nFifo or pipe.\n");
    else if(S_ISLNK(st.st_mode))
    printf("\nSymbolic link\n");
    else if(S_ISSOCK(st.st_mode))
    printf("\nSocket \n");
    else 
    printf("\nUnknown file type.\n");
}