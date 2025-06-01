from model.access_log import AccessLog
from psycopg2.extras import RealDictCursor

class AccessLogDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, access_log):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".AccessLog (id, accessed_at, user_id, dataset_id)
                VALUES (%s, %s, %s, %s)
            """, (
                str(access_log.id),
                access_log.accessed_at,
                str(access_log.user_id),
                str(access_log.dataset_id)
            ))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".AccessLog WHERE id = %s""", (str(id),))
            row = cur.fetchone()
            if row:
                return AccessLog(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".AccessLog""")
            return [AccessLog(**row) for row in cur.fetchall()]
