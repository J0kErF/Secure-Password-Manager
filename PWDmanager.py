import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

backend = default_backend()


def encrypt(message: bytes, public_key_file: str) -> bytes:
    # Load the public key from file
    with open(public_key_file, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # Encrypt the message using RSA encryption with OAEP padding
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted


def decrypt(websitename,username):
    exit()
def addPWD():
    websitename=input("[*] enter website/app name: ")
    print("[*] website/app name: "+websitename+"\n")
    done=0
    while done != 1:
        username=input("[*] enter username: ")
        print("[*] username: "+username+"\n")
        done=int(input("[*] enter 1 to save | 0 to RE-enter username "))
    done=0
    while done != 1:
        PWD=input("[*] enter password: ")
        print("[*] password: "+PWD+"\n")
        done=int(input("[*] enter 1 to save | 0 to RE-enter password "))
    done=int(input("[*] enter 1 to save | anything to CANCEL and EXIT "))
    if done==1:
        line="("+websitename+","+username+","+PWD+")"
        encrypt(line,"public_key.pem")
        
    exit()
def revealPWD():
    websitename=input("[*] enter website/app name: ")
    print("[*] website/app name: "+websitename+"\n")
    done=0
    while done != 1:
        username=input("[*] enter username (or '*' to show all users): ")
        print("[*] username: "+username+"\n")
        done=int(input("[*] enter 1 to proceed | 0 to RE-enter username "))
    done=int(input("[*] enter 1 to proceed | anything to CANCEL and EXIT "))
    if done==1:
        decrypt(websitename,username)
    exit()

def boot():
    os.system('cls' if os.name == 'nt' else 'clear')
    header="\n ______          _      _    _  _  _  _____  ______  _____      ______         ______          ______ _______ ______  \n(_____ \ /\     | |    | |  | || || |/ ___ \(_____ \(____ \    |  ___ \   /\  |  ___ \   /\   / _____|_______|_____ \ \n _____) )  \     \ \    \ \ | || || | |   | |_____) )_   \ \   | | _ | | /  \ | |   | | /  \ | /  ___ _____   _____) )\n|  ____/ /\ \     \ \    \ \| ||_|| | |   | (_____ (| |   | |  | || || |/ /\ \| |   | |/ /\ \| | (___)  ___) (_____ ( \n| |   | |__| |_____) )____) ) |___| | |___| |     | | |__/ /   | || || | |__| | |   | | |__| | \____/| |_____      | |\n|_|   |______(______(______/ \______|\_____/      |_|_____/    |_||_||_|______|_|   |_|______|\_____/|_______)     |_|\n\n\n"
    name="BY\n╔╦╗┌─┐┬ ┬┌─┐┌┬┐┌┬┐┌─┐┌┬┐  ╦ ╦┌─┐┌─┐┌─┐┌─┐\n║║║│ │├─┤├─┤││││││├─┤ ││  ╚╦╝│ │└─┐├┤ ├┤ \n╩ ╩└─┘┴ ┴┴ ┴┴ ┴┴ ┴┴ ┴─┴┘   ╩ └─┘└─┘└─┘└  \n"
    print(header)
    print(name)
    mainlist="[*] Add password\n[*] Reveal password\n[*] Delete password\n[*] EXIT\n"
    print(mainlist)
    x=int(input("choose your option: "))
    if x==1 :
        addPWD()
    elif x==2 :
        revealPWD()
    elif x==3 :
        print("[*] Delete password (in MAINTAINCE)")
    elif x==4 :
        exit()

if __name__=="__main__":
    boot()







