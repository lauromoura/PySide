
'''Helper classes and functions'''

import os
import sys
import unittest

from random import randint

from PySide.QtCore import QCoreApplication, QTimer

try:
    from PySide.QtGui import QApplication
except ImportError:
    has_gui = False
else:
    has_gui = True


# Helper functions during migration to python 2.3
PY3 = sys.version_info[0] == 3

def create_class(name, bases, attrs={}, meta=type):
    return meta(name, tuple(bases), attrs)

def makeunicode(value):
    '''Create an unicode string without the "u" prefix'''
    if PY3:
        return value
    else:
        return unicode(value, encoding='utf-8')

def unicodetype():
    '''Returns the type of unicode strings'''
    if PY3:
        return str
    else:
        return unicode

def bytestrtype():
    '''Returns the type of byte strings'''
    if PY3:
        return bytes
    else:
        return str

def makebytestr(value):
    '''Create an byte string'''
    if PY3:
        return bytes(value, encoding='utf-8')
    else:
        return str(value)

def makelong(value):
    if PY3:
        return value
    else:
        return long(value)

def islong(value):
    if PY3:
        return isinstance(value, int)
    else:
        return isinstance(value, long)

def longtype():
    if PY3:
        return int
    else:
        return long

def makeStringIO():
    if PY3:
        import io
        return io.StringIO()
    else:
        import cStringIO
        return cStringIO.StringIO()


def makeunichr(value):
    '''Create an unicode char'''
    if PY3:
        return chr(value)
    else:
        return unichr(value)

def isunicode(value):
    '''Is it an unicode string?'''
    if PY3:
        return isinstance(value, str)
    else:
        return isinstance(value, unicode)

def isbytestring(value):
    '''Is it an non-unicode string?'''
    if PY3:
        return isinstance(value, bytes)
    else:
        return isinstance(value, str)


# Other helper stuff

def adjust_filename(filename, orig_mod_filename):
    dirpath = os.path.dirname(os.path.abspath(orig_mod_filename))
    return os.path.join(dirpath, filename)

class NoQtGuiError(Exception):
    def __init__(self):
        Exception.__init__(self, 'No QtGui found')

class BasicPySlotCase(object):
    '''Base class that tests python slots and signal emissions.

    Python slots are defined as any callable passed to QObject.connect().
    '''
    def setUp(self):
        self.called = False

    def tearDown(self):
        try:
            del self.args
        except:
            pass

    def cb(self, *args):
        '''Simple callback with arbitrary arguments.

        The test function must setup the 'args' attribute with a sequence
        containing the arguments expected to be received by this slot.
        Currently only a single connection is supported.
        '''
        if tuple(self.args) == args:
            self.called = True
        else:
            raise ValueError('Invalid arguments for callback')


_instance = None
_timed_instance = None

if has_gui:
    class UsesQApplication(unittest.TestCase):
        '''Helper class to provide QApplication instances'''

        qapplication = True

        def setUp(self):
            '''Creates the QApplication instance'''

            # Simple way of making instance a singleton
            super(UsesQApplication, self).setUp()
            global _instance
            if _instance is None:
                _instance = QApplication([])

            self.app = _instance

        def tearDown(self):
            '''Deletes the reference owned by self'''
            del self.app
            super(UsesQApplication, self).tearDown()


    class TimedQApplication(unittest.TestCase):
        '''Helper class with timed QApplication exec loop'''

        def setUp(self, timeout=100):
            '''Setups this Application.

            timeout - timeout in milisseconds'''
            global _timed_instance
            if _timed_instance is None:
                _timed_instance = QApplication([])

            self.app = _timed_instance
            QTimer.singleShot(timeout, self.app.quit)

        def tearDown(self):
            '''Delete resources'''
            del self.app
else:
    class UsesQApplication(unittest.TestCase):
        def setUp(self):
            raise NoQtGuiError()
    class TimedQapplication(unittest.TestCase):
        def setUp(self):
            raise NoQtGuiError()


_core_instance = None

class UsesQCoreApplication(unittest.TestCase):
    '''Helper class for test cases that require an QCoreApplication
    Just connect or call self.exit_app_cb. When called, will ask
    self.app to exit.
    '''

    def setUp(self):
        '''Set up resources'''

        global _core_instance
        if _core_instance is None:
            _core_instance = QCoreApplication([])

        self.app = _core_instance

    def tearDown(self):
        '''Release resources'''
        del self.app

    def exit_app_cb(self):
        '''Quits the application'''
        self.app.exit(0)


def random_string(size=5):
    '''Generate random string with the given size'''
    return ''.join(map(chr, [randint(33, 126) for x in range(size)]))
