from tkinter import *
from PIL import Image, ImageTk
class vector:
    def __init__(self,X,Y):
        self.X = X
        self.Y = Y
    
    def __add__(self, newVec):
        return vector(self.X+newVec.X,self.Y+newVec.Y)
    
    def __repr__(self):
        return f"Vector({self.X}, {self.Y})"
    
class coord:
    def __init__(self,coordX,coordY):
        self.coordX = coordX
        self.coordY = coordY
    def __add__(self, vec):
        if isinstance(vec, vector):
            return coord(self.coordX + vec.X, self.coordY + vec.Y)  
    def __repr__(self):
        return f"Coords({self.coordX}, {self.coordY})"
event = Event()

# window
game_window = Tk()
game_window.resizable(False,False)
game_window.geometry("500x400")
game_window.title("Flappybird On Python :D")
game_window.config(bg="black")
#inside window
frame = Frame(game_window,width=875,height=575)
frame.pack(fill="both",anchor="center",expand=True)
frame.config(bg="skyblue")
#   character
character_location = coord(100,200)
#       character_image
adjust_character_image = Image.open("birb.png").resize((100,100))
character_image = ImageTk.PhotoImage(adjust_character_image)
character_label = Label(master=frame,image=character_image)
character_label.place(x=character_location.coordX,y=character_location.coordY)
# PIPES
top_pipeCoords = coord(200,0)
top_pipe_label = Label(master=frame,bg="green",width=8,height=12)
top_pipe_label.place(x=top_pipeCoords.coordX,y=top_pipeCoords.coordY)

bottom_pipeCoords = coord(500,160)
bottom_pipe_label = Label(master=frame,bg="green",width=8,height=16)
bottom_pipe_label.place(x=bottom_pipeCoords.coordX,y=bottom_pipeCoords.coordY)
# Macros
#   GRAVITY
gravity = vector(0,2)
#   CHARACTER
jump_velocity = vector(0,-25)
velocity = vector(0,0)
#   PIPES
pipes_velocity = vector(-2.8,0)
#   GAME STATE
game_over = False
#METHODS
def gravity_fun():
    if game_over:
        return 
    global character_location, gravity, velocity
    velocity +=gravity
    character_location = character_location + velocity
    character_label.place(x=character_location.coordX, y=character_location.coordY)
    checking_collision()
    game_window.after(50,gravity_fun)
def jump(event):
    global velocity
    velocity = velocity + jump_velocity

def moving_pipes():
    if game_over:
        return 
    global pipes_velocity,top_pipe_label, top_pipeCoords, bottom_pipe_label, bottom_pipeCoords

    top_pipeCoords = top_pipeCoords + pipes_velocity
    top_pipe_label.place(x=top_pipeCoords.coordX,y=top_pipeCoords.coordY)

    bottom_pipeCoords = bottom_pipeCoords + pipes_velocity
    bottom_pipe_label.place(x=bottom_pipeCoords.coordX,y=bottom_pipeCoords.coordY)

    checking_collision()

    if (top_pipeCoords.coordX <= -80):
        top_pipeCoords.coordX = 500
        top_pipeCoords.coordY = 0
    if(bottom_pipeCoords.coordX <= -80):
        bottom_pipeCoords.coordX = 500
        bottom_pipeCoords.coordY = -100
    game_window.after(50,moving_pipes)

def show_game_over():
    global game_window
    game_over_label = Label(game_window, text="PERDISTE :(", font=("Arial", 24), fg="red")
    game_over_label.place(x=130, y=150)

def checking_collision():
    global game_over
    if(
        character_location.coordX + 50 > top_pipeCoords.coordX and
        character_location.coordX < top_pipeCoords.coordX + 60 and
        character_location.coordY < top_pipeCoords.coordY + 150
       ):
        show_game_over()
        game_over = True
    if(
        character_location.coordX + 50 > bottom_pipeCoords.coordX and
        character_location.coordX < bottom_pipeCoords.coordX + 60 and
        character_location.coordY + 100 > bottom_pipeCoords.coordY
    ):
        show_game_over()
        game_over = True

game_window.bind("<space>",jump)
game_window.after(50,gravity_fun)
game_window.after(50,moving_pipes)
game_window.mainloop()
