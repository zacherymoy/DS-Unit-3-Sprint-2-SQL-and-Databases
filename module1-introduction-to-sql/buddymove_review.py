# import pandas as pd
# import sqlite3
#
# dataset_url = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
# df = pd.read_csv(dataset_url)
# #conn = sqlite3.Connection(dataset_url)
#
# df = pd.read_csv(dataset_url)
# df.to_sql('review', con=conn)

import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row

c.execute('CREATE TABLE REVIEW')
conn.commit()

df = pd.read_csv('buddymove_holidayiq.csv')
df.to_sql('REVIEW', conn, if_exists='replace', index = False)

c.execute('''
SELECT * FROM REVIEW
          ''')

for row in c.fetchall():
    print (row)
