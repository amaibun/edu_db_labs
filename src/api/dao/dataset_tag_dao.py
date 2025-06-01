from model.dataset_tag import DatasetTag
from psycopg2.extras import RealDictCursor

class DatasetTagDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, dataset_tag):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".DatasetTag (dataset_id, tag_id)
                VALUES (%s, %s)
            """, (str(dataset_tag.dataset_id), str(dataset_tag.tag_id)))
            self.conn.commit()

    def find_by_dataset(self, dataset_id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM "ODMS".DatasetTag WHERE dataset_id = %s
            """, (str(dataset_id),))
            return [DatasetTag(**row) for row in cur.fetchall()]

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".DatasetTag""")
            return [DatasetTag(**row) for row in cur.fetchall()]
