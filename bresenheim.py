import OpenGL.GL as gl
import OpenGL.GLUT as glut

x1 = 0
y1 = 0
x2 = 0
y2 = 0


def init():
    gl.glClearColor(0.0, 0.0, 1.0, 1.0)  # Set display-window color to black
    gl.glMatrixMode(gl.GL_PROJECTION)  # Set projection parameters
    gl.glLoadIdentity()
    gl.glOrtho(0.0, 200.0, 0.0, 150.0, -1.0, 1.0)  # Set an orthographic projection


def plotPoint(point):
    gl.glPointSize(2)
    gl.glClearColor(1.0, 0.0, 0.0, 1.0)
    gl.glBegin(gl.GL_POINTS)
    gl.glVertex2iv(point)  # Point 1
    gl.glEnd()
    gl.glFlush()


# def bresenham(x1, y1, x2, y2):
def bresenhamLine():
    global x1, y1, x2, y2
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    if abs(dy) < abs(dx):
        p = 2 * dy - dx
        for i in range(dx):
            plotPoint((x, y))
            x += 1
            if p < 0:
                p += 2 * dy
            else:
                y += 1
                p += 2 * dy - 2 * dx
    else:
        p = 2 * dx - dy
        for i in range(dy):
            plotPoint((x, y))
            y += 1
            if p < 0:
                p += 2 * dx
            else:
                x += 1
                p += 2 * dx - 2 * dy
    plotPoint((x2, y2))



def main():
    print("Enter the line end coordinates:")
    global x1, y1, x2, y2
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    glut.glutInit()  # Initialize GLUT
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)  # Set display mode
    glut.glutInitWindowPosition(50, 300)  # Set top-left display-window position
    glut.glutInitWindowSize(400, 300)  # Set display-window width and height
    glut.glutCreateWindow("An Example OpenGL Program")  # Create display window
    init()  # Execute initialization procedure

    glut.glutDisplayFunc(bresenhamLine)  # Register display callback function to display graphics
    glut.glutMainLoop()  # Display everything and wait


main()