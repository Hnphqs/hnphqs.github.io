# -*- coding: UTF-8 -*-
#made in hnphqs
import turtle as t
import time
import random
import PySimpleGUI as sg
def 设置绘图窗口(width,height,startx,starty):
    t.setup(width,height,startx,starty)
def 移动到(x,y):
    t.goto(x,y)
def 前进(d):
    t.fd(d)
def 后退(d):
    t.bk(d)
def 圆(r,angle):
    t.circle(r,angle)
def 左转(angle):
    t.left(angle)
def 右转(angle):
    t.right(angle)
def 朝向(angle):
    t.seth(angle)
def 设置画笔颜色模式(mode):
    t.colormode(mode)
def 设置画笔颜色(color):
    t.pencolor(color)
def 返回当前画笔颜色():
    return t.pencolor()
def 填充(color):
    t.fillcolor(color)
def 开始填充():
    t.begin_fill()
def 结束填充():
    t.end_fill()
def 抬笔():
    t.pu()
def 落笔():
    t.pd()
def 设置画笔宽度(width):
    t.penwidth(width)
def 绝对值(a):
    return abs(a)
def 完成():
    t.done()
def 当前坐标到原点的值():
    return t.pos()
def 弹窗(a,标题,按钮颜色,背景颜色,一行几个字,按钮内容):
    sg.popup(a,title=标题,button_color=按钮颜色,background_color=背景颜色,line_width=一行几个字,custom_text=按钮内容)
def 判断弹窗(a):
    sg.popup_yes_no(a)
def 警告弹窗(a):
    sg.popup_error(a)
def 自动关闭弹窗(a):
    sg.popup_auto_close(a)
def 滚动弹窗(内容,标题):
    sg.popup_scrolled(内容,title=标题)
def 询问(a):
    return sg.popup_get_text(a)
def 文件选择器(a):
    sg.popup_get_file(a)

