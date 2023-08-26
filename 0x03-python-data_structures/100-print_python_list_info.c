#include <Python.h>
void print_python_list_info(PyObject *p)
{
	int s, alloc, j;
	PyObject *objs;

	s = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", alloc);

	for (j = 0; j < s; j++)
	{
		printf("Element %d: ", j);

		objs = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(objs)->tp_name);
	}
}
