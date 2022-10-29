// VladVons

#include <Python.h>
#include <dirent.h>


void ListDir(const char *aName, int aDepth)
{
    DIR *dir;
    struct dirent *Entry;

    if (!(dir = opendir(aName)))
        return;

    while ((Entry = readdir(dir)) != NULL) {
        if (Entry->d_type == DT_DIR) {
            char path[1024];
            if (strcmp(Entry->d_name, ".") == 0 || strcmp(Entry->d_name, "..") == 0)
                continue;

            snprintf(path, sizeof(path), "%s/%s", aName, Entry->d_name);
            printf("%*s[%s]\n", aDepth, "", Entry->d_name);
            ListDir(path, aDepth + 1);
        } else {
            printf("%*s %s\n", aDepth, "", Entry->d_name);
        }
    }
    closedir(dir);
}

static PyObject *
GetFiles(PyObject *self, PyObject *args) {
    char *val; 

    if (PyTuple_Size(args) != 1) {
        PyErr_SetString(self, "GetFiles(). Args error");
    }

    PyArg_ParseTuple(args, "s", &val);

    ListDir(val, 0);
    return Py_BuildValue("i", 0);
}


//----------------------
static PyMethodDef methods[] = {
    {"GetFiles",  GetFiles,     METH_VARARGS,  "Get files in directory"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "FS", "Test module", -1, methods
};

PyMODINIT_FUNC
PyInit_FS(void) {
    PyObject *mod = PyModule_Create(&module);
    return mod;
}
