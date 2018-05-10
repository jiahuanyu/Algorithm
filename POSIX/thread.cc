#include "thread.h"


Thread::Thread(runable r) {
  this->mRunable = r;
}

Thread::~Thread() {

}

bool Thread::start() {
  pthread_t pth;
  return pthread_create(&pth, NULL, this->mRunable, NULL);
}

int Thread::stop() {
  return pthread_cancel(pthread_self());
}

pthread_t Thread::getThreadID() {
  return pthread_self();
}
