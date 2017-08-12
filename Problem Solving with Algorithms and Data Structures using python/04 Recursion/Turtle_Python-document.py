# coding:utf-8

import turtle

my_win = turtle.Screen()
# The Tutorial of Turtle
# 1、Turtle motion
print turtle.position()
turtle.forward(25)  # 沿x轴正方向移动25  turtle.fd()
print turtle.position()
turtle.forward(-75)  # 沿x轴负方向移动75
print turtle.position()
print '--------------------------'

print turtle.position()  # turtle.pos
turtle.backward(25)  # 沿x轴负方向移动25  turtle.bk(), turtle.back()
print turtle.position()
turtle.back(100)
print turtle.position()
print turtle.pos()
print '--------------------------'

print turtle.heading()
turtle.right(90)  # 度数，左加右减  turtle.rt()
print turtle.heading()  # 270度
turtle.left(100)  # turtle.lf()
print turtle.heading()  # 10度
print '---------------------------'

print turtle.pos()
turtle.setpos(0, 0)
print turtle.pos()
turtle.setpos((20, 100))
print turtle.pos()
turtle.setx(100)
print turtle.pos()
turtle.sety(0)
print turtle.pos()
print '---------------------------'

turtle.setheading(90)  # 设置角度
print turtle.heading()
print turtle.position()
turtle.home()  # 恢复到初始状态
print turtle.heading()
print turtle.position()
print '---------------------------'

turtle.circle(100)  # 半径为50
print turtle.pos()
turtle.circle(50, 360)  # 半径120，角度180
print turtle.pos()
print '---------------------------'

turtle.home()
turtle.dot(20, 'blue')  # 画一个点，点半径20，颜色为blue
turtle.color('blue')  # 线条颜色为blue
print turtle.stamp()

for i in range(8):
    turtle.stamp()
    turtle.fd(30)
turtle.clearstamps(2)

for i in range(5):
    turtle.fd(50)
    turtle.lt(72)
for i in range(10):
    turtle.undo()  # 回退，返回到之前的操作

turtle.speed(6)
turtle.circle(40)
print '--------------------------------------'
print '--------------------------------------'

# 2、Tell Turtle's state
turtle.home()
print turtle.position()
turtle.goto(10, 10)  # 直接去某一点
print turtle.position()
print turtle.towards(0, 0)  # (10,10)到(0,0)的角度为225度
turtle.goto(0, 0)
print turtle.towards(10,10)  # (0,0)到(10,10)的角度为45度
print '-------------------------------------'

turtle.home()
turtle.left(50)
turtle.forward(100)
print turtle.pos()
print turtle.xcor()
print turtle.ycor()

# my_win.exitonclick()
