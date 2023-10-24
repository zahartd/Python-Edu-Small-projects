import random
import turtle
import os
turtle.speed(0)
def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
def drawline(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)
def erase(x, y):
    gotoxy(x, y)
    turtle.color("white")
    turtle.begin_fill()
    turtle.begin_poly()
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.end_poly()
    turtle.end_fill()

x = random.randint(1, 100)
coord_list = []
coord = open("coords.txt")
for line in coord:
    line = line.strip().split(",")
    nums = []
    for n in line:
        nums.append(int(n))

    coord_list.append(nums)
while True:
    answer = turtle.textinput("Играть?", "y/n")
    if answer == "n":
        os.abort()
    elif answer == "y":
        break
    else:
        turtle.textinput("Вы ввели некоректное значение!!!", "Попробуйте еще раз!")
try_count = 0
while True:
    number = turtle.numinput("Угадайте", "Число", 0, 0, 100)
    if number == x:
        turtle.clear()
        turtle.color("green")
        gotoxy(-150, 200)
        turtle.write("Ура! Вы победили.",
                     font=("Arial", 28, "normal"))
        break
    else:
        turtle.color("orange")
        gotoxy(-150, 100)
        turtle.write("Неверно!!!",
                     font=("Arial", 28, "normal"))
        if number < x:
            turtle.textinput("Подсказка", "Загаданное число больше, чем введенное вами.")
        elif number > x:
            turtle.textinput("Подсказка", "Загаданное число меньше, чем введенное вами.")
        turtle.color("black")
        if try_count == 4:
            gotoxy(-100, 0)
            turtle.circle(20)
        drawline(*coord_list[try_count])
        try_count += 1
        if try_count == 10:
            turtle.clear()
            turtle.color("red")
            gotoxy(-150, 200)
            turtle.write("Вы проиграли!!!",
                     font=("Arial", 44, "normal"))
            break