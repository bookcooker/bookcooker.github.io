treeHtml = """
<HTML lang="zh-cn">
<HEAD>
<TITLE>ebxeax</TITLE>
<LINK REL="stylesheet" TYPE="text/css" HREF="./css/lua.css">
<link rel="Shortcut Icon" href="./images/favicon.ico" type="image/x-icon" />
<META HTTP-EQUIV="content-type" CONTENT="text/html; charset=utf-8">
<STYLE TYPE="text/css">
blockquote, .display {
	border: solid #a0a0a0 2px ;
	border-radius: 8px ;
	padding: 1em ;
	margin: 0px ;
}

.display {
	word-spacing: 0.25em ;
}

dl.display dd {
	padding-bottom: 0.2em ;
}

tt, kbd, code {
	font-size: 12pt ;
}
</STYLE>
</HEAD>

<BODY>

<H1>
<A HREF="http://www.github.com/ebxeax"><IMG SRC="./images/favicon.ico" width="100" height="100" ALT="ebxeax"></A>
Homepage
</H1>


<DIV CLASS="menubar">
	<A HREF="#about">about</A>
	&middot;
	<A HREF="#tutorial">tutorial</A>
	&middot;
	<A HREF="#test">test</A>
	&middot;
	<A HREF="tree.html">tree</A>
</DIV>
%s
</BODY>
</HTML>    
"""

link = """
<li><a href="%s" title="%s">%s</a>
</li>
"""

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