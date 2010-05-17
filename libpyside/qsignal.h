﻿#ifndef PYSIDE_SIGNAL_H
#define PYSIDE_SIGNAL_H

#include <pysidemacros.h>
#include <Python.h>
#include <QObject>

namespace PySide
{

typedef struct {
    PyObject_HEAD
    char* signalName;
    char* signature;
    PyObject* source;
    PyObject* next;
} SignalInstanceData;


extern "C"
{
    PyAPI_DATA(PyTypeObject) Signal_Type;
    PyAPI_DATA(PyTypeObject) SignalInstance_Type;
}; //extern "C"

PYSIDE_API PyAPI_FUNC(PyObject*) signalNew(const char* name, ...);
PYSIDE_API void signalUpdateSource(PyObject* source);

} //namespace PySide

#endif
