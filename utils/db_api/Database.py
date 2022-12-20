import aiomysql

async def test_example():
    conn = await aiomysql.connect(host=localhost, port=3306,
                                  user='root', password='', db='mysql')
    conn.close()
