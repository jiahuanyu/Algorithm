#include "FileUtil.h"

FileUtil::FileUtil()
{

}

char* FileUtil::ReadFile(const char* path, ios_base::openmode openmode)
{
	ifstream file(path, openmode);
	if (!file.is_open())
	{
		cerr << path << " open error!" << endl;
		return NULL;
	}

	file.seekg(0, ios::end);
	int size = file.tellg();

	char* buffer = new char[size];
	file.seekg(0, ios::beg);
	file.read(buffer, size);
	file.close();
	return buffer;
}

FileUtil::~FileUtil()
{

}
