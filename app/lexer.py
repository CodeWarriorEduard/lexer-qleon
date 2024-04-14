from tokensClasses import *
class Lexer:
    #Tabla de Simbolos / Para mejorar 
    __stopWords = [" "]
    __lineBreak = "\n"
    __numbers =  "0123456789"
    __operations = ['+','-','/','*','(',')','{','}',';']

    __letters = "abcñdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÑ"
    __declarations = ["crt"] #Crear Variable crt = create
    __reserved = ["if", "elif","else", "while", "for", "show", "blank", "True", "true", "False", "false"]

    __specialCharacters = [">", "<", "=", "&", "|", "!", "#"]   
    __booleans = ["&&", "||"]
    __comparisons = [">", "<", ">=", "<=", "==", "!="]
    __comment = ["###"]


    __string = ['"']


    def __init__(self, code:str):
        self.__code = code
        self.__i = 0
        self.__line = 0
        self.__tokens = []
        self.__chr = self.__code[self.__i]
        self.__token = None
      
    
    def tokenizer(self):
        while self.__i < len(self.__code):

            if self.__chr in Lexer.__numbers: 
                self.__token = self.__extractNumber()

            elif self.__chr in Lexer.__stopWords:
                self.__moveI()
                continue    
                
            elif self.__chr in Lexer.__operations:
                if self.__chr == "+":
                    self.__token = Plus(self.__chr)
                elif self.__chr == "-":
                    self.__token = Minus(self.__chr)
                elif self.__chr == "/":
                    self.__token = Slash(self.__chr)
                elif self.__chr == "*":
                    self.__token = Asterisk(self.__chr)
                elif self.__chr == "(":
                    self.__token = LeftParen(self.__chr)
                elif self.__chr == ")":
                    self.__token = RightParen(self.__chr)
                elif self.__chr == "{":
                    self.__token = LeftBrace(self.__chr)
                elif self.__chr == "}":
                    self.__token = RightBrace(self.__chr)
                elif self.__chr == ";":
                    self.__token = Semicolon(self.__chr)
                

                self.__moveI()
    
            elif self.__chr in Lexer.__letters:
                word = self.__extractWord()
                
                if word in Lexer.__declarations:     
                    self.__token = Declaration(word)

                elif word in Lexer.__reserved:
                    if word == "if":
                        self.__token = If(word)
                    elif word == "elif":
                        self.__token = Elif(word)
                    elif word == "else":
                        self.__token = Else(word)
                    elif word == "while":
                        self.__token = While(word)
                    elif word == "for":
                        self.__token = For(word)
                    elif word == "show":
                        self.__token = Show(word)
                    elif word == "blank":
                        self.__token = Blank(word)
                    elif (word in ("True", "true")):
                        self.__token = Truee(word)
                    elif (word in ("False", "false")):
                        self.__token = Falsee(word)
                else: 
                    self.__token = Variable(word)

            elif self.__chr in Lexer.__string:
                wordl = self.__extractString()
                self.__token = String(wordl)

            elif self.__chr in Lexer.__specialCharacters:
                specialChar = self.__extractEspecialChar()

                if specialChar in Lexer.__booleans:
                    if specialChar == "&&":
                        self.__token = And(specialChar)
                    elif specialChar == "||":
                        self.__token = Or(specialChar)

                elif specialChar in Lexer.__comparisons:
                    if specialChar == ">":
                        self.__token = Greater(specialChar)
                    elif specialChar == "<":
                        self.__token = Less(specialChar)
                    elif specialChar == ">=":
                        self.__token = GreaterEqual(specialChar)
                    elif specialChar == "<=":
                        self.__token = LessEqual(specialChar)
                    elif specialChar == "==":
                        self.__token = EqualEqual(specialChar)
                    elif specialChar == "!=":
                        self.__token = BangEqual(specialChar)

                elif specialChar == '=':
                    self.__token = Assign(specialChar)

                elif specialChar in Lexer.__comment:
                    while ((self.__chr != Lexer.__lineBreak) and (self.__i < len(self.__code))):
                        specialChar += self.__chr
                        self.__moveI()
                    
                    self.__token = Comment(specialChar)
                    if(self.__i ==( len(self.__code)-1)):
                        self.__i == len(self.__code)
                    
                   
            elif self.__chr == Lexer.__lineBreak:
                self.__moveI()
                self.__line += 1
                continue
            else:
                self.__token = Unknown(self.__chr)
                self.__token.setLine(self.__line)
                self.__moveI()

            self.__token.setLine(self.__line)
            self.__tokens.append(self.__token)
        return self.__tokens

    def __extractWord(self):
        word = ""
        while (self.__chr in Lexer.__letters) and (self.__i < len(self.__code)):
            word += self.__chr
            self.__moveI()
        return word     

    def __extractString(self):
        string = ''
        string += self.__chr
        self.__moveI()
        if(self.__i < len(self.__code)):
            while ((self.__chr != '"') and (self.__i < len(self.__code))):
                string += self.__chr 
                self.__moveI()

            if (self.__chr == '"'):
                string += self.__chr
                self.__moveI()
    
        return string        

    def __extractEspecialChar(self):
        especialChar = ""
        while (self.__chr in Lexer.__specialCharacters) and (self.__i < len(self.__code)):
            especialChar += self.__chr 
            self.__moveI()
        return especialChar 

    def __extractNumber(self):
        number = ""
        isFloat = False
        while (self.__chr in Lexer.__numbers or self.__chr == ".") and (self.__i < len(self.__code)):
            if self.__chr == ".":
                isFloat = True
            number += self.__chr
            self.__moveI()
        if isFloat:
            return Float(number)
        else:
            return Integer(number)
        
    def __moveI(self):
        self.__i += 1
        if self.__i < len(self.__code):
            self.__chr = self.__code[self.__i]

    def __clean(self):
        for stopWord in Lexer.__stopWords:
            self.__code = self.__code.replace(stopWord,"")


    def getCode(self)->str:
        return self.__code
    
    def getNumbers(self):
        return Lexer.__numbers
    
    def getStopWords(self):
        return Lexer.__stopWords
    
    def getOperations(self):
        return Lexer.__operations

    def getLetters(self):
        return Lexer.__letters
    
    def getDeclarations(self):
        return Lexer.__declarations
    
    def getReserved(self):
        return Lexer.__reserved
    
    def getSpecialCharacters(self):
        return Lexer.__specialCharacters
    
    def getBooleans(self):
        return Lexer.__booleans
    
    def getComparisons(self):
        return Lexer.__comparisons
    
    def getComment(self):
        return Lexer
    
    def getTokens(self):
        return self.__tokens

    

#lex = Lexer("5+5")
#print(lex.getCode())
#print("------------------")
#lex.tokenizer()
#print("------------------")
#print(lex.getTokens())


