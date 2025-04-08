import os

# Class Setup
class MusicFile():
    def __init__(self, title, link, album=""):
        self.title = title
        self.album = album
        self.link = link

        if self.album == "":
            self.album = self.title

class MultiAlbum():
    def __init__(self, title, music_files):
        self.title = title
        self.music_files = music_files

class Artist():
    def __init__(self, title, music_files=[], multi_albums=[]):
        self.title = title
        self.music_files = music_files
        self.multi_albums = multi_albums

    def __str__(self):
        string = ""
        for file in self.music_files:
            string += f"Title: {file.title}\n"
            string += f"Album: {file.album}\n"
            string += f"Link: {file.link}\n"
        return string



# yt dlp setup
def download_from_youtube(title, link):
    cmd = f"yt-dlp --cookies-from-browser firefox -x --audio-quality 0 --audio-format mp3 \"{link}\" -o \"{title}\""
    os.system(cmd)


# Main loop
def main():
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

            


        # Download all multi albums
        for multi_album in artist.multi_albums:
            if not os.path.exists(f"{artist.title}/{multi_album.title}"):
                os.makedirs(f"{artist.title}/{multi_album.title}")

            for file in multi_album.music_files:
                file_title = f"{artist.title}/{multi_album.title}/{file.title}"

                if not replace_mode:
                    if os.path.isfile(f"{file_title}.mp3"):
                        print("File already exists, skipping.")
                        continue

                download_from_youtube(title=file_title, link=file.link)



# Music list
def return_artists():
    artists = []

    artists.append(
        Artist(title="Butcher M.D.",
            music_files=[
                MusicFile(title="Traces of Gore - Album", link="https://www.youtube.com/watch?v=fSCv6MswW8E")
            ])
    )

    artists.append(
        Artist(title="Esophagus",
            music_files=[
                MusicFile(title="Killing for Sport - EP", link="https://www.youtube.com/watch?v=X_U4WZ-9hf0"),
                MusicFile(title="Steamrollin'", link="https://www.youtube.com/watch?v=-zZUh-Pcs-E")
            ])
    )

    artists.append(
        Artist(title="Gore Instinct",
            music_files=[
                MusicFile(title="Invasion Of The Body Slammer - Album", link="https://www.youtube.com/watch?v=8EUgH9y_D0I")
            ])
    )

    artists.append(
        Artist(title="The Dark Prison Massacre",
            multi_albums=[
                MultiAlbum(title="Deformity of Human Consciousness - Album",
                        music_files=[
                            MusicFile(title="1 - Silence of Decay", link="https://www.youtube.com/watch?v=bsBJwnXMRRI"),
                            MusicFile(title="2 - Illusion of Withering", link="https://www.youtube.com/watch?v=ad0U37c4GJw"), 
                            MusicFile(title="3 - Hate Purgatory", link="https://www.youtube.com/watch?v=FPZSv8__mjw"),
                            MusicFile(title="4 - Despite of Desolation", link="https://www.youtube.com/watch?v=VqY1u5_hIjk"),
                            MusicFile(title="5 - Mortal Awareness", link="https://www.youtube.com/watch?v=ztU6fc8cbTo"),
                            MusicFile(title="6 - Narcotic Induced Hypo-Thermia", link="https://www.youtube.com/watch?v=B1fgKd8lUwQ"),
                            MusicFile(title="7 - Faget (Korn Cover)", link="https://www.youtube.com/watch?v=gQfs1jRbzjs"),
                            MusicFile(title="8 - Crematory", link="https://www.youtube.com/watch?v=WOxzVUXlY4M"),
                            MusicFile(title="9 - Electric Shock", link="https://www.youtube.com/watch?v=7aCHhbGMLp8"),
                        ]
                    )
            ])
    )

    artists.append(
        Artist(title="Visceral Disgorge",
               music_files=[
                   MusicFile(title="Ingesting Putridity - Album", link="https://www.youtube.com/watch?v=Qqa0v79VutY")
               ])
    )

    return artists

main()