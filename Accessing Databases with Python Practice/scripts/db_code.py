import sqlite3
import pandas as pd

# Creating Database
conn = sqlite3.connect('Accessing Databases with Python Practice/database/STAFF.db')

# First Table
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']

# Second Table
table_name2 = 'DEPARTMENTS'
attribute_list2 = ['DEPT_ID', 'DEP_NAME','MANAGER_ID','LOC_ID']

file_path = 'Accessing Databases with Python Practice/data/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)

file_path2 = 'Accessing Databases with Python Practice/data/Departments.csv'
df2 = pd.read_csv(file_path2, names = attribute_list2)

df.to_sql(table_name, conn, if_exists='replace', index=False)
print('Table is ready')

df2.to_sql(table_name2, conn, if_exists='replace', index=False)
print('Table 2 is ready')

# Viewing all the data in the table
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing only FNAME column of data
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Appending new data to the table
data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Appending new data to the table

data_dict = {'DEPT_ID' : [9],
            'DEP_NAME' : ['Quality Assurance'],
            'MANAGER_ID' : 30010,
            'LOC_ID' : ['L0010']}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(table_name2, conn, if_exists = 'append', index =False)
print('Data appended successfully')

# Viewing all the data in the table
query_statement = f"SELECT * FROM {table_name2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing only FNAME column of data
query_statement = f"SELECT DEP_NAME FROM {table_name2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the total number of entries in the table
query_statement = f"SELECT COUNT(*) FROM {table_name2}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

conn.close()