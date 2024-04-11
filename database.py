import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="focus", db="jobs", charset="utf8")
cursor = connection.cursor()

select_data = "SELECT * FROM jobs"

cursor.execute(select_data)

jobs = cursor.fetchall()

# Fetch column names
columns = [column[0] for column in cursor.description]

# Convert each row into a dictionary
jobs_dicts = []
for row in jobs:
    jobs_dicts.append(dict(zip(columns, row)))

# Print the dictionaries
for job_dict in jobs_dicts:
    print(job_dict)

cursor.close()
connection.close()
