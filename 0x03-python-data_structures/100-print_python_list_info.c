#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print a python list's info
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyTypeObject *type;

	printf("[*] Size of the Python List = ");
	printf("%zd\n", ((PyVarObject*)(p))->ob_size);

	printf("[*] Allocated = %zd\n",  ((PyListObject*)(p))->allocated);

	for (i = 0; i < ((PyVarObject*)(p))->ob_size; i++)
	{
		type = Py_TYPE(PyList_GetItem(p, i));
		printf("Element %d: %s\n", i, type->tp_name);
	}
}
