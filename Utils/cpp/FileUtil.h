#ifndef __FILE_UTIL_H__
#define __FILE_UTIL_H__

#include <fstream>
using namespace std;

class FileUtil
{
public:
	FileUtil();
	~FileUtil();
	// 读取文件内容
	char* ReadFile(const char*, ios_base::openmode);
};

#endif
