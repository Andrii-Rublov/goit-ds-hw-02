import faker
from random import randint, choice
import sqlite3

NUMBER_TASKS = 100
NUMBER_USERS = 10
VALUES_STATUS = [('new',), ('in progress',), ('completed',)]


def generate_fake_data(number_tasks, number_users) -> tuple:
    fake_tasks = []
    fake_descriptions = []
    fake_users = []
    fake_email = []
    fake_data = faker.Faker()

    for _ in range(number_tasks):
        fake_tasks.append(fake_data.bothify(text='task-####'))
        fake_descriptions.append(fake_data.sentence())

    for _ in range(number_users):
        fake_name = fake_data.name()
        fake_users.append(fake_name)
        fake_email.append(fake_data.ascii_email())



    return fake_tasks, fake_descriptions, fake_users, fake_email


# tasks, users, emails = generate_fake_data(NUMBER_TASKS, NUMBER_USERS)
# for name, email in zip(users, emails):
#     print(f"Name: {name}, Email: {email}")


def prepare_data(tasks, descriptions, users, emails) -> tuple:
    for_tasks = [
        (task, description, choice(range(1, len(VALUES_STATUS) + 1)), choice(range(1, len(users) + 1)))
        for task, description in zip(tasks, descriptions)
    ]
    for_users = list(zip(users, emails))
    for_status = VALUES_STATUS
    return for_tasks, for_users, for_status


def insert_data_to_db(tasks, users, status) -> None:
    with sqlite3.connect('tasks_management.db') as con:
        cur = con.cursor()

        cur.execute("DELETE FROM tasks")
        cur.executemany(
            "INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)", tasks
        )

        cur.execute("DELETE FROM users")
        cur.executemany("INSERT INTO users(fullname, email) VALUES (?, ?)", users)
        cur.executemany("INSERT OR IGNORE INTO status(name) VALUES (?)", status)


        con.commit()


if __name__ == "__main__":
    tasks, descriptions, users, emails = generate_fake_data(NUMBER_TASKS, NUMBER_USERS)
    tasks, users, status = prepare_data(tasks, descriptions, users, emails)
    insert_data_to_db(tasks, users, status)

