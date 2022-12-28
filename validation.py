#!/bin/python3  python3
# -*- coding: utf-8 -*-


# perform type validation on the input
def validate_database_type(database_type):
    if value in [MySQL, PostgreSQL, Oracle, SQLServer]:
        return value
    else:
        raise ValueError("Invalid database type, Acceptable values are: MySQL, PostgreSQL, Oracle, SQLServer")
