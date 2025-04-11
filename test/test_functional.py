import unittest
import pandas as pd
from mainclass import EmployeeDataAnalysis
from test.TestUtils import TestUtils
import os

class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeDataAnalysis({
            'Employee ID': [101, 102, 103, 104, 105],
            'Name': ['John', 'Michael', 'Sarah', 'Anna', 'David'],
            'Age': [28, 34, 29, 42, 31],
            'Department': ['HR', 'Engineering', 'Marketing', 'Sales', 'Finance']
        })
        cls.test_obj = TestUtils()

    def test_create_employee_dataframe(self):
        """Test if the employee DataFrame is created correctly."""
        try:
            obj = isinstance(self.analysis.df, pd.DataFrame) and len(self.analysis.df) == 5
            self.test_obj.yakshaAssert("TestCreateEmployeeDataFrame", obj, "functional")
            print("TestCreateEmployeeDataFrame = Passed" if obj else "TestCreateEmployeeDataFrame = Failed")
        except:
            self.test_obj.yakshaAssert("TestCreateEmployeeDataFrame", False, "functional")
            print("TestCreateEmployeeDataFrame = Failed")
            
    def test_display_head(self):
        """Test if the first 5 rows are returned correctly."""
        try:
            head = self.analysis.display_head()
            obj = len(head) == 5
            self.test_obj.yakshaAssert("TestDisplayHead", obj, "functional")
            print("TestDisplayHead = Passed" if obj else "TestDisplayHead = Failed")
        except:
            self.test_obj.yakshaAssert("TestDisplayHead", False, "functional")
            print("TestDisplayHead = Failed")
            
    def test_get_employee_by_id(self):
        """Test if the employee details for ID 102 are fetched correctly."""
        try:
            employee = self.analysis.get_employee_by_id(102)
            obj = employee['Name'].iloc[0] == 'Michael'
            self.test_obj.yakshaAssert("TestGetEmployeeByID", obj, "functional")
            print("TestGetEmployeeByID = Passed" if obj else "TestGetEmployeeByID = Failed")
        except:
            self.test_obj.yakshaAssert("TestGetEmployeeByID", False, "functional")
            print("TestGetEmployeeByID = Failed")
            
    def test_get_employees_above_age(self):
        """Test if employees above age 30 are fetched correctly."""
        try:
            employees = self.analysis.get_employees_above_age(30)
            obj = len(employees) == 3  # Expecting 3 employees
            self.test_obj.yakshaAssert("TestGetEmployeesAboveAge", obj, "functional")
            print("TestGetEmployeesAboveAge = Passed" if obj else "TestGetEmployeesAboveAge = Failed")
        except:
            self.test_obj.yakshaAssert("TestGetEmployeesAboveAge", False, "functional")
            print("TestGetEmployeesAboveAge = Failed")
            
    def test_save_to_csv(self):
        """Test if the DataFrame is saved correctly to CSV."""
        self.analysis.save_to_csv("employee_data1.csv")
        obj = os.path.exists("employee_data1.csv")
        self.test_obj.yakshaAssert("TestSaveToCSV", obj, "functional")
        print("TestSaveToCSV = Passed" if obj else "TestSaveToCSV = Failed")
