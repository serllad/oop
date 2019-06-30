from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
def init_display_list():
    glNewList(1,GL_COMPILE)
    glPushMatrix()
    glTranslatef(0.,1.,-1.) #move to where we want to put object
    glutSolidSphere(1.,5.,5.) # make radius 1 sphere of res 5x5
    glPopMatrix()
    glEndList()
    return
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
    glRotatef(roty, 0, 1, 0)
    glRotatef(rotx, 1, 0, 0)
    glCallList(1)
    glutSwapBuffers()
    return
glutInit("Hello, World")
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)
glutInitWindowSize(400,400)
glutCreateWindow("Hello, World")
glClearColor(0.,0.,0.,1.)
#glutSetDisplayFuncCallback(display)
glutDisplayFunc(display)
glutMainLoop()