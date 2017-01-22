#include <stdio.h>
#include <unistd.h>
#include "thread.h"
Thread *mLogThread;
void *log(void *str) {
    // pthread_cleanup_push(mLogThread->getRelease(),NULL);
    pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, NULL); //允许退出线程
    pthread_setcanceltype(PTHREAD_CANCEL_ASYNCHRONOUS, NULL); //设置立即取消
    int i;
    for(i = 0; i < 10; i ++) {
      printf("This is in the thread: %d\n",i);
    }
    while(1) {
      pthread_testcancel();
      printf("XXXXXXX: %d\n",i);
      pthread_testcancel();
      sleep(2);
    }
    // pthread_cleanup_pop(0);
    return NULL;
}


int main(int argc, char *argv[]) {
  void *ret=NULL;
  mLogThread = new Thread(log);
  mLogThread->start();
  sleep(1);
  printf("canceld = %d\n",mLogThread->stop());
  printf("Before of Main\n");
  pthread_join(mLogThread->getThreadID(), &ret);
  printf("End of Main\n");
  return 0;
}
