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
            string += "Title: {}\n".format(file.title)
            string += "Album: {}\n".format(file.album)
            string += "Link: {}\n".format(file.link)

        return string

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

for artist in artists:
    print(artist)