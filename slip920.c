#include<stdio.h>
#include<sys/stat.h>
#include<unistd.h>
#include<sys/types.h>
int main(int argc,char * argv[])
{
if(argc != 2)
{
printf("\n Invalid no of argv\n");
return 1;
}
struct stat st;
if (stat(argv[1] ,&st)== -1)
{
printf("\n Erros in stat");
return 1;
}

if(S_ISREG(st.st_mode))
printf("\n Regual file\n");
else if(S_ISDIR(st.st_mode))
printf("\n Directory.\n");
else if(S_ISCHR(st.st_mode))
printf("\nCharacter file\n");
else if(S_ISBLK(st.st_mode))
printf("\n Block device.\n");
else if(S_ISFIFO(st.st_mode))
printf("\nPipe or fifo\n");
else if(S_ISLNK(st.st_mode))
printf("\nSymbolic link\n");
else if(S_ISSOCK(st.st_mode))
printf("\nSocket.\n");
else
printf("\nunknown file type.\n");
return 0;
}
