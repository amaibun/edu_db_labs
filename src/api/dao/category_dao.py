import psycopg2
from psycopg2.extras import RealDictCursor
from model.category import Category

class CategoryDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, category):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".Category (id, name)
                VALUES (%s, %s)
            """, (
                str(category.id), category.name
            ))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM "ODMS".Category WHERE id = %s
            """, (str(id),))
            row = cur.fetchone()
            if row:
                return Category(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Category""")
            return [Category(**row) for row in cur.fetchall()]
