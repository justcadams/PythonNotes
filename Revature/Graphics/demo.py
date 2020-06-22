import pygame
import random
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
)

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

colors = (
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,0),
    (1,0,1),
    (0,1,1)
)

def Cube():
    glBegin(GL_QUADS)
    x = 0
    for surface in surfaces:
        glColor3fv(colors[x])
        x += 1
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    # glBegin(GL_LINES)
    # for edge in edges:
    #     for vertex in edge:
    #         glVertex3fv(vertices[vertex])
    # glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]),0.1,50.0)
    glTranslatef(0.0,0.0,-10)
    while True:
        glRotatef(3,2,1,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(-.1,0,0)
                if event.key == pygame.K_d:
                    glTranslatef(.1,0,0)
                if event.key == pygame.K_w:
                    glTranslatef(0,.1,0)
                if event.key == pygame.K_s:
                    glTranslatef(0,-.1,0)
                if event.key == pygame.K_LEFT:
                    glRotatef(1,2,3,0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(12,8,4,0)
                if event.key == pygame.K_UP:
                    glRotatef(-3,2,1,0)
                if event.key == pygame.K_DOWN:
                    glRotatef(3,-2,1,0)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
