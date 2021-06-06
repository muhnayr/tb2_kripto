from Crypto.Util import number
import random


def gcd(a, b):
    return a if (b == 0) else gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


def powmod(a, b, p):
    res = 1
    while (b > 0):
        if (b & 1):
            res = (res * a) % p
        a *= a
        a %= p
        b >>= 1
    return res


def inversmod(a, p):
    return powmod(a, p-2, p)


def getPrimeNbit(n):
    return number.getPrime(n)


def find_primitive_root(p):
    if (p == 2):
        return 1
    else:
        tmp = (p - 1) // 2
        while (True):
            g = random.randint(2, p-1)
            if not(powmod(g, (p-1)//2, p) == 1) and not(powmod(g, (p-1)//tmp, p) == 1):
                return g


def generate_e(phin, num_bits):
    e = getPrimeNbit(num_bits)
    while (gcd(phin, e) != 1):
        # while not coprime
        e = getPrimeNbit(num_bits)
    return e


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
