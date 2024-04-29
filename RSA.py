import random
import math

def extended_gcd(a, b):#ax + by = gcd
    if b == 0:
        return a, 1, 0
    gcd, x, y = extended_gcd(b, a % b)
    
    return gcd, y, x - a//b * y

def mod_inverse(a, m):# a x b ≡ 1 (mod n)
    #e x d ≡ (mod phi(n) )
    g, x, y = extended_gcd(a, m)
    
    if(g != 1):
        print('don\'t have inv')
    return x % m

def generate_key(p,q):
    n = p * q
    # phi(n) = phi(p) * phi(q) = (p-1)(q-1)
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    g, _, _= extended_gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g, _, _= extended_gcd(e, phi)
    d = mod_inverse(e,phi)
    return (e, n), (d ,n)

def encrypt(public_key, plaintext):
    #ciphertext = m^e mod n
    e, n = public_key
    if isinstance(plaintext, int):
        return plaintext ** e % n
    elif isinstance(plaintext, (tuple, list)):
        return [s ** e % n for s in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    if isinstance(ciphertext, int):
        return ciphertext ** d % n
    elif isinstance(ciphertext, (tuple, list)):
        return [s ** d % n for s in ciphertext]

def encode_int(str):
    int_list = []
    for i in range (len(str)):
        int_list.append(ord(str[i]))
    return int_list

def decode_chr(nums):
    chr_list = []
    for i in range(len(nums)):
        chr_list.append(chr(nums[i]))
    return "".join(chr_list)

# n > plaintext, 2q > p > q
#The size of plaintext(ascii) should < n, or plaintext will loss when decrypt
def main():
    p, q = 181, 281
    # This p and q are for testing. If you want to ensure information security, please increase the value of p and q. 
    while True:
        print('=================choose the function=================')
        print('                 k.generate key')
        print('                 e.encrypt')
        print('                 d.decrypy')
        print('                 0.end')
        func = input('input the letter to choose the function:')
        
        if func == 'k':
            public_key, private_key = generate_key(p, q)
            tmp1 = ' '.join(map(str, public_key))
            tmp2 = ' '.join(map(str, private_key))
            print(f'public_key:{tmp1},private_key:{tmp2}')

        elif func == 'e':
            plaintext = input('Input your plaintext.(make sure that each char is < p*q):')
            
            while True:
                u_input = input('please input public key, and split e n by a space:')
                try:
                    e, n = map(int,u_input.split())
                    public_key = (e, n)
                    break
                except ValueError:
                    print('Invalid input. Please ensure your two numbers separated by a space.')

            plaintext_int = encode_int(plaintext)
            tmp = ' '.join(map(str, plaintext_int))
            print(f'plaintext(int): {tmp}')
            ciphertext_int = encrypt(public_key, plaintext_int)
            tmp = ' '.join(map(str, ciphertext_int))
            print(f'ciphertext(int): {tmp}')
            ciphertext = decode_chr(ciphertext_int)
            print(f'ciphertext: {ciphertext}')

        elif func == 'd':
            while True:
                try:
                    u_inpur = input('Input your ciphertext(int) which is split by a space:')

                    ciphertext = [int(x.strip()) for x in u_input.split(' ')]
                    break
                except:
                    print('Invalid input. Please ensure your all numbers separated by a space.')


            while True:
                u_input = input('please input private key, and split d n by a space:')
                try:
                    d, n = map(int, u_input.split())
                    private_key = (d, n)
                    break
                except ValueError:
                    print('Invalid input. Please ensure your two numbers separated by a space.')

            plaintext_int = decrypt(private_key, ciphertext_int)
            tmp = ' '.join(map(str, plaintext_int))
            print(f'plaintext(int):{tmp}')
            plaintext = decode_chr(plaintext_int)
            print(f'plaintext:{plaintext}')
        elif func == '0':
            break
        else:
            print('Invalid input')

if __name__ == "__main__":
    main()
