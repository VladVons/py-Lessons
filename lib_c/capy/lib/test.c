#include <Python.h>


int a = 5;  
double b = 5.12345;
char c = 'X';


// Можно без args, но будет warning при компиляции.
static PyObject *
Hello(PyObject *self, PyObject *args) {
    puts("C Hello !");
    Py_RETURN_NONE;
}

// Получение значения переменной содержащей значение типа int и возврат его.
static PyObject *
GetInt(PyObject *self, PyObject *args) {
    int val;

    // Проверка кол-ва аргументов
    if (PyTuple_Size(args) != 1) {
        PyErr_SetString(self, "GetInt(). Args erros");
    }

    PyArg_ParseTuple(args, "i", &val);
    /* 
     * Альтернативный вариант.
     * 
    // Получаем аргумент
    PyObject *obj = PyTuple_GetItem(args, 0);
    // Проверяем его на тип int/long
    if (PyLong_Check(obj)) {
        PyErr_Print();
    }
    // Приводим (PyObject *) к int
    val = _PyLong_AsInt(obj);
     */
    printf("C GetInt(): %d\n", val);
    return Py_BuildValue("i", val);
}

//Получение значения переменной содержащей значение типа double и возврат его.
static PyObject *
GetDouble(PyObject *self, PyObject *args) {
    double val;

    if (PyTuple_Size(args) != 1) {
        PyErr_SetString(self, "GetDouble(). Args error");
    }

    PyArg_ParseTuple(args, "d", &val);

    printf("C GetDouble(): %f\n", val);
    return Py_BuildValue("f", val);
}

// Получение string и возврат его.
static PyObject *
GetStr(PyObject *self, PyObject *args) {
    char *val;

    if (PyTuple_Size(args) != 1) {
        PyErr_SetString(self, "GetStr(). Args error");
    }

    PyArg_ParseTuple(args, "s", &val);
    /* 
     * Альтернативный вариант.
     * 
    PyObject *obj = PyTuple_GetItem(args, 0);

    PyObject* pResultRepr = PyObject_Repr(obj);
    val = PyBytes_AS_STRING(PyUnicode_AsEncodedString(pResultRepr, "utf-8", "ERROR"));
     */
    printf("C GetStr(): %s\n", val);
    return Py_BuildValue("s", val);
}

// Получение значения переменных содержащих значения типа int, double, char *.
static PyObject *
GetMany(PyObject *self, PyObject *args) {
    int val1;
    double val2;
    char *val3;

    if (PyTuple_Size(args) != 3) {
        PyErr_SetString(self, "GetMany(). args error");
    }

    PyArg_ParseTuple(args, "ids", &val1, &val2, &val3);

    printf("C GetMany(): int - %d, double - %f, string - %s\n", val1, val2, val3);
    return Py_BuildValue("ifs", val1, val2, val3);
}


//----------------------
// Список функций модуля
static PyMethodDef methods[] = {
    {"Hello",     Hello,        METH_NOARGS,   "Hello descr"}, // Функция без аргументов
    {"GetInt",    GetInt,       METH_VARARGS,  "GetInt descr"}, // Функция с аргументами
    {"GetDouble", GetDouble,    METH_VARARGS,  "GetDouble descr"},
    {"GetStr",    GetStr,       METH_VARARGS,  "GetStr descr"},
    {"GetMany",   GetMany,      METH_VARARGS,  "GetMany descr"},
    {NULL, NULL, 0, NULL}
};

// Описание модуля
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "MyLib", "Test module", -1, methods
};

// Инициализация модуля
PyMODINIT_FUNC 
PyInit_MyLib(void) {
    PyObject *mod = PyModule_Create(&module);

    // Добавляем глобальные переменные
    PyModule_AddObject(mod, "a", PyLong_FromLong(a)); // int
    PyModule_AddObject(mod, "b", PyFloat_FromDouble(b)); // double
    PyModule_AddObject(mod, "c", Py_BuildValue("b", c)); // char

    return mod;
}
