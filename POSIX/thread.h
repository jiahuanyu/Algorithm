#include <pthread.h>
#include <stdio.h>

typedef void *(*runable)(void *);

class Thread {
  private:
    runable mRunable;

  public:
    Thread(runable);
    ~Thread();
    pthread_t getThreadID();
    bool start();
    int stop();
};
