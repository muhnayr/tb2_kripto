import tkinter as tk
import tkinter.filedialog as fd
import src.utils.gui as hg
from src.utils.file import *
from src.algorithm.rsa import RSA


class RSADecryptForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.initialize()

        hg.insert_header(self, 'RSA Decryption')
        self.render_message_frame()
        self.render_text_message_frame()
        self.render_key_frame()
        self.render_text_key_frame()
        self.render_output_frame()
        self.render_execute_frame()

    def initialize(self):
        self.TITLE_ROW = 0
        self.FILE_MESSAGE_ROW = 1
        self.TEXT_MESSAGE_ROW = 2
        self.FILE_KEY_ROW = 5
        self.TEXT_KEY_ROW = 5
        self.OUTPUT_ROW = 7
        self.EXECUTE_ROW = 8

        self.DEFAULT_OUTPUT_NAME = ''
        self.message_dir = tk.StringVar()
        self.message_dir.set('')

        self.key_dir = tk.StringVar()
        self.key_dir.set('')

    def render_message_frame(self):
        message_frame = hg.create_frame(self, self.FILE_MESSAGE_ROW + 1)
        hg.create_label(message_frame, 'Ciphertext File', 0, 0)
        hg.create_label(message_frame, self.message_dir, 0, 1, fix_text=False)
        hg.create_button(message_frame, 'Browse',
                         lambda: self.load_message_file(), 1, 0)

    def render_text_message_frame(self):
        t_message_frame = hg.create_frame(self, self.TEXT_MESSAGE_ROW + 2)
        hg.create_label(t_message_frame,
                        'or write your ciphertext down here:', 0, 0)
        self.text_message = hg.create_text(t_message_frame, '', 10, 70, 1, 0)

    def render_key_frame(self):
        key_frame = hg.create_frame(self, self.FILE_KEY_ROW + 1)
        hg.create_label(key_frame, 'Key File', 0, 0)
        hg.create_label(key_frame, self.key_dir, 0, 1, fix_text=False)
        hg.create_button(key_frame, 'Browse',
                         lambda: self.load_key_file(), 1, 0)

    def render_text_key_frame(self):
        t_key_frame = hg.create_frame(self, self.TEXT_KEY_ROW + 2)
        hg.create_label(
            t_key_frame, 'or write your key down here: (format: d n)', 0, 0)
        self.text_key = hg.create_text(t_key_frame, '', 2, 70, 1, 0)

    def render_output_frame(self):
        output_frame = hg.create_frame(self, self.OUTPUT_ROW + 1)
        hg.create_label(
            output_frame, 'Output file\'s name (if using file):', 0, 0)
        hg.create_label(output_frame, '.txt', 1, 1)
        self.output_name = hg.create_entry(
            output_frame, self.DEFAULT_OUTPUT_NAME, 1, 0
        )

    def render_execute_frame(self):
        execute_frame = hg.create_frame(self, self.EXECUTE_ROW + 1)

        hg.create_button(execute_frame, 'Execute',
                         lambda: self.execute(), 0, 0)

        hg.create_button(execute_frame, 'Back',
                         lambda: self.controller.show_frame("StartPage"), 0, 1)

    def load_message_file(self):
        self.message_dir.set(fd.askopenfilename())

    def load_key_file(self):
        dialog = fd.askopenfilename(
            filetypes=((".pri", "*.pri"),)
        )
        self.key_dir.set(dialog)

    def setup_key(self, key):
        used_key = {
            'private': {
                'd': int(key[0]),
                'n': int(key[1])
            }
        }
        return used_key

    def execute(self):
        print('> Message dir', self.message_dir.get())
        print('> Message text', self.text_message.get("1.0", "end-1c"))
        print('> Key dir', self.key_dir.get())
        print('> Key text', self.text_key.get("1.0", "end-1c"))
        print('> Output filename', self.output_name.get())
        message_dir = self.message_dir.get()
        message_text = self.text_message.get("1.0", "end-1c")
        key_dir = self.key_dir.get()
        key_text = self.text_key.get("1.0", "end-1c")
        output_filename = self.output_name.get()

        try:
            if (message_dir == '' and message_text == ''):
                return
            if (key_dir == '' and key_text == ''):
                return
            if (message_dir != '' and output_filename == ''):
                return

            message = read_file(message_dir) if (message_dir != '') else message_text
            key = read_file(key_dir) if (key_dir != '') else key_text
            key = self.setup_key(key.split(' '))

            rsa = RSA(256, key)
            results = rsa.decrypt(message)
            results = {
                **results, 
                "file_output": output_filename,
                "message_dir": message_dir
            }

            if (output_filename != ''):
                output_filename = f"./output/decrypted/rsa/{output_filename}.txt"
                write_file(output_filename, results["decrypted"])

            title = 'RSA Decryption'
            tipe = 'rsa_decryption'

            self.controller.show_end_frame(title, tipe, results)
        except Exception as e:
            print("Error occured when decrypt using RSA!")
            print(e)
