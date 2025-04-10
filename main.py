import os
import shelve
import eyed3

from classes import *

# yt dlp setup
def download_from_youtube(title, link):
    cmd = f"yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format mp3 \"{link}\" -o \"{title}\""
    os.system(cmd)

def store_artist(artist):
    shelve_file = shelve.open(f"artists/{artist.title}")
    shelve_file["artist"] = artist
    shelve_file.close()

def retrieve_artist(artist_name):
    shelve_file = shelve.open(f"artists/{artist_name}")
    artist = shelve_file["artist"]
    shelve_file.close()

    return artist

def add_metadata(path, title, artist, album, track=1):
    d3_file = eyed3.load(path)

    d3_file.tag.title = title
    d3_file.tag.artist = artist
    d3_file.tag.album = album
    d3_file.tag.track_num = track
    
    try:
        image_data = open(f"{artist}/{album}.jpg", "rb").read()
        d3_file.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")
        print("Image for album found")
    except:
        print("No image for album found")

    d3_file.tag.save()

# Main loop
if not os.path.exists("artists"):
    os.makedirs("artists")

butcher_md = Artist(title="Butcher M.D.")
butcher_md.add_file(title="Traces of Gore - Album", link="https://www.youtube.com/watch?v=fSCv6MswW8E")

store_artist(butcher_md)

butcher_md_2 = retrieve_artist("Butcher M.D.")
print(butcher_md_2)