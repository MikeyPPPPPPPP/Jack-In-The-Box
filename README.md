# Jack In The Box


## A simple obfuscator for python files, this should get pass static analysis.

* Encoders
* Encryptor
* Obfuscators
* Packer
#


**Encoders**
1. Base64
2. Hex

**Encryptor**
1. polymorphic encrypter using the cryptography module

**Obfuscators**
1. ranenc:       This is a polymorphic ceaser cicher
2. strcla:       This is a polymorphic string builder 

**Packer**
1. Gzip 

#
### Example Usage:
```
./jackInTheBox.py -e base64 -o ranenc -p -i infile.py -f outfile.py
./jackInTheBox.py -E -e hex -p -i infile.py -f outfile.py
./jackInTheBox.py -o strcla -i infile.py -f outfile.py
./jackInTheBox.py -r -i infile.py -f outfile.py
```
More examples [here](https://www.youtube.com/watch?v=GLFhLyJUqRA&ab_channel=MichaelDProvenzano).
#
### Install and dependencies:
* Python 3.7+
* cryptography
#
### Main contributor:
Michael Provenzano @MikeyPPPPPPPP

