import hashlib
import os, struct
from Crypto.Cipher import AES


class Aes(object):
    password = 'idhantmohit'.encode(encoding='UTF-8', errors='strict') #can be changed later
    key = hashlib.sha256(password).digest()
    mode = AES.MODE_CBC

    @classmethod
    def decrypt_file(cls, key=key,in_filename=None, out_filename=None, chunksize=24 * 1024):
        if not in_filename:
            raise('Please enter the file path')
        if not out_filename:
            out_filename = os.path.splitext(in_filename)[0]
        with open(in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(out_filename, 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)

    @classmethod
    def encrypt_file(cls, key=key, in_filename=None, out_filename=None, chunksize=64 * 1024):
        if not in_filename:
            raise('Please enter the input file')
        if not out_filename:
            out_filename = in_filename + '.enc'
        iv = str.encode('This is an IV456')
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(in_filename)
        with open(in_filename, 'rb') as infile:
            with open(out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += str.encode(' ' * (16 - len(chunk) % 16))
                    outfile.write(encryptor.encrypt(chunk))
