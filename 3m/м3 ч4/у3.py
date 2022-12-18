import json

file = "register_file.json"
login = input()
passwd = input()


def login_function(login, passwd, file):
    num = 0
    num1 = 0
    with open(file, "r") as file1:
        f = json.load(file1)
        for i in f:
            if i == login:
                if f[login] == passwd:
                    print("вы вошли в систему")
                    num = 1
                    break
            else:
                num1 = 1
        if num1 != 0 and num != 1:
            print("пароль или логин неверный")


login_function(login, passwd, file)
