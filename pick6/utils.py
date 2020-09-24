import sqlite3
from contextlib import closing

import pandas as pd


def sql_to_df(tbl_name: str, db_path: str = "pick6/db.sqlite3") -> pd.DataFrame:
    """ Returns all values from a single table in a database.

    Args:
        tbl_name (str): Name of the table to return within the database.
        db_path (str, optional): Filepath to the database. Defaults to
            "pick6/db.sqlite3".

    Returns:
        pd.DataFrame: pd.DataFrame of the table in the sqlite database.
    """

    with closing(sqlite3.connect(db_path)) as con:
        df = pd.read_sql(f"select * from {tbl_name}", con)

    return df
