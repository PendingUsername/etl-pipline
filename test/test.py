import psycopg2

conn_params = {
    "dbname": "airflow",
    "user": "airflow",
    "password": "airflow",
    "host": "10.0.0.132",
    "port": 5432,
    "connect_timeout": 10
}

try:
    conn = psycopg2.connect(**conn_params)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")
