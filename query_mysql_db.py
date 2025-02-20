from sqlalchemy import create_engine, text
import pandas as pd

def create_connection_string(db_config):
    """db_config needs to have user, password, host, and database name"""
    return f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

def test_connection(db_dict_config):
    """
    Test the connection to the database using the provided credentials.
    db_dict_config is a dict with keys user, password, host, and database.
    """
    connection_string = create_connection_string(db_dict_config)
    engine = create_engine(connection_string)
    
    try:
        with engine.connect() as connection:
            print("Connection successful")
            message = 'connection successful'
    except Exception as e:
        print(f"Connection failed: {e}")
        message = 'connection failed'
    return message

def query_db(query, db_dict_config):
    """
    Fetch data from the database using the provided SQL query.
    db_dict_config is a dict with keys user, password, host, and database.
    Returns: pd.DataFrame
    """
    connection_string = create_connection_string(db_dict_config)
    engine = create_engine(connection_string)
    
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
            return df
            
    except Exception as e:
        print(f"Error: {e}")
        return None
