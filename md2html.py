import markdown
import os
import sys
from treeGen import *
from time import sleep
exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
html = """
<!DOCTYPE html>
<html lang="en-US">

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../css/style.css">
    <!-- start custom head snippets, customize with your own _includes/head-custom.html file -->

    <!-- Setup theme-color -->
    <!-- start theme color meta headers -->
    <meta name="theme-color" content="#151515">
    <meta name="msapplication-navbutton-color" content="#151515">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <!-- end theme color meta headers -->


    <!-- Setup Google Analytics -->



    <!-- You can set your favicon here -->
    <!-- link rel="shortcut icon" type="image/x-icon" href="/hacker/favicon.ico" -->

    <!-- end custom head snippets -->


    <!-- Begin Jekyll SEO tag v2.7.1 -->
    <title>bookcooker | Welcome to bookcooker.</title>
    <meta name="generator" content="Jekyll v3.9.0">
    <meta property="og:title" content="bookcooker">
    <meta property="og:locale" content="en_US">
    <meta name="description" content="a new series about blog.">
    <meta property="og:description" content="a new series about blog.">
    <link rel="canonical" href="https://github.com/bookcooker/">
    <meta property="og:url" content="https://bookcooker.github.io/">
    <meta property="og:site_name" content="bookcooker">
    <meta name="twitter:card" content="summary">
    <meta property="twitter:title" content="bookcooker">
    <script type="application/ld+json">
{"description":"a new series about blog.","url":"https://github.com/bookcooker/","@type":"WebSite","headline":"bookcooker","name":"bookcooker","@context":"https://schema.org"}</script>
</head>

<header>
    <div class="container">
        <a id="a-title" href="https://bookcooker.github.io/">
            <h1>bookcooker;</h1>
        </a>
        <h2>a new series about blog;</h2>

        <section id="downloads">

            <a href="about.html" class="btn">About;</a>
            <a href="tree.html" class="btn">Tree;</a>

            <a href="https://github.com/bookcooker" class="btn btn-github"><span class="icon"></span>Goto
                GitHub;</a>
        </section>
    </div>
</header>
<body>
%s    
</body>

</html>
"""

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
