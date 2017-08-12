# coding:utf-8

import turtle


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)  # 向右20度
        tree(branch_len - 15, t)
        t.left(40)  # 向左20度
        tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)  # 回到之前的地方


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.speed(1)
    t.left(90)  # 向左90度
    t.up()
    t.backward(100)
    t.down()
    t.color('black')
    tree(75, t)
    my_win.exitonclick()


main()
