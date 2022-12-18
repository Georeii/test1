import json

Login = input()
password = input()


def register(Login, password):
    num = 0
    with open('register_file.json', "r") as file:
        f = json.load(file)
        for i in f:
            if Login == i:
                num = 1
        if num == 0:
            f[Login] = password
            with open('register_file.json', "w") as file:
                json.dump(f, file)
                print("Вы зарегистревивались")
        else:
            print("такой email есть в системе")


register(Login, password)
