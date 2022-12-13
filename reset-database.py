import sys
import os
sys.path.append(os.path.dirname(__file__))

from libs.db_sqlite import SqliteDatabase


if __name__ == '__main__':
    db = SqliteDatabase()

    #
    # songs table

    db.query("DROP TABLE IF EXISTS songs;")
    print('removed db.songs')

    db.query("""
        CREATE TABLE songs (
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT,
        filehash  TEXT
        );
    """)
    print('created db.songs')

    #
    # fingerprints table

    db.query("DROP TABLE IF EXISTS fingerprints;")
    print('removed db.fingerprints')

    db.query("""
        CREATE TABLE `fingerprints` (
        `id`  INTEGER PRIMARY KEY AUTOINCREMENT,
        `song_fk` INTEGER,
        `hash`  TEXT,
        `offset`  INTEGER
        );
    """)
    db.query("""
        CREATE INDEX index_hash_fingerprints 
        ON fingerprints (hash)
    """)
    print('created db.fingerprints')

    print('done')
