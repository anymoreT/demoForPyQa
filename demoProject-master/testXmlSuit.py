# -*- coding:utf-8 -*-
import  unittest
import xmlrunner
from unittest import TestSuite,TestLoader
import pdb
import sys,os


def run_all_cases():
    current_dir = os.path.dirname(__file__)
    testSuit_path = os.path.join(current_dir, "testCases")
    all_suits = TestLoader().discover(testSuit_path)
    test_result = run_suit(all_suits)

def run_suit(suit):
    runner = get_xml_runner()
    return runner.run(suit)

def get_xml_runner():
    root_path = os.path.dirname(".")
    root_path = os.path.join(root_path, "report")
    filename = 'xml_result.xml'
    report_path = os.path.join(root_path, filename)
    file_handle = open(report_path, 'wb')
    testRunner=xmlrunner.XMLTestRunner(output=file_handle)
    return testRunner
 
run_all_cases()    

  