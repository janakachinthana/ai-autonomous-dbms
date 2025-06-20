# Database connection configuration template

import os

DB_TYPE = os.getenv("DB_TYPE", "mssql")  # Options: postgresql, mysql, mongodb, mssql
DB_HOST = os.getenv("DB_HOST", "localhost")  # Default for MSSQL
DB_PORT = int(os.getenv("DB_PORT", 1433))  # Default port for MSSQL
DB_USER = os.getenv("DB_USER", "sa")
DB_PASSWORD = os.getenv("DB_PASSWORD", "enter the password here")
DB_NAME = os.getenv("DB_NAME", "IMBeta_New")

# Add additional configuration as needed for your environment
# Example: driver for MSSQL
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

# Example connection string for MSSQL
DB_CONNECTION_STRING = (
    f"DRIVER={{{DB_DRIVER}}};"
    f"SERVER={DB_HOST},{DB_PORT};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD}"
)
