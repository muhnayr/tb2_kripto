import tkinter as tk
import src.utils.gui as hg

from src.utils.file import write_file, get_file_size, get_abs_path


class EndPage(tk.Frame):
    def __init__(self, parent, controller, title, tipe, results):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        heading = tk.Label(
            self,
            bg="white",
            fg="black",
            text=title,
            font='none 16 bold'
        )
        heading.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        if (tipe == 'elgamal_key'):
            output_frame = hg.create_frame(self, 3)
            pub_key = results["public"]
            pri_key = results["private"]
            pub_output = results['public_name']
            pri_output = results['private_name']

            hg.create_label(output_frame, "Public Key (format: y g p)", 0, 0)
            public_key = f"{pub_key['y']} {pub_key['g']} {pub_key['p']}"
            hg.create_text(output_frame, public_key, 5, 70, 1, 0)
            hg.create_button(output_frame, 'Save Public Key!', lambda: self.save_key(
                True, pub_output, public_key, "elgamal"), 6, 0)

            hg.create_label(output_frame, "Private Key (format: x p)", 7, 0)
            private_key = f"{pri_key['x']} {pri_key['p']}"
            hg.create_text(output_frame, private_key, 5, 70, 8, 0)
            hg.create_button(output_frame, 'Save Private Key!', lambda: self.save_key(
                False, pri_output, private_key, "elgamal"), 9, 0)
        elif (tipe == 'rsa_key'):
            output_frame = hg.create_frame(self, 3)
            pub_key = results["public"]
            pri_key = results["private"]
            pub_output = results['public_name']
            pri_output = results['private_name']

            hg.create_label(output_frame, "Public Key (format: e n)", 0, 0)
            public_key = f"{pub_key['n']} {pub_key['e']}"
            hg.create_text(output_frame, public_key, 5, 70, 1, 0)
            hg.create_button(output_frame, 'Save Public Key!', lambda: self.save_key(
                True, pub_output, public_key, "rsa"), 6, 0)

            hg.create_label(output_frame, "Private Key (format: d n)", 7, 0)
            private_key = f"{pri_key['d']} {pri_key['n']}"
            hg.create_text(output_frame, private_key, 5, 70, 8, 0)
            hg.create_button(output_frame, 'Save Private Key!', lambda: self.save_key(
                False, pri_output, private_key, "rsa"), 9, 0)
        elif (tipe == 'diffie_hellman'):
            output_frame = hg.create_frame(self, 3)
            session_key = results['session_key']

            hg.create_label(output_frame, "Generated Session Key:", 0, 0)
            hg.create_text(output_frame, session_key, 5, 70, 1, 0)
        else:
            execution_time = results['execution_time']
            message = results['encrypted'] if (
                'encrypted' in results) else results['decrypted']
            path_type = 'encrypted' if (
                'encrypted' in results) else 'decrypted'
            file_output = results['file_output']
            message_dir = results['message_dir']
            result_message = 'Encryption Result' if (
                path_type == 'encrypted') else 'Decryption Result'
            algo_type = 'rsa' if ('rsa' in tipe) else 'elgamal'

            output_frame = hg.create_frame(self, 3)
            if (message_dir != ''):
                hg.create_label(
                    output_frame, f"Saved to output/{path_type}/{algo_type}/{file_output}.txt!", 0, 0)
                hg.create_label(
                    output_frame, f"Time execution is {execution_time}", 12, 0)
                abs_path = get_abs_path(
                    f"output/{path_type}/{algo_type}/{file_output}.txt")
                file_size = get_file_size(abs_path)
                hg.create_label(
                    output_frame, f"File size is {file_size}", 13, 0)
            elif (message_dir == '' and file_output != ''):
                hg.create_label(
                    output_frame, f"Saved to output/{path_type}/{algo_type}/{file_output}.txt!", 2, 0)
                hg.create_label(output_frame, result_message, 3, 0)
                hg.create_text(output_frame, message, 8, 70, 4, 0)
                hg.create_label(
                    output_frame, f"Time execution is {execution_time}", 12, 0)
                abs_path = get_abs_path(
                   f"output/{path_type}/{algo_type}/{file_output}.txt")
                file_size = get_file_size(abs_path)
                hg.create_label(
                    output_frame, f"File size is {file_size}", 13, 0)
            else:
                hg.create_label(output_frame, result_message, 0, 0)
                hg.create_text(output_frame, message, 10, 70, 1, 0)
                hg.create_label(
                    output_frame, f"Time execution is {execution_time}", 12, 0)

        back_frame = hg.create_frame(self, 6)
        hg.create_button(back_frame, 'Back',
                         lambda: self.controller.show_frame("StartPage"), 0, 0)

    def save_key(self, is_public, filename, content, algotype):
        filename = "./test-data/keys/" + algotype + "/" + filename
        filename += '.pub' if (is_public) else '.pri'
        write_file(filename, content)
