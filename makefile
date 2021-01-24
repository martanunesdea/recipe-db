CC = clang++
CFLAGS = -Wall -std=c++11
main: main.o file_io.o record.o
	$(CC) $(CFLAGS) -o main main.o file_io.o record.o
main.o: main.cpp file_io.hpp record.hpp
	$(CC) $(CFLAGS) -c main.cpp
file_io.o:
	$(CC) $(CFLAGS) -c file_io.cpp
record.o:
	$(CC) $(CFLAGS) -c record.cpp

clean:
	rm -f *.o *.h.gch main