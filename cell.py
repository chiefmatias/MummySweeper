import random
from tkinter import Button, Label

import settings
import utils


class Cell:
    all = []
    cell_count_label_object = None
    
    def __init__(self, x, y, is_mine = False, is_open = False, is_flagged = False):
        self.x = x
        self.y = y        
        self.is_mine = is_mine
        self.is_flagged = is_flagged
        self.cell_btn_object = None
        self.is_open = is_open
        
        #Recording object in Cell.all list 
        Cell.all.append(self)
        
        
    def create_btn_object(self, location):
        btn = Button(
            location,
            bg = "white",
            width = int(utils.width_prct(0.83)),
            height = int(utils.height_prct(0.6))
        )
        btn.bind("<Button-1>", self.left_click_actions) #Left Click
        btn.bind("<Button-3>", self.right_click_actions) #Right Click
        self.cell_btn_object = btn
        
    
    @staticmethod 
    def create_cell_count_label(location):
        lbl = Label(
            location,
            #bg = "black",
            #fg = "white",
            text = f"Cells Left: {settings.cell_count}",
            width = int(utils.width_prct(0.83)),
            height = int(utils.height_prct(0.6)),
            font = ("", 30)
        )
        Cell.cell_count_label_object = lbl
        return lbl
 
    def left_click_actions(self, event):
        if not self.is_flagged and not self.is_open:
            if self.is_mine:
                self.show_mine()
                
            else:
                self.show_cell()
                self.flood_fill()
               
     
    def flood_fill(self):
        if self.surrounded_cells_mines_count == 0:
                    for cell in self.surrounded_cells:
                        if cell.is_open == True or cell.is_flagged == True:
                            continue
                        cell.show_cell()
                        cell.flood_fill()                        
            
                

            
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        surrounded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        
        surrounded_cells = [cell for cell in surrounded_cells if cell is not None]
        return surrounded_cells
        
    @property
    def surrounded_cells_mines_count(self):
        """Counts the ammount of mines surrounding current cell"""
        
        counter = 0        
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):   
        if not self.is_open and not self.is_flagged:
            settings.cell_count -= 1
            self.is_open = True
            self.cell_btn_object.configure(
                text = self.surrounded_cells_mines_count,
                )
            
            #Update cell count label
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text = f"Cells Left: {settings.cell_count}",)
        
            
            
            
    def show_mine(self):
        # Should display message that player lost and interrupt the game.
        # Temp changes the color
        if not self.is_open:
            self.is_open = True
            self.cell_btn_object.configure(bg = "red")

            for cell in self.all:
                if cell.is_mine:
                    cell.show_mine()

                else:
                    if cell.is_flagged:
                        cell.is_flagged = False
                        #cell.cell_btn_object.configure(bg = "white")
                    cell.show_cell()

            
        
       
        
    def right_click_actions(self, event):
        if not self.is_open:   
            if not self.is_flagged:
                self.is_flagged = True
                self.cell_btn_object.configure(bg = "grey")
                settings.cell_count -= 1
                
        
            else:
                self.is_flagged = False
                self.cell_btn_object.configure(bg = "white")
                settings.cell_count += 1
        
        if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text = f"Cells Left: {settings.cell_count}",)
        
       
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.mines_count)
        
        for cell in picked_cells:
            cell.is_mine = True
        
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"