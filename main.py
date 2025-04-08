import os
import eyed3

from map import return_artists

# yt dlp setup
def download_from_youtube(title, link):
    cmd = f"yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format mp3 \"{link}\" -o \"{title}\""
    os.system(cmd)

def add_metadata(path, title, artist, album, track=1):
    d3_file = eyed3.load(path)

    d3_file.tag.title = title
    d3_file.tag.artist = artist
    d3_file.tag.album = album
    d3_file.tag.track_num = track

    d3_file.tag.save()


# Main loop
artists = return_artists()

artist_count = len(artists)

if input("Replace mode? (y/n): ").lower() == "y":
    replace_mode = True
else:
    replace_mode = False

# Main loop
for i in range(artist_count):

    artist = artists[i]

    print(f"\n\nDownloading {artist.title}, artist {i+1} of {artist_count}")
    print("-"*5)

    # Create folder for artist
    if not os.path.exists(artist.title):
        os.makedirs(artist.title)

    # Download all single files
    for file in artist.music_files:
        file_title = f"{artist.title}/{file.title}"

        # Skip download if not in replace 
        # mode and file already exists
        if not replace_mode:
            if os.path.isfile(f"{file_title}.mp3"):
                print("File already exists, skipping.")
                continue

        download_from_youtube(title=file_title, link=file.link)

        add_metadata(path=f"{file_title}.mp3", 
                        title=file.title,
                        artist=artist.title,
                        album=file.title.replace(" - Album", ""))




    # Download all multi albums
    for multi_album in artist.multi_albums:
        if not os.path.exists(f"{artist.title}/{multi_album.title}"):
            os.makedirs(f"{artist.title}/{multi_album.title}")

        track = 1

        for file in multi_album.music_files:
            file_title = f"{artist.title}/{multi_album.title}/{track} - {file.title}"

            if not replace_mode:
                if os.path.isfile(f"{file_title}.mp3"):
                    print("File already exists, skipping.")
                    continue

            download_from_youtube(title=file_title, link=file.link)

            add_metadata(path=f"{file_title}.mp3",
                            title=file.title,
                            artist=artist.title,
                            album=multi_album.title.replace(" - Album", ""))
            
            track += 1