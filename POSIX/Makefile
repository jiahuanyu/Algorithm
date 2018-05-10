thread_test: thread_test.o thread.o
	g++ -o $@ $^

thread_test.o: thread_test.cc  thread.h
	g++ -c $<

thread.o: thread.cc thread.h
	g++ -c $<

clean:
	rm *.o
