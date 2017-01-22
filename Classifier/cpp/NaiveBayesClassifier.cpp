#include <iostream>
#include <fstream>
#include "../../Utils/cpp/FileUtil.cpp"
using namespace std;

int main(int argc, char const *argv[]) {
	FileUtil* fileUtil = new FileUtil();
	cout << fileUtil->ReadFile("./NaiveBayesClassifierData", ios::in);

	delete fileUtil;
	return 0;
}
