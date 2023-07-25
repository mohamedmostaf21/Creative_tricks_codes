#include <stdio.h>
#include <stdlib.h>

int nomain();

void _start(){
   nomain();
   exit(0);
}

int nomain(){
   printf("hello in c program without main");
   return 0;
}