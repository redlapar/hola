import unittest
import hola
class MyTest(unittest.TestCase):
    def testReadFileCount(self):
        lines = hola.readFile("sample.csv")
        self.assertEqual(2, len(lines))

    def testGetIdFromLine(self):
        id = hola.getIdFromLine("56997446800|1|2|3|4")
        self.assertEqual("56997446800", id)