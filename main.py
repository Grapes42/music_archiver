import os
import eyed3

# yt dlp setup
def download_from_youtube(path, link):
    cmd = f"yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format mp3 \"{link}\" -o \"{path}\""
    os.system(cmd)

def add_metadata(path, title, artist, album, track=1):
    d3_file = eyed3.load(f"{path}.mp3")

    d3_file.tag.title = title
    d3_file.tag.artist = artist
    d3_file.tag.album = album
    d3_file.tag.track_num = track
    
    try:
        image_data = open(f"images/{artist}/{album}.jpg", "rb").read()
        d3_file.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")
        print("Image for album found")
    except:
        print("No image for album found")

    d3_file.tag.save()

# Create base folders
if not os.path.exists("music"):
        os.makedirs("music")

if not os.path.exists("map"):
        os.makedirs("map")

if not os.path.exists("images"):
        os.makedirs("images")

map = os.listdir("map")

for artist_file in map:

    artist = artist_file.replace(".txt", "")
    music_path = f"music/{artist}"
    image_path = f"images/{artist}"

    # Create sub-folders
    if not os.path.exists(music_path):
        os.makedirs(music_path)

    if not os.path.exists(image_path):
        os.makedirs(image_path)


    # Read contents of artist file
    with open(f"map/{artist_file}") as f:
        contents = f.read()

    items = contents.split("\n\n")

    for item in items:
        lines = item.split("\n")

        pos = 0
        path = f"music/{artist}"

        album = ""
        
        if "," not in lines[0]:
            album = lines[0].replace(":", "")

            album_folder = f"music/{artist}/{album}"

            if not os.path.exists(album_folder):
                os.makedirs(album_folder)

            path = album_folder
            pos += 1

        if album == "":
            while pos < len(lines):
                title, link = lines[pos].split(", ")
                
                path = f"music/{artist}/{title}"

                download_from_youtube(path=path, link=link)
                
                add_metadata(path=path, 
                             title=title,
                             artist=artist,
                             album=title.replace(" - Album", ""), 
                             track=1)
                
                pos += 1

        else:
            while pos < len(lines):
                title, link = lines[pos].split(", ")

                path = f"{album_folder}/{title}"

                download_from_youtube(path=path, link=link)
                
                add_metadata(path=path,
                             title=title,
                             artist=artist,
                             album=album.replace(" - Album", ""),
                             track=pos)
                
                pos += 1


        