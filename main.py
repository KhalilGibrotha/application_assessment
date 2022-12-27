#!/bin/python3 python3
# Path: application_organizer\main.py
# Compare this snippet from application_organizer\application.py:
# #!/bin/python3 python3
# # -*- coding: utf-8 -*-

import excel
import openpyxl
from application import Application


#
CRITICALITIES = ["High", "Medium", "Low"]
AVAILABILITIES = ["99.9%", "99.5%", "99.0%", "98.0%", "95.0%"]
BUSINESS_FUNCTIONS = ["Finance", "HR", "Marketing", "Sales", "Operations"]
ENVIRONMENTS = ["Prod", "Dev", "QA", "Staging"]
DATABASES = ["MySQL", "PostgreSQL", "Oracle", "SQL Server", "MongoDB"]
OPERATING_SYSTEMS = ["Linux", "Windows", "MacOS"]
PROGRAMMING_LANGUAGES = ["Python", "Java", "C#", "JavaScript", "PHP"]
FRAMEWORKS = ["Django", "Spring", "ASP.NET", "React", "Laravel"]
VERSION_CONTROL = ["Git", "SVN", "Mercurial"]
DEPLOYMENT = ["Ansible", "Chef", "Puppet", "Jenkins"]
MONITORING = ["New Relic", "AppDynamics", "Datadog"]
LOGGING = ["Splunk", "ELK Stack", "Graylog"]
SECURITY_ZONES = ["DMZ", "Intranet", "Extranet"]
BACKUP = ["AWS S3", "AWS RDS", "Azure Blob Storage", "Google Cloud Storage"]
DISASTER_RECOVERY = ["AWS RDS", "Azure Database", "Google Cloud SQL"]

def main():
    pass

def create_application():
    # prompt the user for input
    name = input("Enter the name of the application: ")
    criticality = input("Enter the criticality of the application ({}): ".format(", ".join(CRITICALITIES)))
    availability = input("Enter the availability of the application ({}): ".format(", ".join(AVAILABILITIES)))
    number_of_users = input("Enter the number of users of the application: ")
    business_function = input("Enter the business function of the application ({}): ".format(", ".join(BUSINESS_FUNCTIONS)))
    environments = input("Enter the environments of the application ({}): ".format(", ".join(ENVIRONMENTS)))
    servers = input("Enter the number of servers of the application: ")
    memory = input("Enter the memory of the application: ")
    storage = input("Enter the storage of the application: ")
    database = input("Enter the database of the application ({}): ".format(", ".join(DATABASES)))
    operating_system = input("Enter the operating system of the application ({}): ".format(", ".join(OPERATING_SYSTEMS)))
    programming_language = input("Enter the programming language of the application ({}): ".format(", ".join(PROGRAMMING_LANGUAGES)))
    framework = input("Enter the framework of the application ({}): ".format(", ".join(FRAMEWORKS)))
    version_control = input("Enter the version control of the application ({}): ".format(", ".join(VERSION_CONTROL)))
    deployment = input("Enter the deployment of the application ({}): ".format(", ".join(DEPLOYMENT)))
    monitoring = input("Enter the monitoring of the application ({}): ".format(", ".join(MONITORING)))
    logging = input("Enter the logging of the application ({}): ".format(", ".join(LOGGING)))
    security_zones = input("Enter the security zones of the application ({}): ".format(", ".join(SECURITY_ZONES)))
    backup = input("Enter the backup of the application ({}): ".format(", ".join(BACKUP)))
    disaster_recovery = input("Enter the disaster recovery of the application ({}): ".format(", ".join(DISASTER_RECOVERY)))
    cost = input("Enter the cost of the application: ")
    revenue = input("Enter the revenue of the application: ")
    profit = input("Enter the profit of the application: ")
    notes = input("Enter any notes about the application: ")

    # create an instance of the Application class
    app_1 = Application(name, criticality, availability, number_of_users, business_function, environments, servers, memory, storage, database, operating_system, programming_language, framework, version_control, deployment, monitoring, logging, security_zones, backup, disaster_recovery, cost, revenue, profit, notes)

def update_application():
    # open the existing workbook and worksheet
    wb = openpyxl.load_workbook("applications.xlsx")
    ws = wb.active

    # create a list to store the application instances
    applications = []

    # iterate over the rows in the worksheet
    for row in ws.iter_rows(min_row=2, values_only=True):
        # unpack the row values into variables
        name, criticality, availability, number_of_users, business_function, environments, servers, memory, storage, database, operating_system, programming_language, framework, version_control, deployment, monitoring, logging, security_zones, backup, disaster_recovery, cost, revenue, profit, notes = row

        # prompt the user for any missing data
        if not name:
            name = input("Enter the name of the application: ")
        if not criticality:
            criticality = input("Enter the criticality of the application ({}): ".format(", ".join(CRITICALITIES)))
        if not availability:
            availability = input("Enter the availability of the application ({}): ".format(", ".join(AVAILABILITIES)))
        if not number_of_users:
            number_of_users = input("Enter the number of users: ")
        if not business_function:
            business_function = input("Enter the business function ({}): ".format(", ".join(BUSINESS_FUNCTIONS)))
        if not environments:
            environments = input("Enter the environments ({}): ".format(", ".join(ENVIRONMENTS)))
        if not servers:
            servers = input("Enter the number of servers: ")
        if not memory:
            memory = input("Enter the memory: ")
        if not storage:
            storage = input("Enter the storage: ")
        if not database:
            database = input("Enter the database ({}): ".format(", ".join(DATABASES)))
        if not operating_system:
            operating_system = input("Enter the operating system ({}): ".format(", ".join(OPERATING_SYSTEMS)))
        if not programming_language:
            programming_language = input("Enter the programming language ({}): ".format(", ".join(PROGRAMMING_LANGUAGES)))
        if not framework:
            framework = input("Enter the framework ({}): ".format(", ".join(FRAMEWORKS)))
        if not version_control:
            version_control = input("Enter the version control ({}): ".format(", ".join(VERSION_CONTROL)))
        if not deployment:
            deployment = input("Enter the deployment ({}): ".format(", ".join(DEPLOYMENT)))
        if not monitoring:
            monitoring = input("Enter the monitoring ({}): ".format(", ".join(MONITORING)))
        if not logging:
            logging = input("Enter the logging ({}): ".format(", ".join(LOGGING)))
        if not security_zones:
            security_zones = input("Enter the security zones ({}): ".format(", ".join(SECURITY_ZONES)))
        if not backup:
            backup = input("Enter the backup ({}): ".format(", ".join(BACKUP)))
        if not disaster_recovery:
            disaster_recovery = input("Enter the disaster recovery ({}): ".format(", ".join(DISASTER_RECOVERY)))
        if not cost:
            cost = input("Enter the cost: ")
        if not revenue:
            revenue = input("Enter the revenue: ")
        if not profit:
            profit = input("Enter the profit: ")
        if not notes:
            notes = input("Enter the notes: ")
        

        # create an instance of the Application class
        app = Application(name, criticality, availability, number_of_users, business_function, environments, servers, memory, storage, database, operating_system, programming_language, framework, version_control, deployment, monitoring, logging, security_zones, backup, disaster_recovery, cost, revenue, profit, notes)

        # add the application to the list
        applications.append(app)

if __name__ == "__main__":
    main()


