import os
from movefile import *
from getImages import *
from movefile import *

def moveImages(md = 'md'):
        fileslist = getFilelist(os.path.abspath(os.path.join('.', md)))
        img = []
        for file in fileslist:
            print(f'>>>>>>load: {file}')
            with open(file, encoding='utf-8') as f:
                mdContent = f.read()

            picslist = getPicslist(mdContent)
            img.append(picslist)
            print(f'>>>>>>find pic: {len(picslist)}')
            
            pics =[]
            for i in picslist:
                 if "../images" in i:
                    pics.append(i)

            for pic in pics:
                src = '.' + pic.split("..")[1]
                print(f'>>>>>> src: {src}')
                desfile = file.split("/md/")[1].split(".md")[0]
                des = "./images/" + desfile + src.split("/images")[1]
                print(f">>>>>>des: {des}")
                shutil.copy(src, des)
            print(f'>>>>>>finish.')

if __name__ == "__main__":
    moveImages()