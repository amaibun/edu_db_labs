from psycopg2.extras import RealDictCursor
from Objects.Dataset import Dataset

class dbf_Dataset:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, dataset):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".Dataset (
                    id, title, description, created_at, updated_at, format, license, status,
                    organization_id, category_id, user_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                str(dataset.id), dataset.title, dataset.description,
                dataset.created_at, dataset.updated_at, dataset.format,
                dataset.license, dataset.status,
                str(dataset.organization_id), str(dataset.category_id), str(dataset.user_id)
            ))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Dataset WHERE id = %s""", (str(id),))
            row = cur.fetchone()
            if row:
                return Dataset(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Dataset""")
            return [Dataset(**row) for row in cur.fetchall()]