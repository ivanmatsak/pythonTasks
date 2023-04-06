import requests
import json
import datetime

class Tasks:
    def task1(self):
        num = int(input("Введите 2-х байтное число: "))
        byte1 = num & 0xff
        byte2 = (num >> 8) & 0xff
        new_num = (byte1 << 8) | byte2
        print("Новое значение:", new_num)
    def task2(self):
        n = int(input("Введите количество корзин: "))
        w = int(input("Введите вес настоящих монет: "))
        d = int(input("Введите разницу в весе фальшивых монет: "))
        p = int(input("Введите суммарный вес отобранных монет: "))

        k = w * n * (n - 1) / 2 - p
        if (k > 0):
            print(int(k / d))
        else:
            print(int(n))

    def task3(self):
        response = requests.get("https://www.python.org/")
        html = response.text
        char_count = {}

        for char in html:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        with open("readme.md", "w") as file:
            for char, count in char_count.items():
                file.write(f"{char}: {count}\n")
    def task4(self):
        with open("file.json", "r") as file:
            data = json.load(file)

        data1 = data

        def get_keys(data1):
            for k, v in data1.items():
                if (isinstance(v, list)):
                    dict1 = v[0]
                    get_keys(dict1)
                elif (isinstance(v, dict)):
                    dict2 = v
                    get_keys(dict2)
                    data1["updated"]=datetime.datetime.now().isoformat();
                else:
                    if k=="updated":
                        data1[k] = datetime.datetime.now().isoformat()

        get_keys(data1)
        o_file = open("result.json", "w")
        json.dump(data1, o_file)