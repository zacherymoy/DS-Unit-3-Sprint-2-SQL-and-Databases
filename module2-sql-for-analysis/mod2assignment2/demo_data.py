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


# - Count how many rows you have - it should be 3!
# SELECT s FROM demo
# - How many rows are there where both `x` and `y` are at least 5?
# SELECT * FROM demo
# WHERE x >= 5 AND y >= 5
# - How many unique values of `y` are there (hint - `COUNT()` can accept a keyword
#   `DISTINCT`)?
# SELECT COUNT (DISTINCT y)
# FROM demo
