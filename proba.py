import json
import urllib.request
import collections
import os
import re
import matplotlib.pyplot as plt
req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=178384865&offset=0&count=20&v=5.92&access_token=8423c2448423c2448423c244d08441f2a1884238423c244dee1644d9e90529494134bf8') 
with urllib.request.urlopen(req) as response: 
    result = response.read().decode('utf-8')
data = json.loads(result)

i = 0
stroka = ""
while i < 20:
    stroka = stroka + "\n" + data['response']['items'][i]['text']
    i = i + 1

massiv1 = stroka.split()
chast1 = collections.Counter(massiv1)

with open("C:\\Users\\student\\Desktop\\input.txt", "w", encoding="utf-8") as f:
    f.write(stroka)


os.system("C:\\Users\\student\\Desktop\\mystem.exe -lndc C:\\Users\\student\\Desktop\\input.txt C:\\Users\\student\\Desktop\\output.txt")


with open("C:\\Users\\student\\Desktop\\output.txt", "r", encoding="utf-8") as f:
    text = f.read()
    text2 = re.sub("\n", "", text)
    text3 = re.sub("\r", "", text2)
    text4 = text3.split("_")
chast2 = collections.Counter(text4)


slovarsmall1 = collections.Counter(massiv1).most_common(10)
slovarsmall2 = collections.Counter(text4).most_common(10)

keys1 = []
keys2 = []
values1 = []
values2 = []


while i < 10:
    for keys 
        keys1.append(key1)
    values1.append(slovarsmall1[key1])

for key2 in slovarsmall2:
    keys2.append(key2)
    values2.append(slovarsmall2[key2])

x1 = [i for i in range(1, 10, 1)]
x2 = x1

for x11, y11, d in zip(x1, values1, keys1):
    plt.scatter(x11, y11,)
    plt.text(x11+0.1, y11+0.1, d) 
plt.show()
    



