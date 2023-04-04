import markdown
import os
import sys
from treeGen import *
from time import sleep

exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
html = ""
h5 = open('./css/h5_post', 'r')
html = h5.read()
h5.close

def md2html(mdstr):
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret

def get_from_argv():
    if len(sys.argv) < 3:
        print('usage: md2html.py [source_filename] [target_file]')
        sys.exit()
    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
    outfile = open(sys.argv[2],'a')
    outfile.write(md2html(md))
    outfile.close()
    print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))

def removeCache(filepath):
    delist = os.listdir(filepath)
    for f in delist:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(">>>>>clean html := " + file_path)

if __name__ == '__main__':

    root = './md/'
    des = './html/'
    removeCache(des)
    sleep(2)
    mdir = os.listdir(path = root)
    ll = []
    for i in mdir:
        if i.split(sep = '.')[1] == 'md':
            ll.append(i)
    for i in ll:
        oldfile = root + i
        newfile = des + i.split('.')[0] + '.html'
        print(">>>>>gen md2html := " + newfile)
        infile = open(oldfile, 'r')
        md = infile.read()
        infile.close()
        outfile = open(newfile ,'w')
        outfile.write(md2html(md))
        outfile.close()
    hdir = os.listdir(path = des)
    hdir.reverse()
    treeGen(hdir)
