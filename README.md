# Jack In The Box


## A simple obfuscator for python files, this should get pass static analysis.

* Encoders
* Encryptor
* Obfuscators
* Packer
#


Encoders
* Base64
* Hex

Encryptor
* polymorphic encrypter using the cryptography module

Obfuscators
* ranenc:       This is a polymorphic ceaser cicher
* strcla:       This is a polymorphic string builder 

Packer
* Gzip 

#
### Example Usage:

* ./jackInTheBox.py -e base64 -o ranenc -p -i infile.py -f outfile.py
* ./jackInTheBox.py -E -e hex -p -i infile.py -f outfile.py
* ./jackInTheBox.py -o strcla -i infile.py -f outfile.py
* ./jackInTheBox.py -r -i infile.py -f outfile.py

#
### Install and dependencies:
* Python 3.7+
* cryptography
#
### Main contributor:
Michael Provenzano @MikeyPPPPPPPP
#
### Demo https://www.youtube.com/watch?v=GLFhLyJUqRA&ab_channel=MichaelDProvenzano
