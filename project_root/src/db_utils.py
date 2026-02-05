import yaml
import pandas as pd
from sqlalchemy import create_engine
import os


def load_credentials(filepath: str = "credentials.yaml") -> dict:
    """
    Loads database credentials from a YAML file.

    Args:
        filepath (str): Path to the credentials YAML file.

    Returns:
        dict: Dictionary containing database credentials.
    """
    with open(filepath, "r") as file:
        credentials = yaml.safe_load(file)
    return credentials


def save_to_csv(df, filepath):
    # Create folder if it does not exist
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Save CSV
    df.to_csv(filepath, index=False)


class RDSDatabaseConnector:
    """
    Class used to connect to a PostgreSQL database and extract loan payment data.
    """

    def __init__(self, credentials: dict):
        """
        Initialise connector with database credentials.

        Args:
            credentials (dict): Dictionary containing database credentials.
        """
        self.credentials = credentials

    def init_engine(self):
        """
        Creates and returns a SQLAlchemy engine using stored credentials.
        """

        user = self.credentials["RDS_USER"]
        password = self.credentials["RDS_PASSWORD"]
        host = self.credentials["RDS_HOST"]
        port = self.credentials["RDS_PORT"]
        database = self.credentials["RDS_DATABASE"]

        connection_string = (
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        )

        engine = create_engine(connection_string)
        return engine

    def extract_loan_payments(self) -> pd.DataFrame:
        """
        Extracts loan_payments table from database and returns it as a DataFrame.
        """
        engine = self.init_engine()
        query = "SELECT * FROM loan_payments;"
        df = pd.read_sql(query, engine)
        return df
    
if __name__ == "__main__":
    print("Script started")

    creds = load_credentials()

    connector = RDSDatabaseConnector(creds)

    df = connector.extract_loan_payments()

    print("Shape:", df.shape)
    print(df.head())

    save_to_csv(df, "data/loan_payments.csv")

    print("CSV saved successfully")