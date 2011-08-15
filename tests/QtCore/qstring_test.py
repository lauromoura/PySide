#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Test cases for QString'''

import unittest
import ctypes
import sys

from PySide.QtCore import *
from helper import makeunicode

class QStringConstructor(unittest.TestCase):
    '''Test case for QString constructors'''

    def testQStringDefault(self):
        obj = QObject()
        obj.setObjectName('foo')
        self.assertEqual(obj.objectName(), makeunicode('foo'))
        obj.setObjectName(makeunicode('áâãà'))
        self.assertEqual(obj.objectName(), makeunicode('áâãà'))
        obj.setObjectName(None)
        self.assertEqual(obj.objectName(), makeunicode(''))

if __name__ == '__main__':
    unittest.main()
