import requests

class Bclass():
    def __init__(self):
        self.lst_name2 = []
        self.lst_price2 = []
        self.url = "http://brsapi.ir/FreeTsetmcBourseApi/Api_Free_Gold_Currency.json"
        request = requests.request("GET", self.url)
        result_var = request.json()
        var_interation = result_var["currency"]
        for i in var_interation:
            name = i.get("name")
            self.lst_name2.append(name)

        for j in var_interation:
            price = j.get("price")
            self.lst_price2.append(price)