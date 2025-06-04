import psycopg2
from psycopg2.extras import RealDictCursor
from Objects.Organization import Organization

class dbf_Organization:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, organization):
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO "ODMS".Organization (id, name, description, contact_email, website)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                str(organization.id), organization.name, organization.description,
                organization.contact_email, organization.website
            ))
            self.conn.commit()

    def find_by_id(self, id):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""
                SELECT * FROM "ODMS".Organization WHERE id = %s
            """, (str(id),))
            row = cur.fetchone()
            if row:
                return Organization(**row)
            return None

    def find_all(self):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("""SELECT * FROM "ODMS".Organization""")
            return [Organization(**row) for row in cur.fetchall()]