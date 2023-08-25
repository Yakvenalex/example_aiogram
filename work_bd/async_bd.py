import asyncpg
import asyncio
from datetime import datetime, timedelta

CONNECT_USR = 'postgresql://adminn:Pl3453bvfhfd3M@89.208.104.136:5432/postgres'


async def create_tables(connection):
    async with connection.transaction():
        await connection.execute("""
            CREATE TABLE IF NOT EXISTS users2 (
                usid BIGINT,
                time TIMESTAMP,
                balance INT,
                profile1 VARCHAR(100),
                profile2 VARCHAR(100),
                profile3 VARCHAR(100),
                profile4 VARCHAR(100),
                profile5 VARCHAR(100),
                message VARCHAR(100),
                iscreate VARCHAR(100),
                username VARCHAR(50)
            )
        """)

        await connection.execute("""
            CREATE TABLE IF NOT EXISTS referrals (
                us_id BIGINT,
                referrer BIGINT
            )
        """)



async def select_all_pay_from_user(us_id, status='Active'):
    conn = await asyncpg.connect(CONNECT_USR)
    try:
        query = 'SELECT * FROM payments WHERE status_pay = $2 AND us_id = $1'
        result = await conn.fetch(query, us_id, status)

        # Преобразуем результат в список словарей
        users = [dict(record) for record in result]
        await conn.close()
        return users
    except:
        await conn.close()
        return False
