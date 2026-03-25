import json
from Cryptodome.Util.number import long_to_bytes

with open("output.txt", "r") as f:
    data = f.read()
    data = json.loads(data)

    n = data["n"]
    c = data["c"]

    e = 2 ** 16 + 1

    flag = long_to_bytes(pow(c, e, n))
    print(flag.decode())