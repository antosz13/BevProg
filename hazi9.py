#!/usr/bin/env python
# -*- coding: utf-8 -*-
def main():
#?pi vers?    
    with open("pivers.txt", "r") as f, open("masikfajl.txt", "w") as f2:
        text = f.read()
        print(text, "3", file=f2)

#aratofeladat
    with open("string1.py", "r") as g, open("string1_clean", "w") as g2:
        li = g.readlines()
        for i in li:
            if i[0] != "#":
                print(i, file=g2)
            else:
                continue
        

if __name__ == "__main__":
    main()