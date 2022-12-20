import aiomysql

async def connection():
    conn = await aiomysql.connect(host=localhost, port=3306,
                                  user='root', password='', db='mysql')
    conn.close()
