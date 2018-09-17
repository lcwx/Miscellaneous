#include "C:\ProgramData\Anaconda3\include\Python.h"
#include <iostream>
using namespace std;

int main()
{
	// 初始化
	Py_Initialize();
	// 将Python工作路径切换到待调用模块所在目录，一定要保证路径名的正确性
	string path = "C:/Users/28012/Desktop/Statistical Learning/naive Bayes/python module/test6";
	string chdir_cmd = string("sys.path.append(\"") + path + "\")";
	const char* cstr_cmd = chdir_cmd.c_str();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString(cstr_cmd);

	// 加载模块
	//模块名，不是文件名
	PyObject* moduleName = PyBytes_FromString("test");
	PyObject* pModule = PyImport_Import(moduleName);

	if (!pModule) {
		cout << "[ERROR] Python get module failed." << endl;
		return 0;
	}
	cout << "[INFO] Python get module succeed." << endl;

	// 加载函数
	PyObject* pv = PyObject_GetAttrString(pModule, "test_add");
	// 验证是否加载成功
	if (!pv || !PyCallable_Check(pv)) {
		cout << "[ERROR] Can't find funftion (test_add)" << endl;
		return 0;
	}
	cout << "[INFO] Get function (test_add) succeed." << endl;

	// 设置参数
	// 2个参数
	PyObject* args = PyTuple_New(2);
	// 参数一设为4
	PyObject* arg1 = PyLong_FromLong(4);
	// 参数二设为3
	PyObject* arg2 = PyLong_FromLong(3);
	PyTuple_SetItem(args, 0, arg1);
	PyTuple_SetItem(args, 1, arg2);

	// 调用函数
	PyObject* pRet = PyObject_CallObject(pv, args);

	// 获取参数 
	// 验证是否调用成功
	if (pRet) {
		long result = PyLong_AsLong(pRet);
		cout << "result:" << result;
	}
	//释放资源
	Py_Finalize();

	return 0;
}
