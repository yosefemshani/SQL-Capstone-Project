
    
import sqlite3
import pandas as pd

def setup_database(db_name="techsmart.db"):
           
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            # Creating Employee_Records table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Employee_Records (
                   employee_id INTEGER PRIMARY KEY,
                   role TEXT,
                   store_location TEXT,
                   sales_performance REAL
                )
            ''')

            # Creating Product_Details table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Product_Details (
                    product_id INTEGER PRIMARY KEY,
                    product_name TEXT,
                    category TEXT,
                    price REAL,
                    stock INTEGER
                )
            ''')

            # Creating Customer_Demographics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Customer_Demographics (
                    customer_id INTEGER PRIMARY KEY,
                    age INTEGER,
                    gender TEXT,
                    location TEXT,
                    loyalty_program TEXT
                )
            ''')
            
            # Creating Sales_Transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Sales_Transactions (
                    transaction_id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    product_id TEXT,
                    employee_id INTEGER,
                    quantity INTEGER,
                    total_amount REAL,
                    sale_date TEXT,
                    FOREIGN KEY (customer_id) REFERENCES customer_demographics(customer_id),
                    FOREIGN KEY (employee_id) REFERENCES employee_records(employee_id)
                )
            ''')


            conn.commit()

            # Loading data from CSVs
            employee_df = pd.read_csv("Employee_Records.csv")
            products_df = pd.read_csv("Product_Details.csv")
            customers_df = pd.read_csv("Customer_Demographics.csv")
            transactions_df = pd.read_csv("Sales_Transactions.csv")
          
            # Inserting data into tables
            employee_df.to_sql("Employee_Records", conn, if_exists="replace", index=False)
            customers_df.to_sql("Customer_Demographics", conn, if_exists="replace", index=False)
            transactions_df.to_sql("Sales_Transactions", conn, if_exists="replace", index=False)
            products_df.to_sql("Product_Details", conn, if_exists="replace", index=False)
            
            conn.close()
            print("✅ Database setup complete: Tables created and populated with data!")

    # Example usage:
    # setup_database()  # Call this from the first notebook

