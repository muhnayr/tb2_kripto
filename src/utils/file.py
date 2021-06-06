import os

def read_file_as_binary(filename):
    try:
        with open(filename, "rb") as f:
            byte_file = f.read()
        return byte_file
    except Exception as e:
        print(str(e))

def write_file_from_binary(filename, byte_file):
    try:
        with open(filename, "wb") as f:
            f.write(byte_file)
    except Exception as e:
        print(str(e))

def read_file(filename):
    try:
        f = open(filename, "r")
        return f.read()
    except Exception as e:
        print(str(e))

def write_file(filename, content):
    try:
        f = open(filename, "w")
        f.write(content)
    except Exception as e:
        print(str(e))

def get_file_size(filename):
    try:
        file_stats = os.stat(filename)
        return f"{file_stats.st_size} bytes"
    except Exception as e:
        print(str(e))

def get_abs_path(filename):
    try:
        abs_path = os.path.abspath(filename)
        return abs_path
    except Exception as e:
        print(str(e))