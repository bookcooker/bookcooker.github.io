ff = open('./src/en2zh/en2zh', 'r')
words = ff.readlines()
en = []
zh = []
for i in words:
    en.append(i.split(":")[0])
    zh.append(i.split("\n")[0].split(":")[1])
for i, j in en, zh:
    print(i + ">>>>>>" + j)

