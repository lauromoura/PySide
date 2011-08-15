import unittest
import os
from helper import UsesQApplication, makeunicode

from PySide.QtGui import *
from PySide.QtUiTools import *

def get_file_path():
    for path in file_path:
        if os.path.exists(path):
            return path
    return ""

class QUioaderTeste(UsesQApplication):

    def run_test_load_file(self, filename):
        loader = QUiLoader()
        parent = QWidget()
        w = loader.load(filename, parent)
        self.assertNotEqual(w, None)

        self.assertEqual(len(parent.children()), 1)

        child = w.findChild(QWidget, "child_object")
        self.assertNotEqual(child, None)
        self.assertEqual(w.findChild(QWidget, "grandson_object"), child.findChild(QWidget, "grandson_object"))



    def testLoadFile(self):
        filePath = os.path.join(os.path.dirname(__file__), 'test.ui')
        self.run_test_load_file(filePath)

    def testLoadFileUnicodeFilePath(self):
        filePath = makeunicode(os.path.join(os.path.dirname(__file__), 'test.ui'))
        self.run_test_load_file(filePath)

if __name__ == '__main__':
    unittest.main()

