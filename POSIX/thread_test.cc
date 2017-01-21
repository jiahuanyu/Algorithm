#include <stdio.h>
#include <unistd.h>
#include "thread.h"

void *log(void *str) {
    int i;
    for(i = 0; i < 10; i ++) {
      printf("This is in the thread: %d\n",i);
    }
    return NULL;
}


int main(int argc, char *argv[]) {
  Thread *logThread = new Thread(log);
  logThread->start();
  pthread_join(*(logThread->getThreadID()), NULL);
  return 0;
}
