import unittest
import numpy as np
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd

class BoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis({
            'Employee ID': [101, 102, 103, 104, 105],
            'Name': ['John', 'Michael', 'Sarah', 'Anna', 'David'],
            'Age': [28, 34, 29, 42, 31],
            'Department': ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        })
        cls.test_obj = TestUtils()
        
    def test_empty_dataframe(self):
        try:
            obj = self.analysis.df.empty
            obj = not(obj)
            self.test_obj.yakshaAssert("TestEmptyDataFrame", obj, "boundary")
            print("TestEmptyDataFrame = Passed" if obj else "TestEmptyDataFrame = Failed")
        except:
            self.test_obj.yakshaAssert("TestEmptyDataFrame", False, "boundary")
            print("TestEmptyDataFrame = Failed")