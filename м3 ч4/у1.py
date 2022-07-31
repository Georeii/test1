import json

Login = input()
password = input()


def register(Login, password):
    with open('register_file.json', "r") as file:
        f = json.load(file)
        f[Login] = password
        with open('register_file.json', "w") as file:
            json.dump(f, file)
    print("вы зарегистрированы")


register(Login, password)
