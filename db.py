from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
import urllib

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                 "SERVER=LAPTOP-AFQ9446H;"
                                 "DATABASE=todo;"
                                 "Trusted_Connection=yes;")

engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

metadata = MetaData()

metadata.reflect(engine)

items = metadata.tables["items"]

usersData = metadata.tables["Users"]

Sessionlocal = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False))
