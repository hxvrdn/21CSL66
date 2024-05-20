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


# def ddaLine(x1, y1, x2, y2):
def ddaLine():
    global x1, y1, x2, y2
    m = (y2 - y1) / (x2 - x1)
    if m < 1:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y = y1
        for x in range(x1, x2):
            plotPoint((x, int(y)))
            y += m
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        x = x1
        for y in range(y1, y2):
            plotPoint((int(x), y))
            x += 1 / m


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

    glut.glutDisplayFunc(ddaLine)  # Register display callback function to display graphics
    glut.glutMainLoop()  # Display everything and wait


main()