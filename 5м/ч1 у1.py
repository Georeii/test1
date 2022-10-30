
class StrngVar():
    stra = ""

    def __init__(self, name):
        self.name = name

    def set(self,str_vod):
        self.stra += " " + str_vod
    def get(self):
        print(self.stra)

djg = StrngVar("сторока")

djg.set("ваня")

djg.set("ваня и маша")

djg.get()