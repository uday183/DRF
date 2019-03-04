class PlayAdopter:
    def __init__(self):
        self.mp3 = "MP3()"
        self.doc = "DOC()"



class MP3(PlayAdopter):
    def play(self):
        print ("audio is playing now...")
        return self.__class__()


class DOC(PlayAdopter):
    def play(self):
        print ("opening doc files...")
        return self.__class__()

