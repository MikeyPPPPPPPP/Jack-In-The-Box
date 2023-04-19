#!/usr/bin/env python3
import random


import utils

def boxEmUp(args):
    filedata = ""
    if args.infile:
        fileopen = open(args.infile, 'r')
        filedata = fileopen.read()
        fileopen.close()
    

    if args.encoder == "base64":
        s = utils.standardEncoding(filedata)
        filedata = s.baseE64()
    if args.encoder == "hex":
        s = utils.standardEncoding(filedata)
        filedata = s.hexE()

    if args.obfu == "ranenc":
        re = utils.encoderGenrator(filedata)
        filedata = re.codeGenrator()
    if args.obfu == "strcla":
        sc = utils.stringObjuscator(filedata)
        filedata = sc.obfuscat()

    if args.packer:
        t = utils.packer(filedata)
        filedata = t.returnString()

    if args.encryption:
        ec = utils.basicEncryption(filedata)
        filedata = ec.encrypt()

    if args.random:
        a = [1,2,3,4,5,6]
        random.shuffle(a)

        for x in a:
            if x == 1:
                s = utils.standardEncoding(filedata)
                filedata = s.baseE64()
            elif x == 2:
                s = utils.standardEncoding(filedata)
                filedata = s.hexE()
            elif x == 3:
                re = utils.encoderGenrator(filedata)
                filedata = re.codeGenrator()
            elif x == 4:
                sc = utils.stringObjuscator(filedata)
                filedata = sc.obfuscat()
            elif x == 5:
                t = utils.packer(filedata)
                filedata = t.returnString()
            elif x == 6:
                ec = utils.basicEncryption(filedata)
                filedata = ec.encrypt()
    if args.outfile:
        with open(args.outfile, 'w') as file:
            file.write(filedata)
    else:
        print(filedata)




def main():
    print("\n\tJack In The Box\nby Michael Provenzano")
    print("        \n\n\n                 What is anti-malware.\n\n\n !!! PYTHON file ONLY !!!")
    arg = utils.age()
    args = arg.get_args()

    if args.encoders:
        arg.enco()
        exit()

    if args.obfus:
        arg.obfuscators()
        exit()

    if args.infile:
        boxEmUp(args)


if __name__ == "__main__":
    main()
