import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="focus", db="jobs", charset="utf8")
cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(250) NOT NULL,
    location VARCHAR(250),
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(2000),
    requirements VARCHAR(2000)
    )
"""

insert_data = """
INSERT INTO jobs (title, location, salary, currency, responsibilities, requirements) VALUES
('Data Analyst', 'Nairobi, Kenya', '200000', 'KSH', 'Manage the company Data', 'Good communication skills'),
('Data Expert', 'Nairobi, Kenya', '200000', 'KSH', 'Manage the company Data', 'Good communication skills'),
('Data Scientist', 'Arusha, Tanzania', '200000', 'KSH', 'Manage the company Data', 'Good communication skills')
"""

cursor.execute(create_table)
cursor.execute(insert_data)

connection.commit()

select_data = "SELECT * FROM jobs"

cursor.execute(select_data)

jobs = cursor.fetchall()

for job in jobs:
    print(job)

cursor.close()
connection.close()

