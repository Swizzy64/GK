#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy
from math import *
import random

N = 20
tab = numpy.zeros((N + 1, N + 1, 3))
tabColor = numpy.zeros((N + 1, N + 1, 3))


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def spin(angle):
    glRotate(angle, 1.0, 0.0, 0.0)
    glRotate(angle, 0.0, 1.0, 0.0)
    glRotate(angle, 0.0, 0.0, 1.0)


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    glFlush()


def eggValues():
    for i in range(0, N + 1):
        for j in range (0, N + 1):
            u = i / N
            v = j / N
            # x
            tab[i][j] = (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * cos(pi * v)
            # y
            tab[i][j][1] = 160 * pow(u, 4) - 320 * pow(u, 3) + 160 * pow(u, 2)
            # z
            tab[i][j][2] = (-90 * pow(u, 5) + 225 * pow(u, 4) - 270 * pow(u, 3) + 180 * pow(u, 2) - 45 * u) * sin(pi * v)


def colorValues():
    for i in range (0, N + 1):
        for j in range (0, N + 1):
            u = i / N
            v = j / N
            tabColor[i][j][0] =  random.uniform(0.0, 1.0)
            tabColor[i][j][1] =  random.uniform(0.0, 1.0)
            tabColor[i][j][2] =  random.uniform(0.0, 1.0)
    
    for i in range (0, int(N / 2) - 1):
        tabColor[N - i][N][0] = tabColor[i][0][0]
        tabColor[N - i][N][1] = tabColor[i][0][1]
        tabColor[N - i][N][2] = tabColor[i][0][2]


def eggPoints():
    glColor(1.0, 1.0, 1.0)
    for i in range(0, N + 1):
        for j in range(0, N + 1):
            glBegin(GL_POINTS)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glEnd()


def eggLines():
    glColor(0.5, 0.5, 0.5)
    for i in range (0, N):
        for j in range (0, N):
            glBegin(GL_LINES)
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
 
            glVertex3f(tab[i][j][0], tab[i][j][1],  tab[i][j][2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])
            glEnd()


def eggTriangles():
    for i in range (0, N):
        for j in range (0, N):
            glBegin(GL_TRIANGLES)
            glColor3f(tabColor[i][j][0], tabColor[i][j][1], tabColor[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])
            
            glColor3f(tabColor[i][j + 1][0], tabColor[i][j + 1][1], tabColor[i][j + 1][2])
            glVertex3f(tab[i][j + 1][0], tab[i][j + 1][1], tab[i][j + 1][2])            
            
            glColor3f(tabColor[i + 1][j][0], tabColor[i + 1][j][1], tabColor[i + 1][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
   
   
            glColor3f(tabColor[i][j+1][0], tabColor[i][j+1][1], tabColor[i][j+1][2])
            glVertex3f(tab[i][j+1][0], tab[i][j+1][1],  tab[i][j+1][2])
           
            glColor3f(tabColor[i + 1][j][0], tabColor[i + 1][j][1], tabColor[i + 1][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1],  tab[i + 1][j][2])
           
            glColor3f(tabColor[i + 1][j + 1][0], tabColor[i + 1][j + 1][1], tabColor[i + 1][j + 1][2])
            glVertex3f(tab[i + 1][j + 1][0], tab[i + 1][j + 1][1], tab[i + 1][j + 1][2])
            glEnd()


def eggTriangleStrip():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range (0, N):
        for j in range (0, N + 1):
            
            glColor3f(tabColor[i][j][0], tabColor[i][j][1], tabColor[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])  
            
            glColor3f(tabColor[i + 1][j][0], tabColor[i + 1][j][1], tabColor[i + 1][j][2])
            glVertex3f(tab[i + 1][j][0], tab[i + 1][j][1], tab[i + 1][j][2])
            
    glEnd()


def render30(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    spin(time * 180 / pi)

    glTranslatef(0, -5, 0)
    eggPoints()

    glFlush()


def render35(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    spin(time * 180 / pi)

    glTranslatef(0, -5, 0)
    eggLines()

    glFlush()


def render40(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    spin(time * 180 / pi)

    glTranslatef(0, -5, 0)
    eggTriangles()

    glFlush()


def render45(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    axes()

    spin(time * 180 / pi)

    glTranslatef(0, -5, 0)
    eggTriangleStrip()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    eggValues()
    colorValues()

    startup()
    while not glfwWindowShouldClose(window):
        # render(glfwGetTime())
        # render30(glfwGetTime())
        # render35(glfwGetTime())
        # render40(glfwGetTime())
        # render45(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
