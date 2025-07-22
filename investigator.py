"""
Project:
    Investigator – Dynamic MySQL Database Search Engine
Author:
    Rithvik Burri
Description:
    Investigator is an interactive Python application that establishes connections to any
    MySQL database and performs intelligent keyword searches across all tables and columns.
    The tool enables users to discover relevant records without requiring prior knowledge of
    the database structure or schema. This application is universally compatible with any
    MySQL database - for this project demonstration, an employee database serves as the
    reference implementation, but the tool automatically adapts to work with databases of
    any structure, size, or content type.
Purpose:
    This project serves developers, data analysts, students, and database administrators
    who need to efficiently explore and analyze unfamiliar MySQL databases. The application
    combines automated schema discovery with flexible keyword-based search algorithms to
    transform complex relational data structures into accessible, readable results. The
    project demonstrates practical expertise in database connectivity, robust error handling,
    and interactive user interface design, providing both educational value and practical
    utility for dynamic database investigation and analysis.
"""
import mysql.connector

# Establish a connection to the MySQL database
def connect_to_employee_db():
    return mysql.connector.connect(
        host="192.168.4.41",    # IP address of the database server
        user="Rithv",           # MySQL username
        password="Rookie@123",  # MySQL password
        database="employee"     # Name of the target database
    )

# Return a list of all table names in the connected database
def list_tables(cursor):
    cursor.execute("SHOW TABLES")
    return [table[0] for table in cursor.fetchall()]

# Get all column names from a specific table
def get_columns(cursor, table_name):
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    return [col[0] for col in cursor.fetchall()]

# Search for the given keyword in all columns of a specific table
def search_keyword_in_table(cursor, table_name, keyword):
    results = []
    columns = get_columns(cursor, table_name)  # Fetch all column names
    for column in columns:
        try:
            # Attempt to search using the LIKE operator
            cursor.execute(
                f"SELECT * FROM `{table_name}` WHERE `{column}` LIKE %s",
                (f"%{keyword}%",)
            )
            matches = cursor.fetchall()
            if matches:
                results.append((column, cursor.column_names, matches))  # Store matching rows
        except:
            pass  # Skip columns that can't be searched (e.g., BLOB, unsupported types)

    return results

# Main execution block
def main():
    conn = connect_to_employee_db()  # Connect to the database
    cursor = conn.cursor()
    print("✅ Connected to 'employee' database.")
    keyword = input("🔍 Enter a keyword to search (e.g., name or department): ").strip()
    tables = list_tables(cursor)  # Get all table names
    all_matches = {}              # Store matches organized by table
    # Search each table for the given keyword
    for table in tables:
        results = search_keyword_in_table(cursor, table, keyword)
        if results:
            all_matches[table] = results
    # Handle case where no matches are found
    if not all_matches:
        print("❌ No matches found in any table.")
        return
    # If only one table has matches, display directly
    if len(all_matches) == 1:
        table = next(iter(all_matches))
        print(f"\n📌 Found matches in table '{table}':")
        for column, col_names, rows in all_matches[table]:
            print(f"\n🔸 Column: {column}")
            for row in rows:
                print(" - " + ", ".join(f"{col}: {val}" for col, val in zip(col_names, row)))
    else:
        # Let the user choose which table's results to view
        print("\n✅ Multiple tables have matches:")
        matched_tables = list(all_matches.keys())
        for i, table in enumerate(matched_tables, 1):
            print(f"{i}. {table}")
        table_choice = int(input("Select a table number to view results: ")) - 1
        selected_table = matched_tables[table_choice]
        print(f"\n📌 Matches in table '{selected_table}':")
        for column, col_names, rows in all_matches[selected_table]:
            print(f"\n🔸 Column: {column}")
            for row in rows:
                print(" - " + ", ".join(f"{col}: {val}" for col, val in zip(col_names, row)))
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
