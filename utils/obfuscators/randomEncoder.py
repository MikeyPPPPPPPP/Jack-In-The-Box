import base64
import random
import sys

class encoderGenrator:
    def __init__(self, text):
        self.text = text
        self.code = {}
        self.alpha = {'\t': '0', '\n': '1', ' ': '2', '!': '3', '@': '4', '~': '5', '`': '6', '#': '7', '$': '8', '%': '9', '^': '10', '&': '11', '*': '12', '(': '13', ')': '14', '_': '15', '=': '16', '-': '17', '+': '18', '{': '24', '}': '23', '|': '21', '\\': '22', '[': '25', ']': '26', ':': '27', ';': '28', '"': '29', "'": '30', ',': '31', '.': '32', '/': '33', '?': '34', '>': '35', '<': '36', '0': '37', '1': '38', '2': '39', '3': '40', '4': '41', '5': '42', '6': '43', '7': '44', '8': '45', '9': '46', 'a': '47', 'b': '48', 'c': '49', 'd': '50', 'e': '51', 'f': '52', 'g': '53', 'h': '54', 'i': '55', 'j': '56', 'k': '57', 'l': '58', 'm': '59', 'n': '60', 'o': '61', 'p': '62', 'q': '63', 'u': '68', 'r': '65', 's': '66', 't': '67', 'v': '69', 'w': '70', 'x': '71', 'y': '72', 'z': '73', 'A': '74', 'B': '75', 'C': '76', 'D': '77', 'E': '78', 'F': '79', 'G': '80', 'H': '81', 'I': '82', 'J': '83', 'K': '84', 'L': '85', 'M': '86', 'N': '87', 'O': '88', 'P': '89', 'Q': '90', 'U': '95', 'R': '92', 'S': '93', 'T': '94', 'V': '96', 'W': '97', 'X': '98', 'Y': '99', 'Z': '100'}
        self.genrateKeys()
        self.encodeedText = (base64.b64encode(''.join([self.code[x] for x in self.text]).encode('ascii'))).decode('ascii')

    def swap(self, inlist, a, b):
        inlist[a], inlist[b] = inlist[b], inlist[a]
        return inlist

    def genrateKeys(self):
        self.temp = [x for x in self.alpha]
        self.counter = len(self.alpha)

        for char in self.alpha:
            self.randomNumber = random.randint(0,self.counter-1)
            self.code[char] = self.temp[self.randomNumber]
            self.temp = self.swap(self.temp, self.randomNumber, self.counter - 1)
            self.counter -= 1


    def codeGenrator(self):
        return 'import base64;exec(\'\'.join([y[0] for x in [x for x in base64.b64decode( (\''+self.encodeedText+'\').encode(\'ascii\') ).decode(\'ascii\')] for y in [[x[0], x[1]] for x in '+str(self.code)+'.items()] if x == y[1]]))'

