import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='L5pS1NJTn8X6Ekz.root',
        password='QZ5bRIrOdhTijxG7',
        database='student_task_manager',
        port=4000
    )

    return connection

# def get_database_connection():
#     connection = mysql.connector.connect(
#         host = 'localhost',
#         user = 'root',
#         password = 'root123',
#         database = 'student_task_manager'
#     )

#     return connection