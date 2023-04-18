import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

backend = default_backend()


def encrypt(data, shift):
    result = ""
    for char in data:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result


def decrypt(websitename, username):
    count = 1
    num = 1
    with open("data.txt", "r") as f:
        for line in f:
            if encrypt(line, -1*count).split(',')[0] == websitename:
                if username == "*" or username == encrypt(line, -1*count).split(',')[1]:
                    print(str(num)+": ")
                    print("[*] username: "+encrypt(line, -1*count).split(',')[1])
                    print("[*] password: "+encrypt(line, -1*count).split(',')[2])
                    num += 1
            count += 1


def addPWD():
    websitename = input("[*] enter website/app name: ")
    print("[*] website/app name: "+websitename+"\n")
    done = 0
    while done != 1:
        username = input("[*] enter username: ")
        print("[*] username: "+username+"\n")
        done = int(input("[*] enter 1 to save | 0 to RE-enter username "))
    done = 0
    while done != 1:
        PWD = input("[*] enter password: ")
        print("[*] password: "+PWD+"\n")
        done = int(input("[*] enter 1 to save | 0 to RE-enter password "))
    if done == 1:
        data = websitename+","+username+","+PWD
        count = 1
        
        with open("data.txt", "r") as f:
            for line in f:
                count += 1
        data = encrypt(line, count)
        with open("data.txt", "a") as f:
            f.write(data+"\n")

    exit()


def revealPWD():
    websitename = input("[*] enter website/app name: ")
    print("[*] website/app name: "+websitename+"\n")
    done = 0
    while done != 1:
        username = input("[*] enter username (or '*' to show all users): ")
        print("[*] username: "+username+"\n")
        done = int(input("[*] enter 1 to proceed | 0 to RE-enter username "))
    if done == 1:
        decrypt(websitename, username)
    exit()


def boot():
    os.system('cls' if os.name == 'nt' else 'clear')
    header = "\n ______          _      _    _  _  _  _____  ______  _____      ______         ______          ______ _______ ______  \n(_____ \ /\     | |    | |  | || || |/ ___ \(_____ \(____ \    |  ___ \   /\  |  ___ \   /\   / _____|_______|_____ \ \n _____) )  \     \ \    \ \ | || || | |   | |_____) )_   \ \   | | _ | | /  \ | |   | | /  \ | /  ___ _____   _____) )\n|  ____/ /\ \     \ \    \ \| ||_|| | |   | (_____ (| |   | |  | || || |/ /\ \| |   | |/ /\ \| | (___)  ___) (_____ ( \n| |   | |__| |_____) )____) ) |___| | |___| |     | | |__/ /   | || || | |__| | |   | | |__| | \____/| |_____      | |\n|_|   |______(______(______/ \______|\_____/      |_|_____/    |_||_||_|______|_|   |_|______|\_____/|_______)     |_|\n\n\n"
    name = "BY\n╔╦╗┌─┐┬ ┬┌─┐┌┬┐┌┬┐┌─┐┌┬┐  ╦ ╦┌─┐┌─┐┌─┐┌─┐\n║║║│ │├─┤├─┤││││││├─┤ ││  ╚╦╝│ │└─┐├┤ ├┤ \n╩ ╩└─┘┴ ┴┴ ┴┴ ┴┴ ┴┴ ┴─┴┘   ╩ └─┘└─┘└─┘└  \n"
    print(header)
    print(name)
    mainlist = "[*] Add password\n[*] Reveal password\n[*] Delete password\n[*] EXIT\n"
    print(mainlist)
    x = int(input("choose your option: "))
    if x == 1:
        addPWD()
    elif x == 2:
        revealPWD()
    elif x == 3:
        print("[*] Delete password (in MAINTAINCE)")
    elif x == 4:
        exit()


if __name__ == "__main__":
    boot()
