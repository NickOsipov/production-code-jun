"""
Module: config/database.py
Description: This module contains the database configuration settings for the application.
"""

from sqlalchemy import create_engine

from config.variables import (
    MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DBNAME,
    CH_USER, CH_PASS, CH_HOST, CH_PORT, CH_DBNAME
)


MYSQL_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DBNAME}"
CH_URI = f"clickhouse+http://{CH_USER}:{CH_PASS}@{CH_HOST}:{CH_PORT}/{CH_DBNAME}"

ENGINE = create_engine(CH_URI)
