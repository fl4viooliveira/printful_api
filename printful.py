import json
from typing import ItemsView
import requests
import base64

s_key = 'xk7ov0my-t9vm-70z6:y491-2uyygexkkq6r' # this is a secret key of the test store on Printful
key = base64.b64encode(bytes(s_key, 'utf-8'))
keyDecoded = key.decode('ascii')
header = {'Authorization': 'Basic ' + keyDecoded}

r = requests.get('https://api.printful.com/sync/products', headers=header)

test = r.json()

print(json.dumps(test, indent=4))
#print(test)


id = [n for i in test["result"] for k, n in i.items() if k == "id"]

product_1 = id[0]
url_product1 = f'https://api.printful.com/store/products/{product_1}'

r = requests.get(url_product1, headers=header)
product_1_details = r.json()


#variant_name = product_1_details['result']['sync_variants']

variant_name = [n for i in product_1_details['result']['sync_variants'] for k, n in i.items() if k == "product"]

print(json.dumps(variant_name, indent=2))

# y = json.loads(variant_name)
# print(y["name"])
# url_sing_var = f' https://api.printful.com/store/variants/{product_1}'

# r = requests.get(url_sing_var, headers=header)
# product_1_var = r.json()


# print(json.dumps(product_1_var, indent=2))


# print(product_1, variant_name)

# print(json.dumps(variant_name, indent=2))

# f = open('data.test',)

# data = test.load(f)

# for i in test['result']:
    # print(i)


# name_list = [n for i in test["result"] for k, n in i.items() if k == "name"]
# print(test)

# print(json.dumps(test, indent=4))


# print([n for i in test["result"] for k, n in i.items() if k == "name"])


# print(type(test)) # dict

# print(print(test.keys())) # dict_keys(['code', 'result', 'extra', 'paging'])

# print(type(test["result"])) # <class 'list'>

# print(len(test["result"])) # 3

# print(type(test["result"][0])) # <class 'dict'>