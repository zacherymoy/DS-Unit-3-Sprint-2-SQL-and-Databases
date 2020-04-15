import sqlite3

# Connect to Database
connection = sqlite3.connect("demo_data.sqlite3")

# Need a cursor to execute queries
pg_curs = connection.cursor()

# Create a table -
create_table_statement = '''
CREATE TABLE demo (
  s        TEXT PRIMARY KEY,
  x  INT NOT NULL,
  y    INT
);


INSERT INTO demo (s, x, y)
VALUES('g', 3, 9);

INSERT INTO demo (s, x, y)
VALUES('v', 5, 7);

INSERT INTO demo (s, x, y)
VALUES('f', 8, 7);

'''
connection.commit()
connection.close()
