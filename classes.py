# class.py
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