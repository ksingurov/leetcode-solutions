all: runme testme

runme: main.cpp solution.cpp
	g++ -std=c++17 -Wall main.cpp solution.cpp -o runme

testme: tests.cpp solution.cpp
	g++ -std=c++17 -Wall tests.cpp solution.cpp -o testme

clean:
	rm -f runme testme
