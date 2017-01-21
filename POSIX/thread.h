#include <pthread.h>
#include <stdio.h>

typedef void *(*runable)(void*);

class Thread {
  private:
    runable mRunable;
    pthread_t *mPthread_t;
  public:
    Thread(runable);
    ~Thread();
    pthread_t *getThreadID();
    void start();
    void stop();
};
