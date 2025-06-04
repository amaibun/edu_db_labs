from psycopg2.extras import RealDictCursor
from Objects.DataResource import DataResource

class dbf_DataResource:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, resource):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".DataResource (
                    id, file_name, file_type, size, url, uploaded_at, dataset_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                str(resource.id),
                resource.file_name,
                resource.file_type,
                resource.size,
                resource.url,
                resource.uploaded_at,
                str(resource.dataset_id)
            ))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".DataResource WHERE id = %s""", (str(id),))
            row = cur.fetchone()
            if row:
                return DataResource(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".DataResource""")
            return [DataResource(**row) for row in cur.fetchall()]