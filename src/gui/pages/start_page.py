import tkinter as tk

class StartPage(tk.Frame):
    def donothing(self):
        filewin = tk.Toplevel(self.master)
        button = tk.Button(filewin, text="Do nothing button")
        button.pack()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        heading = tk.Label(
            self,
            bg="white",
            fg="black",
            text='Tugas Besar 2 : Implementasi Algoritma RSA, Elgamal, dan Diffie-Hellman',
            font='none 12 bold'
        )
        heading.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        text_elements = [
            "Encrypt Message with RSA",
            "Decrypt Message with RSA",
            "Generate Key with RSA",
            "Encrypt Message with Elgamal",
            "Decrypt Message with Elgamal",
            "Generate Key With Elgamal",
            "Generate Session Key with Diffie-Hellman",
        ]

        command_elements = [
            lambda: controller.show_frame("RSAEncryptForm"),
            lambda: controller.show_frame("RSADecryptForm"),
            lambda: controller.show_frame("RSAKeyForm"),
            lambda: controller.show_frame("ElgamalEncryptForm"),
            lambda: controller.show_frame("ElgamalDecryptForm"),
            lambda: controller.show_frame("ElgamalKeyForm"),
            lambda: controller.show_frame("DiffieHellmanForm"),
        ]

        index = 0
        for text in text_elements:
            button = tk.Button(
                self,
                bg='white',
                fg='black',
                text=text,
                command=command_elements[index],
                width=50,
                height=2
            )
            button.place(relx=0.5, rely=0.1*(index+2), anchor=tk.CENTER)
            index += 1
