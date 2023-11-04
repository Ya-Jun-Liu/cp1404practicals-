"""
project_management
Estimate: 1200 minutes
Actual:  minutes
"""
import datetime
import csv
from project import Project

FILENAME = 'projects.txt'

# Define the constable variable for keys in dictionary
NAME = "name"
START_DATE = 'start_date'
PRIORITY = 'priority'
COST_ESTIMATE = 'cost_estimate'
COMPLETE_PERCENTAGE = 'complete_percentage'

# Define the rules that input should be not violated
STR_RULE = {lambda s: len(s) != 0: "Input can not be blank."}
PRIORITY_RULE = {lambda y: y > 0: "Priority should be greater than 0."}
COST_RULE = {lambda y: y > 0: "Cost estimate should be greater than 0."}
COMP_RULE = {lambda y: 100 >= y >=
             0: "Completion Percentage should be in ragne [0,100]"}
