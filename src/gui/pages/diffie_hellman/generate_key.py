import tkinter as tk
import src.utils.gui as hg

from src.algorithm.diffie_hellman import DiffieHellman

class DiffieHellmanForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initialize()

        hg.insert_header(self, 'Diffie-Hellman Algorithm')
        self.render_n_frame()
        self.render_g_frame()
        self.render_x_frame()
        self.render_y_frame()
        self.render_execute_frame()

    def initialize(self):
        self.TITLE_ROW = 0
        self.N_ROW = 1
        self.G_ROW = 2
        self.X_ROW = 3
        self.Y_ROW = 4
        self.EXECUTE_ROW = 5
    
    def render_n_frame(self):
        n_frame = hg.create_frame(self, self.N_ROW + 1)
        hg.create_label(n_frame, 'n', 0, 0)
        self.n_name = hg.create_entry(n_frame, '', 1, 0)
    
    def render_g_frame(self):
        g_frame = hg.create_frame(self, self.G_ROW + 1)
        hg.create_label(g_frame, 'g', 0, 0)
        self.g_name = hg.create_entry(g_frame, '', 1, 0)
    
    def render_x_frame(self):
        x_frame = hg.create_frame(self, self.X_ROW + 1)
        hg.create_label(x_frame, 'x', 0, 0)
        self.x_name = hg.create_entry(x_frame, '', 1, 0)
    
    def render_y_frame(self):
        y_frame = hg.create_frame(self, self.Y_ROW + 1)
        hg.create_label(y_frame, 'y', 0, 0)
        self.y_name = hg.create_entry(y_frame, '', 1, 0)
    
    def render_execute_frame(self):
        execute_frame = hg.create_frame(self, self.EXECUTE_ROW + 1)

        hg.create_button(execute_frame, 'Execute',
                         lambda: self.execute(), 0, 0)

        hg.create_button(execute_frame, 'Back',
                         lambda: self.controller.show_frame("StartPage"), 0, 1)

    def execute(self):
        print('> n value', self.n_name.get())
        print('> g value', self.g_name.get())
        print('> x value', self.x_name.get())
        print('> y value', self.y_name.get())
        n = self.n_name.get()
        g = self.g_name.get()
        x = self.x_name.get()
        y = self.y_name.get()
        
        try:
            if (n == '' or g == '' or x == '' or y == ''):
                return
            n = int(n)
            g = int(g)
            x = int(x)
            y = int(y)

            dh = DiffieHellman(n, g, x, y)
            session_key = dh.session_key
            results = {
                "session_key": session_key
            }
            title = 'Diffie-Hellman Algorithm'
            tipe = 'diffie_hellman'

            self.controller.show_end_frame(title, tipe, results)
        except Exception as e:
            print('Error occured when generate session key!')
            print(e)