# -*- coding: utf-8 -*-

import sys
import shutil

def main():

    args = sys.argv
    argc = len(args)

    if argc != 2:
        print("need 1 argument.")
        return

    for n in range(int(args[1]) - 1 ):
        shutil.copyfile("./1.txt" , "./" + str(n+2) + ".txt")

    return


if __name__ == '__main__':
    main()
