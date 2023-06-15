#include <Python.h>

/**
 * print_python_bytes - print a python list's info
 * @p: python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *obj = (PyBytesObject *) p;
	int size = 0, bytes, i;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	bytes = (size >= 10) ? 10 : size + 1;
	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", obj->ob_sval);
	printf("  first %d bytes: ", bytes);
	for (i = 0; i < bytes; i++)
	{
		printf("%02x", (unsigned char) obj->ob_sval[i]);
		if (i < bytes - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - print python object's bytes
 * @p: python object
 */
void print_python_list(PyObject *p)
{
	int i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = ");
	printf("%zd\n", ((PyVarObject *)(p))->ob_size);

	printf("[*] Allocated = %zd\n",  ((PyListObject *)(p))->allocated);

	for (i = 0; i < ((PyVarObject *)(p))->ob_size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
