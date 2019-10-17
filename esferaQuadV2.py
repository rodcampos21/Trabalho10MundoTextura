from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

m = 50
r = 3

def pontoEsfera(i,j):
    theta = (i * math.pi/m) - (math.pi/2)
    phi = (j * 2 * math.pi)/m
    x = r * math.cos(theta) * math.cos(phi)
    y = r * math.sin(theta)
    z = r * math.cos(theta) * math.sin(phi)
    return x,y,z

def Esfera():
   glBegin(GL_QUAD_STRIP)
   for i in range(0,m+1):
      glColor3f(1,i/(1.0*m),1-(i/(1.0*m)))
      for j in range(0,m+1):
         glVertex3fv(pontoEsfera(i,j))
         glVertex3fv(pontoEsfera(i+1,j))
   glEnd()
 
  
def desenha():
   glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
   glRotatef(10,0,0,1)
   Esfera()
   glutSwapBuffers()


def timer(i):
   glutPostRedisplay()
   glutTimerFunc(50,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()