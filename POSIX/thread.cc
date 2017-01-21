#include "thread.h"


Thread::Thread(runable r) {
  mPthread_t = new pthread_t();
  this->mRunable = r;
}

Thread::~Thread() {
  delete this->mPthread_t;
}

void Thread::start() {
  pthread_create(mPthread_t, NULL, this->mRunable, NULL);
}

void Thread::stop() {

}


pthread_t *Thread::getThreadID() {
  return this->mPthread_t;
}
