import random
import string

class stringObjuscator:
    def __init__(self, inString, number=1):
        self.inString = inString
        self.number = number
        self.combinedVar = ''.join([random.choice(string.ascii_lowercase) for x in range(random.randint(5,10))])

    
    def obfuscat(self):
        self.allText = ""

        cD = self.stringify()
        BB = self.builder(cD)
        self.allText += str(BB[0])+'\n'

        ff = self.final(BB[1])
        self.allText += str(ff)
        self.allText += str('exec('+self.combinedVar+')')
        return self.allText


    #this will segment the string into a  list
    def stringify(self):
        splitLenght = random.randint(5,10)
        lenString = len(self.inString)
        odd = False
        if lenString % 2:
            odd = True
        
        segments = []

        counter = 0
        for x in range(1,lenString, splitLenght):
            segments.append(self.inString[counter:x])
            counter = x
        segments.append(self.inString[x:lenString])
        return segments

    def builder(self, seg):
        usedStrings = []#these are so we dont make duplicat variables
        code = {}

        combinedText = ""#this wil be where all the text is combined

        for part in seg:

            #this will randomly genrate variables
            while True:
                var1 = ''.join([random.choice(string.ascii_lowercase) for x in range(random.randint(5,10))])
                if var1 not in usedStrings:
                    break

            
            #this will obfuscat the string
            randList = []
            for x in part:
                randList.append('chr('+str(ord(x))+')')


            com = ' + '.join(randList)
            code[var1 +' = '+com]=var1

        for x in code.keys():
            #print(x)
            combinedText += str(x)+'\n'

        #print(combinedText)

        return combinedText, code
        #return code

    def final(self, code):
        current = 0
        count = 0

        combinedTextTwo = ""#this string will be the combined code


        #stuff = ' + '.join([y for y in [x for x in code.keys()]])
        values = code.values()
        values_list = list(values)
        #print(self.combinedVar+' = ""')
        #print(self.combinedVar+' += '+values_list[0])

        combinedTextTwo += str(self.combinedVar+' = ""')+'\n'
        combinedTextTwo += str(self.combinedVar+' += '+values_list[0])+'\n'


        for x in range(0, len(code.keys())-2, 2):

            try:
                #print(self.combinedVar+'+= ',values_list[x+1],' + ', values_list[x+2])

                combinedTextTwo += str(self.combinedVar+'+= '+values_list[x+1]+' + '+values_list[x+2])+'\n'

            except IndexError:
        
                pass

        if len(code.keys()) % 2 == False:
            #print(self.combinedVar+' += ', values_list[-1])
            combinedTextTwo += str(self.combinedVar+' += '+ values_list[-1])+'\n'
        return combinedTextTwo


#r = "There are many variations of passages of Lorem Idgdfg psum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc."


#test = stringObjuscator(r)
#test.obfuscat()