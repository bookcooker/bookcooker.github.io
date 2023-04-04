treeHtml = ""

link = """
<li><a href="%s" title="%s">%s</a>
</li>
"""

h5 = open('./css/h5_tree', 'r')
treeHtml = h5.read()
h5.close

def getHtmlist(ll):
    links = ""
    des = "./html/"
    for i in ll:
        links = links + link % (des + i, i.split(".")[0], i.split(".")[0])
    return treeHtml % links

def treeGen(hdir):
    tree = getHtmlist(hdir)
    filename = './tree.html'
    treeff = open(filename, 'w')
    treeff.write(tree)
    print(">>>>>gen tree := " +filename)
    treeff.close()