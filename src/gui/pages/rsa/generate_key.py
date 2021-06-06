import tkinter as tk
import src.utils.gui as hg

from src.algorithm.rsa import RSA


class RSAKeyForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initialize()

        self.render_public_frame()
        self.render_private_frame()
        self.render_execute_frame()

    def initialize(self):
        self.TITLE_ROW = 0
        self.PUBLIC_ROW = 1
        self.PRIVATE_ROW = 2
        self.EXECUTE_ROW = 3
        self.PUBLIC_OUTPUT_NAME = 'public'
        self.PRIVATE_OUTPUT_NAME = 'private'

    def render_public_frame(self):
        public_frame = hg.create_frame(self, self.PUBLIC_ROW + 1)
        hg.create_label(public_frame, 'File name for public key:', 0, 0)
        hg.create_label(public_frame, '.pub', 1, 1)
        self.public_name = hg.create_entry(
            public_frame, self.PUBLIC_OUTPUT_NAME, 1, 0
        )

    def render_private_frame(self):
        private_frame = hg.create_frame(self, self.PRIVATE_ROW + 1)
        hg.create_label(private_frame, 'File name for private key:', 0, 0)
        hg.create_label(private_frame, '.pri', 1, 1)
        self.private_name = hg.create_entry(
            private_frame, self.PRIVATE_OUTPUT_NAME, 1, 0
        )

    def render_execute_frame(self):
        execute_frame = hg.create_frame(self, self.EXECUTE_ROW + 1)

        hg.create_button(execute_frame, 'Execute',
                         lambda: self.execute(), 0, 0)

        hg.create_button(execute_frame, 'Back',
                         lambda: self.controller.show_frame("StartPage"), 0, 1)

    def execute(self):
        print('>public key output', self.public_name.get())
        print('>private key output', self.private_name.get())
        public_name = self.public_name.get()
        private_name = self.private_name.get()

        try:
            if (public_name == '' or private_name == ''):
                return

            rsa = RSA(256, '')
            key = rsa.key

            results = {
                **key,
                'execution_time': 10,
                'public_name': public_name,
                'private_name': private_name
            }
            tipe = 'rsa_key'
            title = 'RSA Key Generator'

            self.controller.show_end_frame(title, tipe, results)
        except Exception as e:
            print('Error occured when generate key using RSA!')
            print(e)
