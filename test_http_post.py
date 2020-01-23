import requests
url = 'http://localhost:4022'

msg = """
test success!

can post second line and empty lines


<font color="blue">support</font> <font color="green">html</font> <font color="red">syntax</font>

"""
resp = requests.post(url,json={'log':msg})
