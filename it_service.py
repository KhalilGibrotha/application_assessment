#!/bin/python3  python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, validator
from validation import *
from typing import Union, List, Literal
from globals import *


@dataclass
class ITService:
    name: str
    criticality: str
    availability: float
    number_of_users: int
    service_type: str
    environments: List[str]
    servers_count: int
    memory: str
    storage: str
    database: str
    operating_system: str
    programming_language: str
    framework: str
    version_control: str
    deployment: str
    monitoring: str
    logging: str
    security_zones: List[str]
    backup: bool
    disaster_recovery: bool
    cost: float
    revenue: float
    profit: float
    notes: str


@dataclass
class WebApplication(ITService):
    frontend_framework: str
    backend_framework: str


@dataclass
class Database(ITService):
    database_type: Union[Literal["MySQL"], Literal["PostgreSQL"], Literal["Oracle"], Literal["SQLServer"], List[str]]
    data_capacity: str

    # perform type validation on the input
    @validator("database_type")
    def validate_database_type(cls, value):#cls is the class
        if value in [MySQL, PostgreSQL, Oracle, SQLServer]:
            return value
        else:
            raise ValueError("Invalid database type, Acceptable values are: MySQL, PostgreSQL, Oracle, SQLServer")

#
if __name__ == "__main__":
    main()

db = Database("MySQL database", "High", 99.9, 1000, "Database", ["Production"], 2, "16GB", "500GB", "MySQL", "Linux", "Python", "Django", "Git", "Ansible", "Nagios", "ELK", "DMZ, Internal", "Yes", "Yes", 1000, 10000, 9000, "This is a MySQL database used for storing customer data.")

