import os
import eyed3

# yt dlp setup
def download_from_youtube(path, link):
    cmd = f"yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format mp3 \"{link}\" -o \"{path}\""
    os.system(cmd)

def add_metadata(path, title, artist, album, track):
    d3_file = eyed3.load(f"{path}.mp3")

    d3_file.tag.title = title
    d3_file.tag.artist = artist
    d3_file.tag.album = album
    d3_file.tag.track_num = track

    image_path = f"images/{artist}/{album}.jpg"

    if os.path.exists(image_path):
        image_data = open(image_path, "rb").read()
        d3_file.tag.images.set(3, image_data, "image/jpeg", u"Album Cover")
        print("Image for album found")
    else:
        print("No image for album found")

    d3_file.tag.save()

maps = os.listdir("maps")

artists = []
titles = []
links = []
albums = []
tracks = []
paths = []

# Create images folder
if not os.path.exists("images"):
    os.makedirs("images")

for map in maps:
    with open(f"maps/{map}", "r") as f:
        content = f.readlines()

    i = 0

    # If line has no alphabet characters,
    # remove it from the list
    while True:
        if not content[i].upper().isupper():
            del content[i]

        i += 1

        if i >= len(content):
            break

    del content[1] # Second line is just sheet 
                   # headings; not required
                    

    # Remove all newline characters
    for i in range(len(content)):
        content[i] = content[i].replace("\n", "")
        
    artist = content[0].split("	")[1]

    # Create image sub-folders
    image_path = f"images/{artist}"
    if not os.path.exists(image_path):
        os.makedirs(image_path)
    
    i = 1

    # Extract information from map and
    # add it to corrosponding lists
    while i < len(content):
        title, link, album, track, path = content[i].split("	")

        if album == "":
            album = title

        titles.append(title)
        links.append(link)
        albums.append(album.replace(" - Album", ""))
        tracks.append(track)
        paths.append(path)

        artists.append(artist)

        i += 1

download_count = 0

# Check how many files don't exist
for path in paths:
    if not os.path.exists(f"{path}.mp3"):
        download_count += 1

song_count = len(titles)

print(f"Number of Artists: {len(maps)}")
print(f"Number of songs to download {download_count}/{song_count}")

proceed = str(input("Proceed? (y/n): ")).lower()

if proceed != "y":
    exit()

# If no songs exist, default
# to no replace
if download_count == song_count:
    replace = "n"
    replace_metadata = "n"
else:
    replace = str(input("Replace existing files? (y/n): ")).lower()

    if replace != "y":
        replace_metadata = str(input("Replace metadata? (y/n): ")).lower()


if replace != "y":
    for i in range(len(paths)):

        if os.path.exists(path=f"{paths[i]}.mp3"):
            links[i] = ""


print("\n--- POWERED BY YT-DLP AND EYED3 ---")

for i in range(song_count):
    print(f"\nFile {i+1}/{song_count}, {titles[i]}:")
    can_download = True
    can_metadata = True

    if not "http" in links[i]:
        can_download = False

        if replace_metadata != "y":
            can_metadata = False
    
    if can_download:
        download_from_youtube(path=paths[i], link=links[i])

    if can_metadata:
        add_metadata(path=paths[i], 
                    title=titles[i],
                    artist=artists[i],
                    album=albums[i],
                    track=tracks[i])
        
    if not can_download and not can_metadata:
        print("Passing...")