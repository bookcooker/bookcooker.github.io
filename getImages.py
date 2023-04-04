import misaka
import os
import requests
import uuid
from bs4 import BeautifulSoup


def getFilelist(dir):
    filelist = []
    for root, dirs, files in os.walk(dir, topdown=False):
        for file in files:
            filelist.append(os.path.join(root, file))

    return filelist


def getPicslist(md_content):
    mdRender = misaka.Markdown(misaka.HtmlRenderer())
    html = mdRender(md_content)
    soup = BeautifulSoup(html, features='html.parser')
    picslist = []
    for img in soup.find_all('img'):
        picslist.append(img.get('src'))

    return picslist


def downloadPics(url, file):
    data = requests.get(url).content
    filename = os.path.basename(file)
    dirname = os.path.dirname(file)
    des = os.path.join(dirname, f'{filename}.assets')
    if not os.path.exists(des):
        os.mkdir(des)

    with open(os.path.join(des, f'{uuid.uuid4().hex}.jpg'), 'w+') as f:
        f.buffer.write(data)


def macthCountImages(des, img = './images/'):
    images = os.listdir(img)
    print(len(images))
    acc = 0
    for i in des:
        for j in i:
            if str(j).rfind('/images/') != -1:
                if j.split('/images/')[1] in images:
                    acc = acc + 1
                    print(">>>>>>match: " + j)
            else:
                print(">>>>>>n-match: " + j)
    return acc

def getImages(md = 'md'):
        fileslist = getFilelist(os.path.abspath(os.path.join('.', md)))
        img = []
        for file in fileslist:
            print(f'>>>>>>load: {file}')
            with open(file, encoding='utf-8') as f:
                mdContent = f.read()

            picslist = getPicslist(mdContent)
            img.append(picslist)
            print(f'>>>>>>find pic: {len(picslist)}')

            for index, pic in enumerate(picslist):
                print(f'>>>>>>id: {index + 1} ... {pic}')
                
            print(f'>>>>>>finish.')
        print(macthCountImages(img))
if __name__ == '__main__':
    getImages()
    
