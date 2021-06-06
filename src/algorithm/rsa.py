from src.utils.math import *
from src.utils.file import *
from timeit import default_timer as timer


class RSA():
    def __init__(self, num_bits, key):
        self.num_bits = num_bits
        self.key = key if (len(key) > 0) else self.generate_key()

    def encode(self, plaintext):
        bytes_array = bytearray(plaintext, 'utf-16')
        encoded = []
        byte_size = self.num_bits // 8
        idx_encoded = -byte_size

        for i in range(len(bytes_array)):
            if (i % byte_size == 0):
                idx_encoded += byte_size
                encoded.append(0)
            val = (2 ** (8 * (i % byte_size)))
            encoded[idx_encoded//byte_size] += bytes_array[i] * val

        return encoded

    def decode(self, plaintext):
        bytes_array = []
        byte_size = self.num_bits // 8

        for num in plaintext:
            for i in range(byte_size):
                temp = num
                for j in range(i+1, byte_size):
                    temp = temp % (2 ** (8 * j))
                letter = temp // 2 ** (8 * i)
                bytes_array.append(letter)
                num -= (letter * (2 ** (8 * i)))

        decoded_text = bytearray(b for b in bytes_array).decode('utf-16')
        return decoded_text

    def generate_key(self):
        p1 = getPrimeNbit(self.num_bits)
        p2 = getPrimeNbit(self.num_bits)
        n = p1 * p2
        phin = (p1-1)*(p2-1)
        e = generate_e(phin, self.num_bits)
        d = egcd(e, phin)[1]
        d = d % phin
        if (d < 0):
            d += phin

        public_key = {'n': n, 'e': e}
        private_key = {'d': d, 'n': n}

        return {'public': public_key, 'private': private_key}

    def encrypt(self, plaintext):
        st_time = timer()

        encoded = self.encode(plaintext)
        ciphers = []
        n, e = self.key['public'].values()

        for val in encoded:
            ciphr = powmod(val, e, n)
            ciphers.append(ciphr)

        encrypted_str = ""
        for cipher in ciphers:
            encrypted_str += str(cipher) + ' '

        end_time = timer()
        execution_time = "{:.20f}".format((end_time - st_time))

        return {
            "encrypted": encrypted_str,
            "execution_time": f"{execution_time} seconds"
        }

    def decrypt(self, ciphertext):
        st_time = timer()
        plaintext = []
        ciphers_array = ciphertext.split()
        d, n = self.key['private'].values()

        for i in range(len(ciphers_array)):
            plain = powmod(int(ciphers_array[i]), d, n)
            plaintext.append(plain)

        decrypted_str = self.decode(plaintext)
        decrypted_str = "".join([ch for ch in decrypted_str if (ch != '\x00')])

        end_time = timer()
        execution_time = "{:.20f}".format((end_time - st_time))

        return {
            "decrypted": decrypted_str,
            "execution_time": f"{execution_time} seconds"
        }

    def save_key(self, is_public, filename):
        filename += '.pub' if is_public else '.pri'
        key_type = 'public' if is_public else 'private'

        write_file(filename, self.key[key_type])

