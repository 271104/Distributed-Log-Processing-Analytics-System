import psycopg2

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


class PostgresClient:

    def __init__(self):

        self.connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )

        self.cursor = self.connection.cursor()

    def test_connection(self):

        self.cursor.execute(
            "SELECT version();"
        )

        result = self.cursor.fetchone()

        return result

    def insert_log(self, event):

        query = """
        INSERT INTO logs (
            event_id,
            user_id,
            event_type,
            device_type,
            country,
            event_timestamp
        )
        VALUES (%s,%s,%s,%s,%s,%s)
        """

        values = (
            event["event_id"],
            int(event["user_id"]),
            event["event_type"],
            event["device_type"],
            event["country"],
            event["timestamp"]
        )

        self.cursor.execute(query, values)

        self.connection.commit()