import pymysql


class BotDB:

    def __init__(self):
        self.connect = pymysql.connect(host='localhost', user='root', password='1111', database='bobr_city')

    def close(self):
        print("Работа с базой данных завершена")
        self.connect.close()

    def user_exists(self, user_id):
        # Проверка есть ли данный пользователь в базе дынных
        with self.connect.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE Telegram_id = %s", user_id)

            self.connect.commit()
            row = cursor.fetchall()
            cursor.close()
            print(len(row))
            if len(row) == 0:
                return True
            else:
                return False

    def user_add(self, user_id: int):
        try:

            with self.connect.cursor() as cursor:
                print(user_id)
                cursor.execute("INSERT INTO users (Telegram_id) VALUE (%s)", user_id)
            self.connect.commit()
        except:
            print("Работа с базой данных завершена")
            self.connect.close()

    def get_all_attractions(self):
        # Берем все достопримечательности
        with self.connect.cursor() as cursor:
            cursor.execute("SELECT * FROM attractions")
            rows = cursor.fetchall()
            cursor.close()
            return rows
