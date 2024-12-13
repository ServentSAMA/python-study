import sqlite3
# 创建一个新的数据库文件
conn = sqlite3.connect('example.db')

# 创建一个表
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# 插入数据
conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Alice', 'alice@example.com'))
conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Bob', 'bob@example.com'))

# 查询数据
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

# 更新数据
conn.execute("UPDATE users SET email = ? WHERE id = ?", ('alice_new@example.com', 1))

# 删除数据
conn.execute("DELETE FROM users WHERE id = ?", (2,))

# 开始事务
conn.execute("BEGIN TRANSACTION")
# 插入多条数据
conn.executemany("INSERT INTO users (name, email) VALUES (?, ?)", [('Charlie', 'charlie@example.com'), ('David', 'david@example.com')])
# 提交事务
conn.commit()

# # 备份数据库
# with open('backup.db', 'w') as f:
#     for line in conn.iterdump():
#         f.write(line)

# # 创建一个新的数据库文件
# new_conn = sqlite3.connect('example.db')
# # 恢复数据库
# with open('backup.db', 'r') as f:
#     for line in f:
#         new_conn.execute(line)

