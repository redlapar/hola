import unittest
import hola
class MyTest(unittest.TestCase):
    def testReadFileCount(self):
        lines = hola.readFile("sample.csv")
        self.assertEqual(2, len(lines))

    def testGetIdFromSampleLine(self):
        id = hola.getIdFromSampleLine("56997446800|1|2|3|4")
        self.assertEqual("56997446800", id)

    def testFiltraSampleDeSCL(self):
        lines = hola.filtrarDosArchivos("sample.csv", "scl.csv")
        expected = "56997446800,7315290-9,quiero este campo"
        actual = lines[0]
        self.assertEqual(expected, actual)

    def testGetIdFromSCLLine(self):
        id = hola.getIdFromSCLLine("9,828,AAA,7103277-8,56989089032")
        self.assertEqual("56989089032", id)