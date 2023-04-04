import os
import re


def writeDown(des, res):
    ff = open(des, 'w')
    ff.write(res)

def genTexCallPdfLatex(gets):
    root = 'temp'
    if root not in os.listdir('./'):
        root = './temp/'
        os.makedirs(root)
    for i in len(gets):
        genFile = str(i) + '.tex'
        des = root + genFile
        writeDown(des, gets[i])
        os.system("pdflatex.exe -synctex=1 -interaction=nonstopmode " + des)


def test():
    ll = os.listdir('./md/')
    print(ll)
    ff = open('./md/' + ll[2], 'r')
    md = ff.read()
    ff.close()
    print(md)
    def test():
        slice = md.split("$$")
        l = len(slice)
        selected = []
        for i in range(l):
            if i % 2 == 1:
                selected.append(slice[i])
        return selected

    gets = test()
    print(gets)

def iszhcn(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

if __name__ == '__main__':
    ll = os.listdir('./md/')
    ff = open('./md/' + ll[2], 'r')
    md = ff.read()
    ff.close()
    slice = md.split("$$")
    l = len(slice)
    selected = []
    for i in range(l):
        if i % 2 == 1:
            selected.append(slice[i])
