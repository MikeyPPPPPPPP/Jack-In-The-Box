#!/usr/bin/env python3
import random


from utils.getArgs.gArgs import age
from utils.packers import gzipPacker
from utils.encoders import standard
from utils.obfuscators import randomEncoder, stringClass
from utils.encrypters import basicEncrypter



def boxEmUp(args):
    filedata = ""
    if args.infile:
        fileopen = open(args.infile, 'r')
        filedata = fileopen.read()
        fileopen.close()
    

    if args.encoder == "base64":
        s = standard.standardEncoding(filedata)
        filedata = s.baseE64()
    if args.encoder == "hex":
        s = standard.standardEncoding(filedata)
        filedata = s.hexE()

    if args.obfu == "ranenc":
        re = randomEncoder.encoderGenrator(filedata)
        filedata = re.codeGenrator()
    if args.obfu == "strcla":
        sc = stringClass.stringObjuscator(filedata)
        filedata = sc.obfuscat()

    if args.packer:
        t = gzipPacker.packer(filedata)
        filedata = t.returnString()

    if args.encryption:
        ec = basicEncrypter.basicEncryption(filedata)
        filedata = ec.encrypt()

    if args.random:
        a = [1,2,3,4,5,6]
        random.shuffle(a)

        for x in a:
            if x == 1:
                s = standard.standardEncoding(filedata)
                filedata = s.baseE64()
            elif x == 2:
                s = standard.standardEncoding(filedata)
                filedata = s.hexE()
            elif x == 3:
                re = randomEncoder.encoderGenrator(filedata)
                filedata = re.codeGenrator()
            elif x == 4:
                sc = stringClass.stringObjuscator(filedata)
                filedata = sc.obfuscat()
            elif x == 5:
                t = gzipPacker.packer(filedata)
                filedata = t.returnString()
            elif x == 6:
                ec = basicEncrypter.basicEncryption(filedata)
                filedata = ec.encrypt()
    if args.outfile:
        with open(args.outfile, 'w') as file:
            file.write(filedata)
    else:
        print(filedata)




def main():
    print("\n\tJack In The Box\nby Michael Provenzano")
    print("        \n\n\n                 What is anti-malware.\n\n\n !!! PYTHON file ONLY !!!")
    arg = age()
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