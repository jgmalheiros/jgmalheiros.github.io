#!/bin/python

import os

def indexer():
    for path, dirs, files in os.walk("."):
        if path == ".": continue
        if ".assets" in path: continue
        with open(path+"/index.md","w") as r:
            for i in sorted(dirs):
                if not ".assets" in i: r.write("[" + i + "](" + i + ")\n\n")
            for i in sorted(files):
                name=i[:-2]+"html"
                if not "index" in name:
                    r.write("[" + name[:-5]+ "](" + name + ")\n\n")

def appender(texto):
    for path, dirs, files in os.walk("."):
        for arq in files:
            if (".md" in arq) and (arq != "index.md"):
                with open(path+"/"+arq, "a") as w:
                    w.write(texto)

indexer()
appender("\n\n{% include mathjax.html %}")
