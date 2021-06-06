import tkinter as tk

from src.gui.pages.start_page import StartPage
from src.gui.pages.end_page import EndPage
from src.gui.pages.elgamal.encrypt_form import ElgamalEncryptForm
from src.gui.pages.elgamal.decrypt_form import ElgamalDecryptForm
from src.gui.pages.elgamal.generate_key import ElgamalKeyForm
from src.gui.pages.diffie_hellman.generate_key import DiffieHellmanForm
from src.gui.pages.rsa.generate_key import RSAKeyForm
from src.gui.pages.rsa.encrypt_form import RSAEncryptForm
from src.gui.pages.rsa.decrypt_form import RSADecryptForm

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
            StartPage, 
            ElgamalEncryptForm, 
            ElgamalKeyForm, 
            ElgamalDecryptForm, 
            DiffieHellmanForm, 
            RSAKeyForm,
            RSAEncryptForm,
            RSADecryptForm
        ):
            page_name = F.__name__

            frame = F(parent=self.container, controller=self)
            frame.configure(bg='white')
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_end_frame(self, title, tipe, results):
        frame = EndPage(
            parent=self.container, 
            controller=self,
            title = title,
            tipe = tipe,
            results = results
        )
        frame.configure(bg='white')
        frame.grid(row=0, column=0, sticky="nsew")