import unittest
from os.path import abspath,dirname

file_path = dirname(abspath(__file__)) + "\\test_case"
print(file_path)
suit = unittest.defaultTestLoader.discover(file_path,"*case.py")

runner = unittest.TextTestRunner()
runner.run(suit)