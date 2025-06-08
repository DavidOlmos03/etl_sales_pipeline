import sqlite3

def load_data(df, db_path='warehouse/datawarehouse.db'):
    conn = sqlite3.connect(db_path)
    df.to_sql('fact_sales', conn, if_exists='replace', index=False)
    conn.close()

