from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()


def encrypt_file(file_path, key):
    cipher_suite = Fernet(key)

    with open(file_path, 'rb') as file:
        file_path = file.read()

    encrypted_data = cipher_suite.encrypt(file_data)


    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(encrypt_file_path, key):
    cipher_suite = Fernet(key)

    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(encrypted_file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)


key = generate_key()

encrypt_file('myfile.txt', key)

# decrypt_file('myfile.txt.enc',key)