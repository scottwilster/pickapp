import os
import sqlite3
from contextlib import closing

import pandas as pd
import pytest

# What the fuck shit kinda shit is django in to that you have to do this...
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pick6.pick6.settings")

from pick6.picks.models import sql_to_df


@pytest.mark.models
def test_sql_to_df():
    # Create the dummy DataFrame to load.
    test_df = pd.DataFrame({"Str": ["This", "is", "a", "test"], "Num": list(range(4))})

    # Write the table to the newly created delete.db table.
    with (closing(sqlite3.connect("delete.db"))) as con:
        test_df.to_sql("test_tbl", con, index=False, if_exists="replace")

    # Let's get crazy and change the test_df before we compare.
    test_df.loc[0, "Num"] = 99

    # Call the function we intend to confirm works.
    fnct_df = sql_to_df(tbl_name="test_tbl", db_path="delete.db")

    assert not (test_df.equals(fnct_df))

    # Do the same adjustement to the loaded df and make sure it now matches.
    fnct_df.loc[0, "Num"] = 99
    assert test_df.equals(fnct_df)

    os.remove("delete.db")
