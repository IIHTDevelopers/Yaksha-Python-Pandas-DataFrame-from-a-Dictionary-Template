import unittest
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import pandas as pd


class ExceptionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis({
            'Employee ID': [101, 102, 103, 104, 105],
            'Name': ['John', 'Michael', 'Sarah', 'Anna', 'David'],
            'Age': [28, 34, 29, 42, 31],
            'Department': ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        })
        cls.test_obj = TestUtils()

    def test_invalid_employee_id(self):
        """Test if an invalid employee ID returns an empty result."""
        try:
            employee = self.analysis.get_employee_by_id(999)  # Non-existent ID
            obj = employee.empty
            self.test_obj.yakshaAssert("TestInvalidEmployeeID", obj, "exceptional")
            print("TestInvalidEmployeeID = Passed" if obj else "TestInvalidEmployeeID = Failed")
        except:
            self.test_obj.yakshaAssert("TestInvalidEmployeeID", False, "exceptional")
            print("TestInvalidEmployeeID = Failed")
            
    def test_invalid_column_access(self):
        """Test if accessing a non-existent column throws an error."""
        try:
            self.analysis.df["Invalid_Column"]
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")            
        except KeyError:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", True, "exceptional")
            print("TestInvalidColumnAccess = Passed")
        except:
            self.test_obj.yakshaAssert("TestInvalidColumnAccess", False, "exceptional")
            print("TestInvalidColumnAccess = Failed")
