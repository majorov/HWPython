# Открыть соединение с базой данных
conn = MySQLdb.connect('localhost','root','12345','Список группы','Фамилия','Имя','Отчество')
cursor = conn.cursor()


# выполнить SQL-запрос с помощью execute()
cursor.execute("SELECT Фамилия FROM Спимок фамилий")


# Извлекаем одну строку с помощью fetchone и fetchall
row = cursor.fetchone()
rest_of_rows = cursor.fetchall()
print ("Фамилия: %" row)


sql = "insert into group(Фамилия, Имя, Отчество) value ('Федоров', 'Федор', 'Федорович')"
cursor.execute(sql)

sql = "update group SET Фамилия='Федоров' where Отчество='Федорович'"
cursor.execute(sql)

sql = "select * from group where Имя='Федор' AND Фамилия='Федорович'"
cursor.execute(sql)
rows = cursor.fetchone()
print (rows)
rows=cursor.fetchone()


# Не забываем закрыть соединение с базой данных
conn.close()