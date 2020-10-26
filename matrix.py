mtx1 = []
mtx2 = []
opr = input("Введите операцию (+ или * ): ")
print("Введите первую матрицу")
for x in range(3):
s = []
for y in range(3):
s.append(int(input()))
mtx1.append(s)
for x in range(3): # Вид первой матрицы
for y in range(3):
print(mtx1[x][y], end=" ")
print()
print("Введите вторую матрицу")
mtx2 = []
for x in range(3):
s = []
for y in range(3):
s.append(int(input()))
mtx2.append(s)
for x in range(3): # Вид второй матрицы
for y in range(3):
print(mtx2[x][y], end=" ")
print()
print()
if opr == "+":
for x in range(3):
for y in range(3):
mtx1[x][y] += mtx2[x][y]
elif opr == "*":
for x in range(3):
for y in range(3):
mtx1[x][y] *= mtx2[x][y]
else:
print("Ошибка. Команда не найдена")
for x in range(3):
for y in range(3):
print(mtx1[x][y], end=" ")
print()
