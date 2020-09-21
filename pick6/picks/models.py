import datetime
import sqlite3
from contextlib import closing

import pandas as pd

from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Sum, Count

# Create your models here.


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


class Bet(models.Model):
    user_name = models.CharField(max_length=30)
    team_text = models.CharField(max_length=40)
    pub_date = models.DateTimeField("date published")
    line_text = models.CharField(default="", max_length=50)
    line_pts = models.FloatField(default=0.0)
    result = models.IntegerField(default=1)

    def __str__(self):
        return self.result

    def __str__(self):
        return self.user_name

    def __str__(self):
        return self.line_text

    def __str__(self):
        return self.team_text

    def __str__(self):
        return self.user_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def sum_result(self):
        return self.__class__.objects.all().aggregate(sum_all=Sum("result"))

    def count_picks(self):
        return self.__class__.objects.all().aggregate(count_all=Count("line_text"))
