import sys
import os
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(sys.path[0], '..'))

from termcolor import colored
from libs.db_sqlite import SqliteDatabase


if __name__ == '__main__':
    db = SqliteDatabase()

    row = db.executeOne("SELECT 2+3 as x;")

    assert row[0] == 5, "failed simple sql execution"
    print(f" * {colored('ok', 'green')}")
