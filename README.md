# Database Investigator
Interactive Python-based MySQL database search engine that dynamically explores unknown schemas and performs intelligent keyword searches across all tables and columns. Enables users to uncover relevant records without needing prior knowledge of the database structure.

## Purpose
Demonstrates practical skills in MySQL integration, automated schema discovery, and interactive search algorithms. This tool is valuable for developers, analysts, and administrators working with unfamiliar or complex relational databases.

## Skills Learned
Throughout the development of this project, I gained hands-on experience and strengthened my skills in:

* **Database Management:** MySQL connections, schema discovery, and query generation  
* **Python Programming:** Modular design and interactive CLI applications  
* **Dynamic Schema Analysis:** Automated table/column mapping across database structures  
* **Search Algorithm Development:** Flexible keyword-based search using LIKE queries  
* **Error Handling & Resilience:** Graceful handling of unsupported types and query failures  
* **User Experience Design:** Clear prompts, informative feedback, and result displays  
* **Tool Adaptability:** Universal design for any MySQL database structure
<br>
<br>

# Instructions: Setup and Run

Follow these steps to set up and run the MySQL DB Investigator locally.
This project uses an example employee database, but the Python script can be adapted to work with any MySQL database — simply update the queries and schema references in `investigator.py`.

## 1. Clone the Repository

```bash
git clone https://github.com/RithvikBurri/mysql-db-investigator.git
cd mysql-db-investigator
```

## 2. Combine SQL Dump Parts

The SQL dump is split into multiple parts. Combine them into a single `.sql` file before importing it.

🔹 On **Linux/macOS**:

```bash
cat employee_database_dump.sql.part00* > employee_database_dump.sql
```

🔹 On **Windows**:

```cmd
copy /b employee_database_dump.sql.part000 + employee_database_dump.sql.part001 + employee_database_dump.sql.part002 + employee_database_dump.sql.part003 + employee_database_dump.sql.part004 + employee_database_dump.sql.part005 + employee_database_dump.sql.part006 employee_database_dump.sql
```

## 3. Set Up MySQL Database

Make sure MySQL is installed and running on your system.

Open your MySQL client (such as MySQL Workbench or terminal), and run the SQL script to set up the database:

```bash
source employee_database_dump.sql;
```

This will create the required database and populate it with initial data.

## 4. Configure Database Connection

In `investigator.py`, update the database connection details with your own MySQL credentials:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='your_mysql_username',
    password='your_mysql_password',
    database='your_database_name'
)
```

## 5. Install Required Python Packages

Make sure you're using Python **3**.

Install the MySQL connector:

```bash
pip install mysql-connector-python
```

## 6. Run the Application

```bash
python investigator.py
```

## How It Works

1. Connect to the MySQL database.
2. Run custom queries or analysis defined in `investigator.py`.
3. View the output directly in your terminal.
