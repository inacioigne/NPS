import sqlite3

ids = [
    '40af385f-3987-4231-9374-8172eddb1662',
    'ffab9fc1-dfba-4a61-a070-4da4704d084b',
    'b94526ec-c891-425d-a5c4-b0591a9b77c7',
    '94d481bc-ce21-40b9-b31f-a5faa3e2a009',
    '0b5ffbdb-9535-4898-99f2-fb70f3f23737',
    '74b2ddfa-e675-470c-b2c3-81b1f923301d',
    '03c75352-15f5-4766-a566-886e70043aa1',
    'a64a54da-6eb5-44db-b026-dfd27630b06d'
]
conn = sqlite3.connect('src/database/database.sqlite')
cursor = conn.cursor()

for Id in ids:
    cursor.execute(
        """DELETE FROM surveys_users WHERE id = ?""",(Id,)
    )
    conn.commit()
    
