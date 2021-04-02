from cryptography.fernet import Fernet
print(str(Fernet.generate_key()).split('\'')[1])
