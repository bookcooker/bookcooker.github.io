def iszhcn(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


if __name__ == '__main__':
    root = './temp/'
    filename = '1.md'
    des = root + filename
    ff = open(des, 'r')
    md = ff.read()
    print(iszhcn(md))
    l = len(md)
    for i in range(l):
        if iszhcn(i):
            