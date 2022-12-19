#!/python/bin/python python3
# -*- coding: utf-8 -*-

import openpyxl
from application import Application
# from application import Application

# create a list of application instances
class Excel:
    def __init__(self):
        pass
    # def __init__(self, name, criticality, availability, number_of_users, business_function, environments, servers, memory, storage, database, operating_system, programming_language, framework, version_control, deployment, monitoring, logging, security_zones, backup, disaster_recovery, cost, revenue, profit, notes):
    def generate_excel():
        # create a new workbook and worksheet
        wb = openpyxl.Workbook()
        ws = wb.active

        # create a list of application instances
        applications = [
            Application("App 1", "High", "99.9%", 1000, "Finance", ["Prod", "Dev"], 2, 16, 500, "MySQL", "Linux", "Python", "Django", "Git", "Ansible", "New Relic", "Splunk", ["DMZ", "Intranet"], "AWS S3", "AWS RDS", 100000, 200000, 100000, "Some notes"),
            Application("App 2", "Low", "99.5%", 100, "HR", ["Prod"], 1, 8, 250, "PostgreSQL", "Windows", "Java", "Spring", "SVN", "Jenkins", "New Relic", "Splunk", ["Intranet"], "AWS S3", "AWS RDS", 50000, 150000, 100000, "Other notes"),
            Application("App 3", "Medium", "99.0%", 500, "Marketing", ["Prod", "QA"], 4, 16, 500, "Oracle", "Linux", "Java", "Hibernate", "Git", "Ansible", "New Relic", "Splunk", ["DMZ", "Intranet"], "AWS S3", "AWS RDS", 75000, 150000, 75000, "")]

        # write each application's information to a row in the worksheet
        row_num = 1
        for app in applications:
            app.write_to_excel(ws, row_num)
            row_num += 1

        # save the workbook
        wb.save("applications.xlsx")
