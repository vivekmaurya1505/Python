import random
s = """qqwertyuiop[[[]\a"'sdfghjkl;'zxcv
        bnm,../(){}_+|?><:*&^%$@!~QWERTYUIOPASDFGHJKLZXCVBNM"""

passwordlen = 16
password = "".join(random.sample(s,passwordlen))
print(password)
