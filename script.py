import time
import os
import json
from ddgs import DDGS

usrrslt = input("How many results per line would you like? ")

file = open("songs.txt")
line = file.readline()
open("linkoutput.txt", "w")

while line:
    print(line)
    results = DDGS().text(line, max_results=int(usrrslt))
    if results and "href" in results[0]:
        url = results[0]["href"]
        print(url)
        with open("linkoutput.txt", "a") as file:
            file.write(url + "\n")
            file.close()
    else:
        print("No valid results found.")
    

    line = file.readline()


file.close()
