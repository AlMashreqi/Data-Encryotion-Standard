from Crypto.Cipher import DES
import binascii

def add_padding(text, blocksize=64):
    pad_len = blocksize - (len(text) % blocksize)
    padding = '$' * pad_len
    return text + padding

def remove_padding(str, block_size=64):
     count = 0

     for chr in str[::-1]:
         if chr == '$':
             count += 1

         else:
             break

     return str[:-count]

def encrypt(plaintext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.encrypt(plaintext)

def decrypt(ciphertext, key):
    des = DES.new(key, DES.MODE_ECB)
    return des.decrypt(ciphertext).decode('UTF-8')


if __name__ == '__main__':
    key = 'sauoodxx'
    plaintext = "This is called being based"
    plaintext = add_padding(plaintext)
    print(len(plaintext))
    cipher = encrypt(plaintext, key)
    print(binascii.hexlify(bytearray(cipher)))