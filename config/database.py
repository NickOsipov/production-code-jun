"""
Module: config/database.py
Description: This module contains the database configuration settings for the application.
"""

from sqlalchemy import create_engine

from config.variables import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ENGINE = create_engine(DB_URI)
