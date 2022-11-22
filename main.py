from tkinter import *
from PIL import Image

import settings
import utils
from cell import Cell


root = Tk()
# Override the settings of the window
root.configure(bg = "black")
root.geometry("1440x710")
root.title("MummySweeper")
root.resizable(False, False)
root.iconbitmap("./data/mummy_icon.ico")

background_load = PhotoImage(file = "./data/desert_landscape.png")
#mummy = PhotoImage(file = "./data/mummy.png")
#sand = PhotoImage(file = "./data/sand_mound.png")
#cell_button_load = PhotoImage(file = "./data/cell_button.png")

background = Label(root, image = background_load)
background.place(x = 0, y = 0)


"""
im = Image.open("./data/cell_button.png")
size = 40, 40
im.thumbnail(size, Image.Resampling.LANCZOS)
im.save("./test.png", "PNG")
im = PhotoImage(file = "./test.png")




top_frame = Frame(root,
                  bg = "black",
                  width = settings.width,
                  height = utils.height_prct(25),
                  )
top_frame.place(x = 0, y = 0)




left_frame = Frame(root,
                  #bg = "black", 
                  width = utils.width_prct(25),
                  height = utils.height_prct(75),
                  )
left_frame.place(x = 0, y = utils.height_prct(25))
"""


center_frame = Frame(root,
                  bg = "green", 
                  width = utils.width_prct(75),
                  height = utils.height_prct(75),
                  )
center_frame.place(x = utils.width_prct(25), y = utils.height_prct(25))


#Creates grid of cells
for x in range(settings.grid_x):
    for y in range(settings.grid_y):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x, row = y
        )

#Cell.create_cell_count_label(left_frame)
Cell.create_cell_count_label(root)
Cell.cell_count_label_object.place(x = 0, y = 0)

Cell.randomize_mines()

#Run the window
root.mainloop()
