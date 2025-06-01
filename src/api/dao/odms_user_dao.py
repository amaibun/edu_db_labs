from model.odms_user import ODMSUser
from psycopg2.extras import RealDictCursor

class ODMSUserDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, user):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".ODMS_User (id, username, email, role)
                VALUES (%s, %s, %s, %s)
            """, (str(user.id), user.username, user.email, user.role))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".ODMS_User WHERE id = %s""", (str(id),))
            row = cur.fetchone()
            if row:
                return ODMSUser(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".ODMS_User""")
            return [ODMSUser(**row) for row in cur.fetchall()]
