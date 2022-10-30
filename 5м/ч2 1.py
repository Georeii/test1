import json


class Model():

    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        with open('save_Model.json', "r") as file:
            file_model = json.load(file)
            file_model.append(self.title)
            file_model.append(self.text)
            file_model.append(self.author)
            with open('save_Model.json', "w") as file:
                json.dump(file_model, file)


s = Model("Ты и я (Александру I)", "Ты богат, я очень беден;", "Александр Пушкин")

s.save()
