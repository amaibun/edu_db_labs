from psycopg2.extras import RealDictCursor
from Objects.Tag import Tag

class dbf_Tag:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, tag):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".Tag (id, name)
                VALUES (%s, %s)
            """, (str(tag.id), tag.name))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Tag WHERE id = %s""", (str(id),))
            row = cur.fetchone()
            if row:
                return Tag(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Tag""")
            return [Tag(**row) for row in cur.fetchall()]