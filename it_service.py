#!/bin/python3  python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class ITService:
    name: str
    criticality: str
    availability: float
    number_of_users: int
    service_type: str
    environments: List[str]
    servers: int
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
    database_type: str
    data_capacity: str

if __name__ == "__main__":
    main()
