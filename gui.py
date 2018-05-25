from tkinter import *

##########initial functions#############
def init(data):
    print("init")
    data.textX = data.width/2
    data.textY = data.height/2
    data.rectX1 = data.width/3
    data.rectY1 = data.height/2 - 100
    data.rectY2 = data.height/2 - 40
    data.rectX2 = 2*data.width/3

#######################################
def mousePressed(event, data):
    print("mousePressed")
    if (data.mode == "startScreen"): start_mousePressed(event, data)
    else: filter_mousePressed(event, data)

def keyPressed(event, data):
    print("keyPressed")
    if (data.mode == "startScreen"): start_keyPressed(event, data)
    else: filter_keyPressed(event, data)

def redrawAll(canvas, data):
    print("redrawAll")
    if (data.mode == "startScreen"): start_redrawAll(canvas, data)
    else: filter_redrawAll(canvas, data)

#######################################
def start_mousePressed(event, data):
    print("start_mousePressed")
    pass

def start_keyPressed(event, data):
    print("start_keyPressed")
    if (event.keysym == "Return"):
        data.mode = "filterScreen"

def start_redrawAll(canvas, data):
    print("start_redrawAll")

#######################################
#for filter Screen
def filter_mousePressed(event, data):
    print("filter_mousePressed")
    if (event.x < data.textX - 20 and event.y > data.textY + 20):
        data.mode = "startScreen"

def filter_keyPressed(event, data):
    print("filter_keyPressed")
    pass

def filter_redrawAll(canvas, data):
    print("filter_redrawAll")
    canvas.create_text(data.width/2, 20,
                       text="Example")

#######################################
def run(data):
    print("run")
    def redrawAllWrap(canvas, data):
        canvas.delete("all")
        canvas.create_rectangle(0,0, data.width, data.height, 
                                fill='white', width = 0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrap(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrap(canvas, data)

    def keyPressedWrap(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrap(canvas, data)

    # Set up data and call init
    root = Tk()
    root.title("Credit Suisse Error Log")
    print("mode: ", data.mode)
    init(data)
    if (data.mode == "startScreen"):
    #b1 thru b5 serve as buffers between text
        b1 = Label(root, bg = "white")
        b1.pack(anchor = CENTER)
        b2 = Label(root, bg = "white")
        b2.pack(anchor = CENTER)
        b3 = Label(root, bg = "white")
        b3.pack(anchor = CENTER)
        L1 = Label(root, text="Enter error filters you'd like to subscribe to: ", bg = "SteelBlue1")
        L1.pack(anchor = CENTER)
        L2 = Label(root, text="Errors: Trace, Debug, Info, Warning, Error, Fatal, Off", bg = "SteelBlue3")
        L2.pack(anchor = CENTER)
        b4 = Label(root, bg = "white")
        b4.pack(anchor = CENTER)
        E1 = Entry(root, bd = 5)
        E1.pack(anchor = CENTER)
        E2 = Entry(root, bd = 5)
        E2.pack(anchor = CENTER)
        E3 = Entry(root, bd = 5)
        E3.pack(anchor = CENTER)
        E4 = Entry(root, bd = 5)
        E4.pack(anchor = CENTER)
        E5 = Entry(root, bd = 5)
        E5.pack(anchor = CENTER)
        E6 = Entry(root, bd = 5)
        E6.pack(anchor = CENTER)
        E7 = Entry(root, bd = 5)
        E7.pack(anchor = CENTER)
        b5 = Label(root, bg = "white")
        b5.pack(anchor = CENTER)
        I1 = Label(root, text="Hit 'Enter' when you are done.")
        I1.pack(anchor = CENTER)
    if (data.mode == "filterScreen"):
        b1 = Label(root, bg = "white")
        b1.pack(anchor = CENTER)
        b2 = Label(root, bg = "white")
        b2.pack(anchor = CENTER)
        b3 = Label(root, bg = "white")
        b3.pack(anchor = CENTER)
        L1 = Label(root, text="Enter error log text file: ", bg = "SteelBlue1")
        L1.pack(anchor = CENTER)
        E1 = Entry(root, bd = 5)
        E1.pack(anchor = CENTER)
        b5 = Label(root, bg = "white")
        b5.pack(anchor = CENTER)
        I1 = Label(root, text="Hit 'Enter' when you are done.")
        I1.pack(anchor = CENTER)

    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrap(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrap(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed

class Struct(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.mode = "filterScreen"
data = Struct(1200, 1200)
run(data)

