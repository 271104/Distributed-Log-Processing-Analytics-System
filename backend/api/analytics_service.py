from database import get_connection


class AnalyticsService:

    def __init__(self):

        self.connection = get_connection()

        self.cursor = self.connection.cursor()

    def get_summary(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM logs
        """)

        total_events = self.cursor.fetchone()[0]

        return {
            "total_events": total_events
        }
    
    def get_event_distribution(self):

        self.cursor.execute("""
            SELECT
                event_type,
                COUNT(*)
            FROM logs
            GROUP BY event_type
            ORDER BY COUNT(*) DESC
        """)

        rows = self.cursor.fetchall()

        return [
            {
                "event_type": row[0],
                "count": row[1]
            }
            for row in rows
        ]
    
    def get_event_distribution(self):

        self.cursor.execute("""
            SELECT
                event_type,
                COUNT(*)
            FROM logs
            GROUP BY event_type
            ORDER BY COUNT(*) DESC
        """)

        rows = self.cursor.fetchall()

        return [
            {
                "event_type": row[0],
                "count": row[1]
            }
            for row in rows
        ]


    def get_active_users(self):

        self.cursor.execute("""
            SELECT COUNT(DISTINCT user_id)
            FROM logs
        """)

        active_users = self.cursor.fetchone()[0]

        return {
            "active_users": active_users
        }


    def get_timeline(self):

        self.cursor.execute("""
            SELECT
                DATE_TRUNC('minute', event_timestamp),
                COUNT(*)
            FROM logs
            GROUP BY 1
            ORDER BY 1
        """)

        rows = self.cursor.fetchall()

        return [
            {
                "minute": str(row[0]),
                "count": row[1]
            }
            for row in rows
        ]