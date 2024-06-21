from pytube import YouTube
from sys import stdout

with open("links.txt", "r") as f:
    links = f.readlines()
    print("Downloading " + str(len(links)) + " videos...")
    count = 0
    for link in links:
        yt = YouTube(link).streams.first().download("./downloads")
        count += 1
        print(f"Downloaded ({count}/{len(links)})")
        stdout.flush()
