import json


class Model:
    def __init__(self):
        self.title = "Ты и я (Александру I)"
        self.text = "Ты богат, я очень беден;"
        self.author = "Александр Пушкин"

    def _save(self,):
        with open('save_Model.json', "r") as file:
            file_model = json.load(file)
            file_model = file_model | s.__dict__
            print(file_model,s.__dict__)
            with open('save_Model.json', "w") as file:
                json.dump(file_model, file)

    def _save1(self):
        pass


s = Model()
s._save()