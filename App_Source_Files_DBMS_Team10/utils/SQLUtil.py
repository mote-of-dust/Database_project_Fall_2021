import mysql.connector

my_connect = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='newpokemondatabase'
)

my_cursor = my_connect.cursor()


class SqlUtil:

    def execute_query(self, entry_str):
        global my_connect
        global my_cursor

        my_cursor = my_connect.cursor()
        search_string = entry_str
        output = []

        my_cursor.execute(entry_str)
        record = my_cursor.fetchall()

        for result in record:
            col = []
            for j in range(len(result)):
                col.append(str(result[j]))
            output.append(col)

        return output

    def execute_insert(self, entry_str):
        global my_connect
        global my_cursor

        my_cursor = my_connect.cursor()
        search_string = entry_str

        my_cursor.execute(search_string)
        my_connect.commit()

    def close_connection(self):
        global my_connect

        my_connect.close()
