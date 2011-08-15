'''Test cases for QVariant::Type converter'''
import unittest
from PySide.QtCore import *
from PySide.QtSql import *

from helper import unicodetype, bytestrtype, longtype

class QVariantTypeTest(unittest.TestCase):
    def testQVariantType(self):
        f = QSqlField("name", unicodetype())
        self.assertEqual(f.type(), unicodetype())

        f = QSqlField("name", bytestrtype())
        self.assertEqual(f.type(), unicodetype())

        f = QSqlField("name", "QString")
        self.assertEqual(f.type(), unicodetype())

        f = QSqlField("name", "double")
        self.assertEqual(f.type(), float)

        f = QSqlField("name", float)
        self.assertEqual(f.type(), float)

        f = QSqlField("name", int)
        self.assertEqual(f.type(), int)

        f = QSqlField("name", longtype())
        self.assertEqual(f.type(), int) # long isn't registered in QVariant:Type, just in QMetaType::Type

        #f = QSqlField("name", QObject)
        #self.assertEqual(f.type(), None)

        f = QSqlField("name", None)
        self.assertEqual(f.type(), None)

if __name__ == '__main__':
    unittest.main()
