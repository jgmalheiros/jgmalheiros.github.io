#!/bin/python

import os

for path, dirs, files in os.walk("1o Semestre"):
    if ".assets" in path: pass
    with open(path+"/index.md","w") as r:
        for i in sorted(dirs):
            if not ".assets" in i: r.write("[" + i + "](" + i + ")\n\n")
        for i in sorted(files):
            name=i[:-2]+"html"
            if not "index" in name:
                r.write("[" + name[:-5]+ "](" + name + ")\n\n")
