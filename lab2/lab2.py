#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

import random


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


# 4.0 auxiliary function
def drawRectangleDeformed(x, y, a, b, d):

    deformFactor = 1 + d

    # epilepsy warning - rapid colour change
    # random.seed()
    
    # glColor3f(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    glColor3f(d, d, d)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - (0.5 * a) * deformFactor, y - (0.5 * b) * deformFactor)
    glVertex2f(x - (0.5 * a) * deformFactor, y + (0.5 * b) * deformFactor)
    glVertex2f(x + (0.5 * a) * deformFactor, y + (0.5 * b) * deformFactor)
    glEnd()

    # glColor3f(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    glColor3f(d, d, d)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + (0.5 * a) * deformFactor, y + (0.5 * b) * deformFactor)
    glVertex2f(x + (0.5 * a) * deformFactor, y - (0.5 * b) * deformFactor)
    glVertex2f(x - (0.5 * a) * deformFactor, y - (0.5 * b) * deformFactor)
    glEnd()


# 4.0 function
def render40(time):
    glClear(GL_COLOR_BUFFER_BIT)

    x = 0.0
    y = 0.0
    a = 100.0
    b = 70.0
    
    #epilepsy warning - rapid size and colour change
    random.seed()
    d = random.uniform(0.0, 1.0)

    drawRectangleDeformed(x, y, a, b, d)

    glFlush()


# 3.5 auxiliary function
def drawRectangle(x, y, a, b):

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x - 0.5 * a, y - 0.5 * b)
    glVertex2f(x - 0.5 * a, y + 0.5 * b)
    glVertex2f(x + 0.5 * a, y + 0.5 * b)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x + 0.5 * a, y + 0.5 * b)
    glVertex2f(x + 0.5 * a, y - 0.5 * b)
    glVertex2f(x - 0.5 * a, y - 0.5 * b)
    glEnd()


# 3.5 function
def render35(time):
    glClear(GL_COLOR_BUFFER_BIT)

    x = 0.0
    y = 0.0
    a = 100.0
    b = 70.0

    drawRectangle(x, y, a, b)

    glFlush()


# 3.0 function
def render30(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50.0, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-50.0, 0.0)
    glEnd()

    glFlush()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glVertex2f(50.0, 0.0)
    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 50.0)
    glVertex2f(-50.0, 0.0)
    glEnd()

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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

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

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        # render30(glfwGetTime())
        # render35(glfwGetTime())
        # render40(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
