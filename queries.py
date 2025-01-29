import sqlite3

def execute_query1(sql: str) -> list:
    with sqlite3.connect('tasks_management.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

sql = """
select t.id as task_id, t.title, t.description as task_description, u.id as user_id, u.fullname
from tasks as t
inner join users as u on u.id = t.user_id
WHERE user_id = 10;
"""

print(execute_query1(sql))

