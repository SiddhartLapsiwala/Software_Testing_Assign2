# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    """Positive"""
    def testEquilateralTriangles(self):
        """ test for Equilateral triangle """
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')

    def testIsocelesTriangles(self):
        """ test for Isoceles triangle """
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isoceles', '3,3,5 should be Isoceles')

    def testScaleneTriangles(self):
        """ test for Scalene triangle """
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3,4,6 should be Scalene')

    def testRightTriangleA(self):
        """ test for Right triangle """
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        """ test for Right triangle """
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    """Negative"""
    def testNotTriangle(self):
        """ test for side does not form triangle """
        self.assertEqual(classifyTriangle(2,3,9),'NotATriangle','2,3,9 is a not triangle')

    def testNegativeSides(self):
        """ test for negative side """
        self.assertEqual(classifyTriangle(-2,-3,-9),'InvalidInput','-2,-3,-9 is a not valid input')

    def testMorethan200(self):
        """ test for side more than 200 """
        self.assertEqual(classifyTriangle(201, 301, 901), 'InvalidInput', '201,301,901 is a not valid input as more than 200')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

