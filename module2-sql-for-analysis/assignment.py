import os
import pandas
from dotenv import load_dotenv
from psycopg2.extras import execute_values
import psycopg2
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

load_dotenv() #> loads contents of the .env file into the script's environment

dbname='txaxqhui'
user='txaxqhui'
password='0Csh9-op9iXf7Ui6J2Lrc32VxA7EULlx'
host='drona.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user,
                        password=password, host=host)

# CSV_FILEPATH = os.path.join(
#     os.path.dirname(__file__), '.', 'data', 'titanic.csv')
#
# df = pandas.read_csv(C:\Users\zmoy9\OneDrive\Documents\GitHub\DS-Unit-3-Sprint-2-SQL-and-Databases\module2-sql-for-analysis\titanic.csv)
# print(df.head())

df = pandas.read_csv("https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv")


connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

#query = "SELECT * from test_table;"
#cursor.execute(query)
#results = cursor.fetchall()
#print(type(results)) #> list
#print(results)

#
# CREATE TABLE

table_creation_query = """
CREATE TABLE IF NOT EXISTS passengers (
  id SERIAL PRIMARY KEY,
  survived integer,
  pclass integer,
  name varchar NOT NULL,
  gender varchar NOT NULL,
  age float,
  sib_spouse_count integer,
  parent_child_count integer,
  fare float
);
"""
cursor.execute(table_creation_query)
#
# INSERT DATA IN THE TABLE
#

#list_of_tuples = [
#  ('A rowwwww', 'null'),
#  ('Another row, with JSONNNNN', json.dumps(my_dict)),
#  ('Third row', "3")
#]

# how to convert dataframe into a list of tuples?

list_of_tuples = list(df.to_records(index=True))
# possibly sometimes would need to do further transformations, perhaps using a list comprehension

insertion_query = "INSERT INTO passengers (id, survived, pclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples)

# SAVE THE RESULTS!
connection.commit()
# CLEAN UP!
cursor.close()
connection.close()
