import os
import yt_dlp

# Class Setup
class MusicFile():
    def __init__(self, title, link, album=""):
        self.title = title
        self.album = album
        self.link = link

        if self.album == "":
            self.album = self.title

class MultiAlbum():
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs

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
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{title}.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])



artists = []

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

artist_count = len(artists)

for i in range(artist_count):

    artist = artists[i]

    print(f"\n\nDownloading {artist.title}, artist {i+1} of {artist_count}")
    print("-"*5)

    if not os.path.exists(artist.title):
        os.makedirs(artist.title)

    for file in artist.music_files:
        download_from_youtube(title=f"{artist.title}/{file.title}", link=file.link)