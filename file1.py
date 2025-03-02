import requests

class Aclass():
    def __init__(self):
        self.lst_name1 = []
        self.lst_price1 = []
        self.url = "http://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency_v2.json"
        request = requests.request("GET", self.url)
        result_var = request.json()
        var_interation = result_var["gold"]
        for i in var_interation:
            name = i.get("name")
            self.lst_name1.append(name)

        for j in var_interation:
            price = j.get("price")
            self.lst_price1.append(price)