import argparse

class age:
    def get_args(self):
        a = argparse.ArgumentParser()
        a.add_argument('-i', '--infile', help="this is the PYTHON file to be obfuscated")
        a.add_argument('-e', '--encoder', help="type --encoders for list on encoders")
        a.add_argument('--encoders', action='store_true')

        a.add_argument('-o', '--obfu', help="type --obfus for list on encoders")
        a.add_argument('--obfus', action='store_true')

        a.add_argument('-p', '--packer', action='store_true', help="this will pack the code with gzip compression")
        a.add_argument('-E', '--encryption', action='store_true', help="this is a polymorphic encryptor")
        a.add_argument('-r', '--random', action='store_true', help="this will randomly obfuscate the file with all the options")
        a.add_argument('-f', '--outfile', help="this will be the out file name")

        return a.parse_args()

    def enco(self):
        print("""
        Encoders
        --------
        base64  : this will encode with base64
        hex     : this will encode with hex
        """)

    def obfuscators(self):
        print("""
        Obfuscators
        -----------
        ranenc :this is a polymorphic ceaser cicher
        strcla :this is a polymorphic string builder 
        """)